import customtkinter as ctk
import socket
import threading
import ssl
import time
from tkinter import messagebox

# --- Classe principale de l'application CustomTkinter ---
class SocketApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime : Sockets Avancés (TCP, UDP, TLS/SSL, P2P)")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # --- Création du cadre de navigation latéral ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # --- Création des boutons de navigation ---
        self.intro_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Introduction aux Sockets",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_intro)
        self.intro_button.pack(fill="x", padx=10, pady=5)
        
        self.tcp_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="TCP : Le protocole fiable",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_tcp)
        self.tcp_button.pack(fill="x", padx=10, pady=5)
        
        self.udp_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="UDP : Le protocole rapide",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_udp)
        self.udp_button.pack(fill="x", padx=10, pady=5)

        self.ssl_tls_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="TLS/SSL : La sécurité",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_ssl_tls)
        self.ssl_tls_button.pack(fill="x", padx=10, pady=5)
        
        self.p2p_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="P2P : Le réseau décentralisé",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_p2p)
        self.p2p_button.pack(fill="x", padx=10, pady=5)

        # --- Création du cadre principal pour le contenu ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")
        
        # --- Démarrage sur le premier onglet ---
        self.show_intro()

    def set_content(self, title, text, code=None):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        if code:
            self.content_textbox.insert("end", f"\n\n```python\n{code}\n```")
        
        self.content_textbox.configure(state="disabled")

    def show_intro(self):
        content = (
            "**Introduction aux Sockets et Modèles de Communication** 🔌\n\n"
            "Un **socket** est le point de terminaison d'une communication réseau, permettant à deux programmes d'échanger des données. Le module `socket` de Python est l'interface standard pour interagir avec le réseau au niveau le plus bas.\n\n"
            "**Modèles de communication :**\n"
            "- **Client-Serveur** : Un serveur écoute les connexions, tandis que les clients s'y connectent.\n"
            "- **Peer-to-Peer (P2P)** : Chaque participant peut agir à la fois comme client et serveur."
        )
        self.set_content("Introduction aux Sockets", content)

    def show_tcp(self):
        code_example = (
            "import socket, threading, time\n\n"
            "HOST = '127.0.0.1'  # Localhost\n"
            "PORT = 8000\n\n"
            "# --- Fonctions du serveur TCP ---\n"
            "def handle_client(conn, addr):\n"
            "    print(f\"[NOUVELLE CONNEXION] {addr} est connecté.\")\n"
            "    try:\n"
            "        conn.sendall(b'Bienvenue sur le serveur TCP !')\n"
            "        while True:\n"
            "            data = conn.recv(1024)\n"
            "            if not data: break # Le client a fermé la connexion\n"
            "            print(f\"[{addr}] Reçu: {data.decode()}\")\n"
            "            response = f\"Serveur: J'ai bien reçu votre message: {data.decode()}\"\n"
            "            conn.sendall(response.encode())\n"
            "    except socket.error as e:\n"
            "        print(f\"[ERREUR] Erreur de communication avec {addr}: {e}\")\n"
            "    finally:\n"
            "        conn.close()\n"
            "        print(f\"[DECONNEXION] {addr} a quitté.\")\n\n"
            "def start_server():\n"
            "    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
            "    server.bind((HOST, PORT))\n"
            "    server.listen()\n"
            "    print(f\"[EN ÉCOUTE] Le serveur écoute sur {HOST}:{PORT}\")\n"
            "    while True:\n"
            "        conn, addr = server.accept()\n"
            "        thread = threading.Thread(target=handle_client, args=(conn, addr))\n"
            "        thread.start()\n\n"
            "# --- Fonction du client TCP ---\n"
            "def start_client():\n"
            "    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
            "    try:\n"
            "        client.connect((HOST, PORT))\n"
            "        print(f\"[CONNECTÉ] Connecté au serveur sur {HOST}:{PORT}\")\n"
            "        msg = client.recv(1024).decode()\n"
            "        print(f\"[SERVEUR] {msg}\")\n"
            "        client.sendall(b'Bonjour, c\\'est le client TCP !')\n"
            "        response = client.recv(1024).decode()\n"
            "        print(f\"[SERVEUR] {response}\")\n"
            "    except socket.error as e:\n"
            "        print(f\"[ERREUR] Erreur de connexion: {e}\")\n"
            "    finally:\n"
            "        client.close()\n"
            "        print(\"[DÉCONNECTÉ] Connexion fermée.\")\n\n"
            "# --- Démarrage simulé (ne pas exécuter directement) ---\n"
            "# server_thread = threading.Thread(target=start_server)\n"
            "# server_thread.start()\n"
            "# time.sleep(1)\n"
            "# client_thread = threading.Thread(target=start_client)\n"
            "# client_thread.start()\n"
        )
        content = (
            "**TCP (Transmission Control Protocol) : Le protocole fiable** 🌐\n\n"
            "Le TCP est un protocole **orienté connexion**. Il garantit que les données arrivent dans le bon ordre et sans perte, ce qui le rend idéal pour les applications où l'intégrité des données est primordiale (web, emails, transferts de fichiers).\n\n"
            "**Étapes clés :**\n"
            "1.  **Serveur :** Crée un socket, le **lie** (`bind`), se met à l'**écoute** (`listen`) et **accepte** (`accept`) les connexions clientes.\n"
            "2.  **Client :** Crée un socket et tente de se **connecter** (`connect`) au serveur.\n"
            "3.  **Communication :** Les données sont envoyées avec `send()` ou `sendall()` et reçues avec `recv()`.\n\n"
            "**Conseil :** Pour gérer plusieurs clients simultanément, le serveur doit utiliser le **multithreading** en créant un nouveau thread pour chaque client, comme dans l'exemple ci-dessous."
        )
        self.set_content("TCP : Le protocole fiable", content, code_example)
        
    def show_udp(self):
        code_example = (
            "import socket\n"
            "import threading\n"
            "import time\n\n"
            "HOST = '127.0.0.1'\n"
            "PORT = 8001\n\n"
            "# --- Serveur UDP ---\n"
            "def start_udp_server():\n"
            "    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n"
            "    udp_server_socket.bind((HOST, PORT))\n"
            "    print(f\"[SERVEUR UDP] En écoute sur {HOST}:{PORT}\")\n"
            "    try:\n"
            "        data, addr = udp_server_socket.recvfrom(1024)\n"
            "        print(f\"[SERVEUR UDP] Reçu de {addr}: {data.decode()}\")\n"
            "        udp_server_socket.sendto(b'Bonjour, client UDP !', addr)\n"
            "    except socket.error as e:\n"
            "        print(f\"[ERREUR] Erreur UDP: {e}\")\n"
            "    finally:\n"
            "        udp_server_socket.close()\n"
            "        print(\"[SERVEUR UDP] Socket fermé.\")\n\n"
            "# --- Client UDP ---\n"
            "def start_udp_client():\n"
            "    udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n"
            "    try:\n"
            "        message = 'Bonjour depuis le client UDP !'\n"
            "        udp_client_socket.sendto(message.encode(), (HOST, PORT))\n"
            "        print('[CLIENT UDP] Message envoyé.')\n"
            "        data, addr = udp_client_socket.recvfrom(1024)\n"
            "        print(f\"[CLIENT UDP] Reçu de {addr}: {data.decode()}\")\n"
            "    except socket.error as e:\n"
            "        print(f\"[ERREUR] Erreur UDP: {e}\")\n"
            "    finally:\n"
            "        udp_client_socket.close()\n"
            "        print(\"[CLIENT UDP] Socket fermé.\")\n\n"
            "# --- Démarrage simulé (ne pas exécuter directement) ---\n"
            "# server_thread = threading.Thread(target=start_udp_server)\n"
            "# server_thread.start()\n"
            "# time.sleep(1)\n"
            "# client_thread = threading.Thread(target=start_udp_client)\n"
            "# client_thread.start()\n"
        )
        content = (
            "**UDP (User Datagram Protocol) : Le protocole rapide** 💨\n\n"
            "L'UDP est un protocole **sans connexion et non fiable**. Il est plus rapide que le TCP car il n'y a pas de poignée de main et de gestion des erreurs. Il est parfait pour le streaming, les jeux en ligne, ou toute application où la perte de quelques paquets est acceptable pour réduire la latence.\n\n"
            "**Étapes clés :**\n"
            "1.  **Création du socket :** Utilisez `socket.SOCK_DGRAM`.\n"
            "2.  **Communication :** Le serveur et le client utilisent `sendto(data, address)` pour envoyer et `recvfrom(size)` pour recevoir. `recvfrom()` renvoie à la fois les données et l'adresse de l'expéditeur.\n\n"
            "**Conseil :** Comme l'UDP ne garantit pas la livraison, il est recommandé de mettre en place une logique de retransmission côté application si la fiabilité est nécessaire."
        )
        self.set_content("UDP : Le protocole rapide", content, code_example)

    def show_ssl_tls(self):
        code_example = (
            "# Prérequis : créer un certificat et une clé privée\n"
            "# openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem\n\n"
            "import socket, ssl, threading\n\n"
            "HOST = '127.0.0.1'\n"
            "PORT = 8002\n"
            "CERT_PATH = 'cert.pem'\n"
            "KEY_PATH = 'key.pem'\n\n"
            "# --- Serveur TLS/SSL ---\n"
            "def start_ssl_server():\n"
            "    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)\n"
            "    context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)\n"
            "    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:\n"
            "        sock.bind((HOST, PORT))\n"
            "        sock.listen(5)\n"
            "        print(f\"[SERVEUR TLS] Écoute sécurisée sur {HOST}:{PORT}\")\n"
            "        with context.wrap_socket(sock, server_side=True) as ssock:\n"
            "            conn, addr = ssock.accept()\n"
            "            print(f\"[SERVEUR TLS] Connexion sécurisée de {addr}\")\n"
            "            conn.sendall(b'Bienvenue sur le serveur TLS !')\n"
            "            conn.close()\n"
            "            ssock.close()\n\n"
            "# --- Client TLS/SSL ---\n"
            "def start_ssl_client():\n"
            "    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)\n"
            "    context.load_verify_locations(CERT_PATH)\n"
            "    with socket.create_connection((HOST, PORT)) as sock:\n"
            "        with context.wrap_socket(sock, server_hostname=HOST) as ssock:\n"
            "            print('[CLIENT TLS] Connecté au serveur TLS/SSL')\n"
            "            data = ssock.recv(1024)\n"
            "            print(f\"[CLIENT TLS] Reçu: {data.decode()}\")\n"
            "            ssock.close()\n"
            "            sock.close()\n\n"
            "# --- Démarrage simulé (ne pas exécuter directement) ---\n"
            "# server_thread = threading.Thread(target=start_ssl_server)\n"
            "# server_thread.start()\n"
            "# time.sleep(1)\n"
            "# client_thread = threading.Thread(target=start_ssl_client)\n"
            "# client_thread.start()\n"
        )
        content = (
            "**TLS/SSL : Sécuriser la communication réseau** 🔒\n\n"
            "Les protocoles **TLS (Transport Layer Security)** et **SSL** sont utilisés pour chiffrer les données, garantissant ainsi leur confidentialité et leur intégrité. Ils sont essentiels pour toute application traitant d'informations sensibles (mots de passe, données personnelles).\n\n"
            "**Étapes clés :**\n"
            "1.  **Certificats :** Le serveur a besoin d'un certificat et d'une clé privée. `openssl` est l'outil standard pour les générer.\n"
            "2.  **`SSLContext` :** Le module `ssl` utilise un objet `SSLContext` pour gérer la configuration de la connexion sécurisée.\n"
            "3.  **`wrap_socket()` :** Le socket TCP est «enveloppé» dans un `SSLSocket` qui gère automatiquement le chiffrement et le déchiffrement des données. Le reste de la logique (send/recv) reste la même.\n\n"
            "**Conseil :** En production, le client doit vérifier le certificat du serveur pour s'assurer de son authenticité. `context.load_verify_locations()` est utilisé pour valider la chaîne de certificats."
        )
        self.set_content("TLS/SSL : La sécurité", content, code_example)
        
    def show_p2p(self):
        code_example = (
            "import socket, threading, time\n\n"
            "HOST = '127.0.0.1'\n"
            "PORT_A = 8003\n"
            "PORT_B = 8004\n\n"
            "# --- Fonction du pair A (serveur) ---\n"
            "def peer_A_listen():\n"
            "    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
            "    server_socket.bind((HOST, PORT_A))\n"
            "    server_socket.listen(1)\n"
            "    print(f\"[PAIR A] Écoute sur {HOST}:{PORT_A}\")\n"
            "    try:\n"
            "        conn, addr = server_socket.accept()\n"
            "        print(f\"[PAIR A] Connexion acceptée de {addr}\")\n"
            "        data = conn.recv(1024)\n"
            "        print(f\"[PAIR A] Reçu de B: {data.decode()}\")\n"
            "    except socket.error as e:\n"
            "        print(f\"[ERREUR] Erreur sur le pair A: {e}\")\n"
            "    finally:\n"
            "        conn.close() if 'conn' in locals() else None\n"
            "        server_socket.close()\n\n"
            "# --- Fonction du pair B (client) ---\n"
            "def peer_B_connect():\n"
            "    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n"
            "    print(f\"[PAIR B] Tente de se connecter à {HOST}:{PORT_A}\")\n"
            "    try:\n"
            "        time.sleep(1)\n"
            "        client_socket.connect((HOST, PORT_A))\n"
            "        client_socket.sendall(b'Bonjour, c\\'est le pair B !')\n"
            "        print(\"[PAIR B] Message envoyé.\")\n"
            "    except ConnectionRefusedError:\n"
            "        print(\"[ERREUR] Le pair A n'est pas en écoute.\")\n"
            "    finally:\n"
            "        client_socket.close()\n\n"
            "# --- Démarrage simulé (ne pas exécuter directement) ---\n"
            "# thread_A = threading.Thread(target=peer_A_listen)\n"
            # thread_A.start()\n"
            "# thread_B = threading.Thread(target=peer_B_connect)\n"
            # thread_B.start()\n"
        )
        content = (
            "**Architecture P2P (Peer-to-Peer) : Un réseau décentralisé** 🤝\n\n"
            "Le modèle **P2P** est une architecture réseau où chaque participant (un **pair**) est à la fois un serveur et un client. Il peut à la fois accepter des connexions d'autres pairs et en initier lui-même. Il n'y a pas de serveur central.\n\n"
            "**Avantages :**\n"
            "- **Résilience :** Le réseau continue de fonctionner même si plusieurs pairs tombent en panne.\n"
            "- **Évolutivité :** La capacité du réseau augmente avec le nombre de pairs, la charge étant distribuée.\n\n"
            "**Implémentation :**\n"
            "   - Chaque pair doit utiliser un thread pour écouter les connexions entrantes sur un port et un autre pour se connecter aux autres pairs. L'exemple ci-dessous simule une communication simple entre deux pairs."
        )
        self.set_content("P2P : Le réseau décentralisé", content, code_example)

if __name__ == "__main__":
    app = SocketApp()
    app.mainloop()