import customtkinter as ctk
import socket
import threading
import sys
import time

# --- Configuration de l'application ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Variables globales pour le tunnel ---
is_tunnel_running = False
listener_thread = None
udp_socket = None

# --- Fonctions du tunnel UDP ---
def start_udp_tunnel(ip_b, local_port, ip_a, port_a, ip_c, port_c):
    """
    Démarre le tunnel UDP et gère le relai de paquets entre A et C.
    Le tunnel sur B écoute sur l'adresse IP et le port spécifiés.
    """
    global is_tunnel_running, udp_socket

    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((ip_b, local_port))
        
        log_message(f"[*] Tunnel UDP démarré sur B ({ip_b}:{local_port}).")
        log_message(f"[*] Relais bidirectionnel entre A ({ip_a}:{port_a}) et C ({ip_c}:{port_c}).")
        
        is_tunnel_running = True
        
        # Le tunnel a besoin de connaître les adresses de A et C
        addr_a = (ip_a, port_a)
        addr_c = (ip_c, port_c)
        
        while is_tunnel_running:
            try:
                data, addr = udp_socket.recvfrom(4096)
                if not is_tunnel_running:
                    break
                
                # Si le paquet vient de A, on le redirige vers C
                if addr == addr_a:
                    udp_socket.sendto(data, addr_c)
                    log_message(f"-> Paquet de A vers C : {len(data)} octets")
                
                # Si le paquet vient de C, on le redirige vers A
                elif addr == addr_c:
                    udp_socket.sendto(data, addr_a)
                    log_message(f"<- Paquet de C vers A : {len(data)} octets")
                
                # Si le paquet vient d'une autre source, on l'ignore
                else:
                    log_message(f"[!] Paquet ignoré d'une source inconnue : {addr}")
                
            except socket.timeout:
                continue
            except Exception as e:
                if is_tunnel_running:
                    log_message(f"[!] Erreur de relai : {e}")
                break
                
    except Exception as e:
        log_message(f"[!] Échec de démarrage du tunnel UDP : {e}")
        stop_tunnel()
    finally:
        if udp_socket:
            udp_socket.close()
        log_message("[*] Tunnel UDP arrêté.")

def stop_tunnel():
    """Arrête le tunnel en modifiant la variable globale."""
    global is_tunnel_running
    if is_tunnel_running:
        is_tunnel_running = False
        log_message("[*] Arrêt du tunnel en cours...")
        try:
            # Envoyer un paquet pour débloquer le socket
            local_port = int(app.local_port_entry.get())
            ip_b = app.ip_b_entry.get()
            socket.socket(socket.AF_INET, socket.SOCK_DGRAM).sendto(b'', (ip_b, local_port))
        except Exception:
            pass
        if listener_thread and listener_thread.is_alive():
            listener_thread.join(timeout=1)
        log_message("[*] Le tunnel est maintenant arrêté.")

def log_message(message):
    """Ajoute un message dans la zone de texte du GUI."""
    app.log_text.configure(state="normal")
    app.log_text.insert(ctk.END, message + "\n")
    app.log_text.see(ctk.END)
    app.log_text.configure(state="disabled")

# --- Classe de l'interface graphique ---
class TunnelApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tunnel UDP Bidirectionnel")
        self.geometry("700x500")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # --- Widgets de configuration ---
        self.config_frame = ctk.CTkFrame(self)
        self.config_frame.pack(pady=10, padx=10, fill="x")

        # Configuration de la machine A
        ctk.CTkLabel(self.config_frame, text="Machine A").grid(row=0, column=0, columnspan=2, pady=5)
        ctk.CTkLabel(self.config_frame, text="IP A :").grid(row=1, column=0, padx=(5,0))
        self.ip_a_entry = ctk.CTkEntry(self.config_frame, width=120)
        self.ip_a_entry.insert(0, "192.168.1.10")
        self.ip_a_entry.grid(row=1, column=1, padx=5)
        
        ctk.CTkLabel(self.config_frame, text="Port A :").grid(row=2, column=0, padx=(5,0))
        self.port_a_entry = ctk.CTkEntry(self.config_frame, width=80)
        self.port_a_entry.insert(0, "5000")
        self.port_a_entry.grid(row=2, column=1, padx=5)

        # Configuration du Tunnel B
        ctk.CTkLabel(self.config_frame, text="Tunnel B").grid(row=0, column=2, columnspan=2, pady=5)
        ctk.CTkLabel(self.config_frame, text="IP B :").grid(row=1, column=2, padx=(20,0))
        self.ip_b_entry = ctk.CTkEntry(self.config_frame, width=120)
        self.ip_b_entry.insert(0, "192.168.1.20") # IP de votre machine B
        self.ip_b_entry.grid(row=1, column=3, padx=5)
        
        ctk.CTkLabel(self.config_frame, text="Port B :").grid(row=2, column=2, padx=(20,0))
        self.local_port_entry = ctk.CTkEntry(self.config_frame, width=80)
        self.local_port_entry.insert(0, "9999")
        self.local_port_entry.grid(row=2, column=3, padx=5)

        # Configuration de la machine C
        ctk.CTkLabel(self.config_frame, text="Machine C").grid(row=0, column=4, columnspan=2, pady=5)
        ctk.CTkLabel(self.config_frame, text="IP C :").grid(row=1, column=4, padx=(20,0))
        self.ip_c_entry = ctk.CTkEntry(self.config_frame, width=120)
        self.ip_c_entry.insert(0, "192.168.1.50")
        self.ip_c_entry.grid(row=1, column=5, padx=5)
        
        ctk.CTkLabel(self.config_frame, text="Port C :").grid(row=2, column=4, padx=(20,0))
        self.port_c_entry = ctk.CTkEntry(self.config_frame, width=80)
        self.port_c_entry.insert(0, "8080")
        self.port_c_entry.grid(row=2, column=5, padx=5)

        # --- Boutons de contrôle ---
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(pady=5, padx=10, fill="x")

        self.start_button = ctk.CTkButton(self.control_frame, text="Démarrer le tunnel", command=self.on_start_button_click)
        self.start_button.pack(side="left", padx=5, expand=True)

        self.stop_button = ctk.CTkButton(self.control_frame, text="Arrêter le tunnel", command=self.on_stop_button_click, state="disabled")
        self.stop_button.pack(side="left", padx=5, expand=True)

        # --- Zone de logs ---
        self.log_text = ctk.CTkTextbox(self, state="disabled")
        self.log_text.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_start_button_click(self):
        """Action du bouton Démarrer."""
        global listener_thread
        
        try:
            ip_b = self.ip_b_entry.get()
            local_port = int(self.local_port_entry.get())
            ip_a = self.ip_a_entry.get()
            port_a = int(self.port_a_entry.get())
            ip_c = self.ip_c_entry.get()
            port_c = int(self.port_c_entry.get())
        except ValueError:
            log_message("[!] Veuillez entrer des ports valides.")
            return

        if not is_tunnel_running:
            self.start_button.configure(state="disabled")
            self.stop_button.configure(state="normal")
            
            # Lancer le tunnel dans un thread séparé
            listener_thread = threading.Thread(
                target=start_udp_tunnel, 
                args=(ip_b, local_port, ip_a, port_a, ip_c, port_c)
            )
            listener_thread.daemon = True
            listener_thread.start()

    def on_stop_button_click(self):
        """Action du bouton Arrêter."""
        stop_tunnel()
        self.start_button.configure(state="normal")
        self.stop_button.configure(state="disabled")
        
    def on_closing(self):
        """Gère la fermeture de la fenêtre."""
        stop_tunnel()
        self.destroy()

if __name__ == "__main__":
    app = TunnelApp()
    app.mainloop()