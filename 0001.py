import customtkinter
import threading
import socket
import queue
import os
import struct
import time
from datetime import datetime
from tkinter import messagebox

# Constantes pour le protocole du tunnel
# Correspond aux constantes du script du tunnel
TUNNEL_CLIENT_ID = 2       # Message de l'ID assigné
TUNNEL_MSG_FORWARD = 3     # Paquet de données à relayer (le client ne l'utilise pas en tant que tel, mais le reçoit)
PACKET_HEADER_FORMAT = "!HL" # ID Dest/Source(2B), Taille(4B)
PACKET_HEADER_SIZE = struct.calcsize(PACKET_HEADER_FORMAT)
TCP_CHUNK_SIZE = 4096

class TunnelClientApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Application Client Tunnel")
        self.geometry("600x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- Cadre de Connexion et d'envoi ---
        self.client_frame = customtkinter.CTkFrame(self)
        self.client_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.client_frame.grid_columnconfigure(1, weight=1)

        self.client_label = customtkinter.CTkLabel(self.client_frame, text="--- Client Tunnel ---", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.client_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.target_ip_label = customtkinter.CTkLabel(self.client_frame, text="IP du Tunnel:")
        self.target_ip_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.target_ip_entry = customtkinter.CTkEntry(self.client_frame)
        self.target_ip_entry.insert(0, "127.0.0.1")
        self.target_ip_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.target_port_label = customtkinter.CTkLabel(self.client_frame, text="Port du Tunnel:")
        self.target_port_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.target_port_entry = customtkinter.CTkEntry(self.client_frame)
        self.target_port_entry.insert(0, "9999")
        self.target_port_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.connect_button = customtkinter.CTkButton(self.client_frame, text="Connecter", command=self.connect_to_tunnel)
        self.connect_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
        self.disconnect_button = customtkinter.CTkButton(self.client_frame, text="Déconnecter", command=self.disconnect_from_tunnel, state="disabled")
        self.disconnect_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.my_id_label = customtkinter.CTkLabel(self.client_frame, text="Mon ID: Non connecté", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.my_id_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # --- Zone d'envoi de message ---
        self.send_frame = customtkinter.CTkFrame(self.client_frame)
        self.send_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.send_frame.grid_columnconfigure(1, weight=1)

        self.dest_id_label = customtkinter.CTkLabel(self.send_frame, text="ID de Destination:")
        self.dest_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.dest_id_entry = customtkinter.CTkEntry(self.send_frame, width=50)
        self.dest_id_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.message_label = customtkinter.CTkLabel(self.send_frame, text="Message:")
        self.message_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.message_entry = customtkinter.CTkEntry(self.send_frame, placeholder_text="Tapez votre message ici...")
        self.message_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.send_button = customtkinter.CTkButton(self.send_frame, text="Envoyer le message", command=self.send_message, state="disabled")
        self.send_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Log du client
        self.client_log_text = customtkinter.CTkTextbox(self, height=400)
        self.client_log_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.client_log_text.configure(state="disabled")

        # --- Variables d'état ---
        self.client_socket = None
        self.client_thread = None
        self.client_running = threading.Event()
        self.my_tunnel_id = None
        self.client_message_queue = queue.Queue()

        self.after(100, self.check_client_message_queue)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def log_client_message(self, message):
        """Affiche un message dans la zone de log du client."""
        self.client_log_text.configure(state="normal")
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.client_log_text.insert("end", f"[{timestamp}] {message}\n")
        self.client_log_text.see("end")
        self.client_log_text.configure(state="disabled")

    def check_client_message_queue(self):
        """Vérifie périodiquement la file d'attente des messages système du client."""
        try:
            while True:
                message = self.client_message_queue.get_nowait()
                self.log_client_message(message)
        except queue.Empty:
            pass
        self.after(100, self.check_client_message_queue)

    def connect_to_tunnel(self):
        """Tente de se connecter au tunnel et de recevoir un ID."""
        ip = self.target_ip_entry.get()
        try:
            port = int(self.target_port_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un port valide.")
            return

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(5.0)

        try:
            self.client_socket.connect((ip, port))
            self.client_message_queue.put(f"Connexion réussie au tunnel sur {ip}:{port}.")
            
            # Attendre de recevoir l'ID du tunnel
            header = self.receive_all(self.client_socket, 3) # 1B type + 2B ID
            if not header:
                raise Exception("Connexion fermée par le tunnel lors de l'attente de l'ID.")
            
            msg_type, assigned_id = struct.unpack("!BH", header)

            if msg_type == TUNNEL_CLIENT_ID:
                self.my_tunnel_id = assigned_id
                self.client_message_queue.put(f"ID temporaire assigné par le tunnel: {self.my_tunnel_id}")
                self.my_id_label.configure(text=f"Mon ID: {self.my_tunnel_id}")
                self.client_running.set()
                self.connect_button.configure(state="disabled")
                self.disconnect_button.configure(state="normal")
                self.send_button.configure(state="normal")
                
                # Démarrer le thread d'écoute
                self.client_thread = threading.Thread(target=self.listen_for_messages, daemon=True)
                self.client_thread.start()
            else:
                raise Exception(f"Reçu un type de message inattendu de l'ID du tunnel: {msg_type}")

        except socket.timeout:
            messagebox.showerror("Erreur de connexion", "Délai d'attente dépassé lors de la connexion au tunnel.")
            self.disconnect_from_tunnel(notify=False)
        except Exception as e:
            messagebox.showerror("Erreur de connexion", f"Échec de la connexion au tunnel: {e}")
            self.disconnect_from_tunnel(notify=False)

    def disconnect_from_tunnel(self, notify=True):
        """Déconnecte le client du tunnel."""
        self.client_running.clear()
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
        
        self.my_tunnel_id = None
        self.my_id_label.configure(text="Mon ID: Non connecté")
        self.connect_button.configure(state="normal")
        self.disconnect_button.configure(state="disabled")
        self.send_button.configure(state="disabled")
        
        if notify:
            self.client_message_queue.put("Déconnecté du tunnel.")
            messagebox.showinfo("Déconnexion", "Déconnecté du tunnel.")
        
    def send_message(self):
        """Envoie un message au client de destination via le tunnel."""
        if not self.client_socket or not self.client_running.is_set():
            messagebox.showerror("Erreur", "Veuillez d'abord vous connecter au tunnel.")
            return

        try:
            dest_id = int(self.dest_id_entry.get())
        except ValueError:
            messagebox.showerror("Erreur", "L'ID de destination doit être un nombre.")
            return
        
        message = self.message_entry.get()
        if not message:
            messagebox.showwarning("Avertissement", "Le message ne peut pas être vide.")
            return
            
        message_bytes = message.encode('utf-8')
        if len(message_bytes) > 0xFFFFFFFF:
             messagebox.showerror("Erreur", "Le message est trop volumineux pour être envoyé.")
             return

        # Format du paquet: [ID_Dest(2B)][Taille(4B)][Données]
        header = struct.pack(PACKET_HEADER_FORMAT, dest_id, len(message_bytes))
        packet = header + message_bytes

        try:
            self.client_socket.sendall(packet)
            self.client_message_queue.put(f"Message envoyé à l'ID {dest_id}: '{message}'")
            self.message_entry.delete(0, customtkinter.END)
        except Exception as e:
            self.client_message_queue.put(f"Erreur d'envoi du message: {e}")
            self.disconnect_from_tunnel(notify=True)

    def listen_for_messages(self):
        """Écoute les messages entrants du tunnel dans un thread séparé."""
        while self.client_running.is_set():
            try:
                # Recevoir l'en-tête du paquet: [ID_Source(2B)][Taille(4B)]
                header = self.receive_all(self.client_socket, PACKET_HEADER_SIZE)
                if not header:
                    self.client_message_queue.put("Le tunnel a fermé la connexion.")
                    break
                
                source_id, msg_len = struct.unpack(PACKET_HEADER_FORMAT, header)
                
                # Recevoir le contenu du message
                message_data = self.receive_all(self.client_socket, msg_len)
                if not message_data or len(message_data) != msg_len:
                    self.client_message_queue.put(f"Erreur: Données de message incomplètes de l'ID {source_id}.")
                    continue
                    
                message = message_data.decode('utf-8')
                self.client_message_queue.put(f"Message reçu de l'ID {source_id}: '{message}'")
                
            except socket.timeout:
                continue
            except Exception as e:
                if self.client_running.is_set():
                    self.client_message_queue.put(f"Erreur de réception du tunnel: {e}")
                break
        
        self.disconnect_from_tunnel(notify=True)

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
        self.disconnect_from_tunnel(notify=False)
        self.destroy()

if __name__ == "__main__":
    app = TunnelClientApp()
    app.mainloop()