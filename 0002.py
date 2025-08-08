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
PACKET_HEADER_FORMAT = "!HL" # ID Dest(2B), Taille(4B)
PACKET_HEADER_SIZE = struct.calcsize(PACKET_HEADER_FORMAT)
TCP_CHUNK_SIZE = 4096

class TunnelApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application Tunnel Réseau")
        self.geometry("600x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Cadre Tunnel ---
        self.tunnel_frame = customtkinter.CTkFrame(self)
        self.tunnel_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.tunnel_frame.grid_columnconfigure(1, weight=1)

        self.tunnel_label = customtkinter.CTkLabel(self.tunnel_frame, text="--- Tunnel (Relais TCP) ---", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.tunnel_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.ip_b_label = customtkinter.CTkLabel(self.tunnel_frame, text="IP Tunnel:")
        self.ip_b_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.ip_b_entry = customtkinter.CTkEntry(self.tunnel_frame, placeholder_text="127.0.0.1")
        self.ip_b_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.local_port_label = customtkinter.CTkLabel(self.tunnel_frame, text="Port d'écoute:")
        self.local_port_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.local_port_entry = customtkinter.CTkEntry(self.tunnel_frame, placeholder_text="9999")
        self.local_port_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        
        self.start_tunnel_button = customtkinter.CTkButton(self.tunnel_frame, text="Démarrer le Tunnel", command=self.start_tunnel)
        self.start_tunnel_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.stop_tunnel_button = customtkinter.CTkButton(self.tunnel_frame, text="Arrêter le Tunnel", command=self.stop_tunnel, state="disabled")
        self.stop_tunnel_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        # Log du Tunnel
        self.tunnel_log_text = customtkinter.CTkTextbox(self, height=400)
        self.tunnel_log_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.tunnel_log_text.configure(state="disabled")

        # --- Variables d'état ---
        self.tunnel_thread = None
        self.tunnel_running = threading.Event()
        self.tunnel_message_queue = queue.Queue()
        self.client_id_map = {} # ID -> Socket
        self.reverse_client_id_map = {} # Socket -> ID
        self.next_id = 1
        self.client_sockets = {} # Pour suivre les sockets actifs
        
        self.after(100, self.check_tunnel_message_queue)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

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
        """Démarre le tunnel TCP."""
        if self.tunnel_running.is_set():
            self.log_tunnel_message("Le tunnel est déjà en cours d'exécution.")
            return
        
        try:
            ip_b = self.ip_b_entry.get()
            local_port = int(self.local_port_entry.get())
        except ValueError:
            self.log_tunnel_message("[!] Veuillez entrer des ports valides.")
            return

        self.tunnel_running.set()
        
        self.tunnel_thread = threading.Thread(
            target=self.run_tcp_tunnel,
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
            try:
                ip_b = self.ip_b_entry.get()
                local_port = int(self.local_port_entry.get())
                dummy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dummy_sock.connect((ip_b, local_port))
                dummy_sock.close()
            except Exception:
                pass
            
            if self.tunnel_thread and self.tunnel_thread.is_alive():
                self.tunnel_thread.join(timeout=1)
            
            # Ferme tous les sockets clients restants
            for conn in self.client_sockets.values():
                try:
                    conn.close()
                except Exception:
                    pass
            self.client_id_map.clear()
            self.reverse_client_id_map.clear()
            self.client_sockets.clear()
            
            self.tunnel_message_queue.put("[*] Le tunnel est maintenant arrêté.")
        else:
            self.tunnel_message_queue.put("[!] Le tunnel n'est pas en cours d'exécution.")
        
        self.start_tunnel_button.configure(state="normal")
        self.stop_tunnel_button.configure(state="disabled")

    def get_next_tunnel_id(self):
        """Génère un ID temporaire unique."""
        while self.next_id in self.client_id_map:
            self.next_id += 1
            if self.next_id > 65535: # Limite pour un short int
                self.next_id = 1
        return self.next_id
            
    def run_tcp_tunnel(self, ip_b, local_port):
        """Logique principale du tunnel TCP, gérant les connexions et l'attribution d'ID."""
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
                    
                    self.tunnel_message_queue.put(f"[*] Nouvelle connexion acceptée de {addr_source}, ID assigné: {client_id}")

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
                        # Nouveau format: [ID_Source(2B)][Taille(4B)][Données]
                        forward_header = struct.pack(PACKET_HEADER_FORMAT, client_id, msg_len)
                        target_conn.sendall(forward_header + data)
                        self.tunnel_message_queue.put(f"-> Relai de (ID {client_id}) vers (ID {id_dest}): {msg_len} octets")
                    else:
                        self.tunnel_message_queue.put(f"[!] ID de destination {id_dest} non trouvé pour le paquet de (ID {client_id}).")
                        
        except Exception as e:
            if self.tunnel_running.is_set():
                self.tunnel_message_queue.put(f"[!] Erreur de gestion de la connexion (ID {client_id}): {e}")
        finally:
            self.remove_client(conn)

    def remove_client(self, conn):
        """Nettoie les références d'un client après sa déconnexion."""
        if conn in self.reverse_client_id_map:
            client_id = self.reverse_client_id_map[conn]
            del self.client_id_map[client_id]
            del self.reverse_client_id_map[conn]
            if client_id in self.client_sockets:
                del self.client_sockets[client_id]
            self.tunnel_message_queue.put(f"[*] Client (ID {client_id}) retiré des tables de routage.")

    def receive_all(self, sock, n_bytes):
        """Fonction d'aide pour s'assurer que tous les n_bytes sont reçus d'un socket TCP."""
        data = b''
        while len(data) < n_bytes:
            packet = sock.recv(n_bytes - len(data))
            if not packet:
                return None
            data += packet
        return data
            
    def on_closing(self):
        """Gère la fermeture de la fenêtre."""
        self.stop_tunnel()
        self.destroy()

if __name__ == "__main__":
    app = TunnelApp()
    app.mainloop()