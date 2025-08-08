import customtkinter
import threading
import socket
import queue
import os
import struct
import time
from datetime import datetime

# Constantes du tunnel
MAX_CONNECTIONS = 10
TUNNEL_REQ_ID = 1  # Demande d'ID au tunnel (ne devrait pas être utilisé par le client)
TUNNEL_CLIENT_ID = 2 # Message de l'ID assigné
TUNNEL_MSG_FORWARD = 3 # Paquet de données à relayer
# Le format d'en-tête est utilisé pour les messages internes, mais la logique
# de transmission sera différente pour UDP.
PACKET_HEADER_FORMAT = "!HL" # ID Dest(2B), Taille(4B)
PACKET_HEADER_SIZE = struct.calcsize(PACKET_HEADER_FORMAT)
TCP_CHUNK_SIZE = 4096

class TunnelApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application Tunnel Réseau (TCP/UDP)")
        self.geometry("600x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Cadre Tunnel ---
        self.tunnel_frame = customtkinter.CTkFrame(self)
        self.tunnel_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tunnel_frame.grid_columnconfigure(1, weight=1)

        self.tunnel_label = customtkinter.CTkLabel(self.tunnel_frame, text="--- Tunnel (Relais TCP/UDP) ---", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.tunnel_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.ip_b_label = customtkinter.CTkLabel(self.tunnel_frame, text="IP Tunnel:")
        self.ip_b_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.ip_b_entry = customtkinter.CTkEntry(self.tunnel_frame, placeholder_text="127.0.0.1")
        self.ip_b_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.local_port_label = customtkinter.CTkLabel(self.tunnel_frame, text="Port d'écoute:")
        self.local_port_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.local_port_entry = customtkinter.CTkEntry(self.tunnel_frame, placeholder_text="9999")
        self.local_port_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.protocol_label = customtkinter.CTkLabel(self.tunnel_frame, text="Protocole:")
        self.protocol_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.protocol_optionmenu = customtkinter.CTkOptionMenu(self.tunnel_frame, values=["TCP", "UDP"], command=self.protocol_changed)
        self.protocol_optionmenu.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.start_tunnel_button = customtkinter.CTkButton(self.tunnel_frame, text="Démarrer le Tunnel", command=self.start_tunnel)
        self.start_tunnel_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")
        self.stop_tunnel_button = customtkinter.CTkButton(self.tunnel_frame, text="Arrêter le Tunnel", command=self.stop_tunnel, state="disabled")
        self.stop_tunnel_button.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        # Log du Tunnel
        self.tunnel_log_text = customtkinter.CTkTextbox(self, height=400)
        self.tunnel_log_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.tunnel_log_text.configure(state="disabled")

        # --- Variables d'état ---
        self.tunnel_thread = None
        self.tunnel_running = threading.Event()
        self.tunnel_message_queue = queue.Queue()
        
        # Pour TCP
        self.client_id_map = {} # ID -> Socket
        self.reverse_client_id_map = {} # Socket -> ID
        self.next_id = 1
        self.client_sockets = {} # Pour suivre les sockets actifs
        
        # Pour UDP
        self.udp_addr_map = {} # ID -> (ip, port)
        self.udp_id_map = {} # (ip, port) -> ID

        self.after(100, self.check_tunnel_message_queue)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def protocol_changed(self, choice):
        """Met à jour l'interface si le protocole change."""
        # Dans ce cas simple, aucune mise à jour de l'interface n'est nécessaire,
        # mais la logique est prête si des champs spécifiques au protocole sont ajoutés.
        self.log_tunnel_message(f"Protocole sélectionné : {choice}")

    def log_tunnel_message(self, message):
        """Affiche un message dans la zone de log du tunnel."""
        self.tunnel_log_text.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.tunnel_log_text.insert("end", f"[{timestamp}] {message}\n")
        self.tunnel_log_text.see("end")
        self.tunnel_log_text.configure(state="disabled")

    def check_tunnel_message_queue(self):
        """Vérifie périodiquement la file d'attente des messages système du tunnel."""
        try:
            while True:
                message = self.tunnel_message_queue.get_nowait()
                self.log_tunnel_message(message)
        except queue.Empty:
            pass
        self.after(100, self.check_tunnel_message_queue)

    def start_tunnel(self):
        """Démarre le tunnel selon le protocole sélectionné."""
        if self.tunnel_running.is_set():
            self.log_tunnel_message("Le tunnel est déjà en cours d'exécution.")
            return
        
        try:
            ip_b = self.ip_b_entry.get()
            local_port = int(self.local_port_entry.get())
            protocol = self.protocol_optionmenu.get()
        except ValueError:
            self.log_tunnel_message("[!] Veuillez entrer des ports valides.")
            return

        self.tunnel_running.set()
        
        if protocol == "TCP":
            target_func = self.run_tcp_tunnel
        else: # UDP
            target_func = self.run_udp_tunnel

        self.tunnel_thread = threading.Thread(
            target=target_func,
            args=(ip_b, local_port)
        )
        self.tunnel_thread.daemon = True
        self.tunnel_thread.start()

        self.start_tunnel_button.configure(state="disabled")
        self.stop_tunnel_button.configure(state="normal")
        
    def stop_tunnel(self):
        """Arrête le tunnel."""
        if self.tunnel_running.is_set():
            self.tunnel_running.clear()
            self.tunnel_message_queue.put("[*] Arrêt du tunnel en cours...")
            
            # Ferme les sockets pour arrêter les threads d'écoute
            try:
                ip_b = self.ip_b_entry.get()
                local_port = int(self.local_port_entry.get())
                protocol = self.protocol_optionmenu.get()
                
                if protocol == "TCP":
                    dummy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    dummy_sock.connect((ip_b, local_port))
                    dummy_sock.close()
                else: # UDP
                    # Un dummy send est suffisant pour le sortir du recvfrom()
                    dummy_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    dummy_sock.sendto(b'stop', (ip_b, local_port))
                    dummy_sock.close()
            except Exception:
                pass
            
            if self.tunnel_thread and self.tunnel_thread.is_alive():
                self.tunnel_thread.join(timeout=1)
            
            # Nettoie les structures de données
            self.cleanup_all_clients()
            
            self.tunnel_message_queue.put("[*] Le tunnel est maintenant arrêté.")
        else:
            self.tunnel_message_queue.put("[!] Le tunnel n'est pas en cours d'exécution.")
        
        self.start_tunnel_button.configure(state="normal")
        self.stop_tunnel_button.configure(state="disabled")

    def cleanup_all_clients(self):
        """Ferme tous les sockets clients et vide les tables de routage."""
        for conn in self.client_sockets.values():
            try:
                conn.close()
            except Exception:
                pass
        self.client_id_map.clear()
        self.reverse_client_id_map.clear()
        self.client_sockets.clear()
        self.udp_addr_map.clear()
        self.udp_id_map.clear()
        self.next_id = 1

    def get_next_tunnel_id(self):
        """Génère un ID temporaire unique."""
        # Fonction utilisée par les deux protocoles
        current_ids = set(self.client_id_map.keys()) | set(self.udp_addr_map.keys())
        while self.next_id in current_ids:
            self.next_id += 1
            if self.next_id > 65535: # Limite pour un short int
                self.next_id = 1
        return self.next_id
            
    def run_tcp_tunnel(self, ip_b, local_port):
        """Logique principale du tunnel TCP."""
        server_socket = None
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((ip_b, local_port))
            server_socket.listen(MAX_CONNECTIONS)
            server_socket.settimeout(1.0)
            
            self.tunnel_message_queue.put(f"[*] Tunnel TCP démarré sur {ip_b}:{local_port}.")
            self.tunnel_message_queue.put(f"[*] Prêt à accepter jusqu'à {MAX_CONNECTIONS} clients.")

            while self.tunnel_running.is_set():
                try:
                    conn, addr_source = server_socket.accept()
                    if len(self.client_id_map) >= MAX_CONNECTIONS:
                        self.tunnel_message_queue.put(f"[!] Rejet de la connexion de {addr_source}: Capacité maximale atteinte ({MAX_CONNECTIONS}).")
                        conn.close()
                        continue
                        
                    client_id = self.get_next_tunnel_id()
                    self.client_id_map[client_id] = conn
                    self.reverse_client_id_map[conn] = client_id
                    self.client_sockets[client_id] = conn
                    
                    self.tunnel_message_queue.put(f"[*] Nouvelle connexion TCP de {addr_source}, ID assigné: {client_id}")

                    # Envoie l'ID au client
                    id_msg = struct.pack("!BH", TUNNEL_CLIENT_ID, client_id)
                    conn.sendall(id_msg)

                    # Lance un thread pour gérer cette nouvelle connexion
                    tunnel_handler_thread = threading.Thread(
                        target=self.handle_tcp_tunnel_connection,
                        args=(conn, addr_source, client_id)
                    )
                    tunnel_handler_thread.daemon = True
                    tunnel_handler_thread.start()

                except socket.timeout:
                    continue
                except Exception as e:
                    self.tunnel_message_queue.put(f"[!] Erreur d'écoute du tunnel TCP: {e}")
                    break
        
        except Exception as e:
            self.tunnel_message_queue.put(f"[!] Échec de démarrage du tunnel TCP: {e}")
            self.stop_tunnel()
        finally:
            if server_socket:
                server_socket.close()
            self.tunnel_message_queue.put("[*] Tunnel TCP arrêté.")
            
    def handle_tcp_tunnel_connection(self, conn, addr_source, client_id):
        """Gère une connexion individuelle dans le tunnel TCP."""
        try:
            with conn:
                while self.tunnel_running.is_set():
                    # Format de message du client: [ID_Dest(2B)][Taille(4B)][Données]
                    header = self.receive_all(conn, PACKET_HEADER_SIZE)
                    if not header:
                        self.tunnel_message_queue.put(f"[*] Connexion de {addr_source} (ID {client_id}) fermée.")
                        break

                    id_dest, msg_len = struct.unpack(PACKET_HEADER_FORMAT, header)

                    if id_dest == 0: # Convention pour déconnexion propre si nécessaire
                        self.tunnel_message_queue.put(f"[*] Client {client_id} demande la déconnexion.")
                        break

                    data = self.receive_all(conn, msg_len)
                    if not data or len(data) != msg_len:
                        self.tunnel_message_queue.put(f"[!] Erreur: Données incomplètes de {addr_source} (ID {client_id})")
                        break

                    target_conn = self.client_id_map.get(id_dest)
                    if target_conn:
                        # Envoie les données au destinataire, avec l'ID source
                        forward_header = struct.pack(PACKET_HEADER_FORMAT, client_id, msg_len)
                        target_conn.sendall(forward_header + data)
                        self.tunnel_message_queue.put(f"-> Relai (TCP) de (ID {client_id}) vers (ID {id_dest}): {msg_len} octets")
                    else:
                        self.tunnel_message_queue.put(f"[!] ID de destination {id_dest} non trouvé pour le paquet de (ID {client_id}).")
                        
        except Exception as e:
            if self.tunnel_running.is_set():
                self.tunnel_message_queue.put(f"[!] Erreur de gestion de la connexion (TCP) (ID {client_id}): {e}")
        finally:
            self.remove_client(conn)

    def remove_client(self, conn):
        """Nettoie les références d'un client TCP après sa déconnexion."""
        if conn in self.reverse_client_id_map:
            client_id = self.reverse_client_id_map[conn]
            del self.client_id_map[client_id]
            del self.reverse_client_id_map[conn]
            if client_id in self.client_sockets:
                del self.client_sockets[client_id]
            self.tunnel_message_queue.put(f"[*] Client (TCP) (ID {client_id}) retiré des tables de routage.")

    def receive_all(self, sock, n_bytes):
        """Fonction d'aide pour s'assurer que tous les n_bytes sont reçus d'un socket TCP."""
        data = b''
        while len(data) < n_bytes:
            packet = sock.recv(n_bytes - len(data))
            if not packet:
                return None
            data += packet
        return data

    def run_udp_tunnel(self, ip_b, local_port):
        """Logique principale du tunnel UDP."""
        server_socket = None
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((ip_b, local_port))
            server_socket.settimeout(1.0)
            
            self.tunnel_message_queue.put(f"[*] Tunnel UDP démarré sur {ip_b}:{local_port}.")
            
            while self.tunnel_running.is_set():
                try:
                    # UDP reçoit des données et l'adresse de l'expéditeur
                    data, addr_source = server_socket.recvfrom(TCP_CHUNK_SIZE)
                    
                    # Le premier message d'un client UDP demande un ID
                    if addr_source not in self.udp_id_map:
                        client_id = self.get_next_tunnel_id()
                        self.udp_id_map[addr_source] = client_id
                        self.udp_addr_map[client_id] = addr_source
                        self.tunnel_message_queue.put(f"[*] Nouvelle connexion UDP de {addr_source}, ID assigné: {client_id}")

                        # Envoie l'ID au client
                        id_msg = struct.pack("!BH", TUNNEL_CLIENT_ID, client_id)
                        server_socket.sendto(id_msg, addr_source)
                        continue # Passe au message suivant

                    # Gère les messages de données après l'attribution de l'ID
                    client_id = self.udp_id_map[addr_source]
                    
                    # Le format des messages de données UDP est le même que TCP pour simplifier
                    if len(data) < PACKET_HEADER_SIZE:
                        self.tunnel_message_queue.put(f"[!] Paquet UDP incomplet de {addr_source}")
                        continue
                    
                    header = data[:PACKET_HEADER_SIZE]
                    payload = data[PACKET_HEADER_SIZE:]
                    
                    id_dest, msg_len = struct.unpack(PACKET_HEADER_FORMAT, header)

                    if id_dest == 0: # Déconnexion
                        self.tunnel_message_queue.put(f"[*] Client (UDP) {client_id} demande la déconnexion.")
                        self.remove_udp_client(addr_source)
                        continue

                    target_addr = self.udp_addr_map.get(id_dest)
                    if target_addr:
                        # Crée le nouvel en-tête avec l'ID source
                        forward_header = struct.pack(PACKET_HEADER_FORMAT, client_id, len(payload))
                        server_socket.sendto(forward_header + payload, target_addr)
                        self.tunnel_message_queue.put(f"-> Relai (UDP) de (ID {client_id}) vers (ID {id_dest}): {len(payload)} octets")
                    else:
                        self.tunnel_message_queue.put(f"[!] ID de destination {id_dest} non trouvé pour le paquet de (ID {client_id}).")

                except socket.timeout:
                    continue
                except Exception as e:
                    self.tunnel_message_queue.put(f"[!] Erreur de gestion de la connexion UDP: {e}")
                    break
        
        except Exception as e:
            self.tunnel_message_queue.put(f"[!] Échec de démarrage du tunnel UDP: {e}")
            self.stop_tunnel()
        finally:
            if server_socket:
                server_socket.close()
            self.tunnel_message_queue.put("[*] Tunnel UDP arrêté.")
    
    def remove_udp_client(self, addr):
        """Nettoie les références d'un client UDP."""
        if addr in self.udp_id_map:
            client_id = self.udp_id_map[addr]
            del self.udp_id_map[addr]
            del self.udp_addr_map[client_id]
            self.tunnel_message_queue.put(f"[*] Client (UDP) (ID {client_id}) retiré des tables de routage.")

    def on_closing(self):
        """Gère la fermeture de la fenêtre."""
        self.stop_tunnel()
        self.destroy()

if __name__ == "__main__":
    app = TunnelApp()
    app.mainloop()
