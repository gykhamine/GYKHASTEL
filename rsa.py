import customtkinter
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption
from cryptography.hazmat.backends import default_backend

# Configuration de la fenêtre principale
app = customtkinter.CTk()
app.title("RSA Cryptographie Asymétrique")
app.geometry("800x650")

# Variables pour stocker les clés RSA
private_key = None
public_key = None
encrypted_message = None

def generate_keys():
    """Génère une paire de clés RSA et les affiche."""
    global private_key, public_key
    
    try:
        # 1. Générer une clé privée RSA (taille de 2048 bits)
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        # Extraire la clé publique de la clé privée
        public_key = private_key.public_key()

        # 2. Sérialiser les clés pour l'affichage (format PEM)
        private_pem = private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo
        )

        # 3. Afficher les clés dans les zones de texte
        output_private_key.delete("1.0", "end")
        output_private_key.insert("1.0", private_pem.decode("utf-8"))
        output_public_key.delete("1.0", "end")
        output_public_key.insert("1.0", public_pem.decode("utf-8"))
        
        status_label.configure(text="Paire de clés RSA générée !", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Erreur lors de la génération des clés : {e}", text_color="red")


def encrypt_message():
    """Chiffre le message avec la clé publique et l'affiche."""
    global encrypted_message
    
    message_str = entry_message.get()
    if not public_key or not message_str:
        status_label.configure(text="Veuillez générer des clés et entrer un message.", text_color="red")
        return

    # Le message doit être converti en octets pour le chiffrement
    message_bytes = message_str.encode("utf-8")

    # 4. Chiffrement avec la clé publique
    try:
        encrypted_message = public_key.encrypt(
            message_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        output_encrypted_message.delete("1.0", "end")
        output_encrypted_message.insert("1.0", encrypted_message.hex())
        status_label.configure(text="Message chiffré !", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Erreur de chiffrement : {e}", text_color="red")


def decrypt_message():
    """Déchiffre le message avec la clé privée et l'affiche."""
    global private_key, encrypted_message
    
    if not private_key or not encrypted_message:
        status_label.configure(text="Veuillez d'abord chiffrer un message.", text_color="red")
        return
    
    # 5. Déchiffrement avec la clé privée
    try:
        decrypted_message_bytes = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        output_decrypted_message.delete("1.0", "end")
        output_decrypted_message.insert("1.0", decrypted_message_bytes.decode("utf-8"))
        status_label.configure(text="Déchiffrement réussi !", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Échec du déchiffrement : {e}", text_color="red")
        output_decrypted_message.delete("1.0", "end")
        output_decrypted_message.insert("1.0", "Erreur : le message a peut-être été altéré ou la clé privée est incorrecte.")


# Création des widgets
# --- Le changement principal est ici : on utilise CTkScrollableFrame ---
scrollable_frame = customtkinter.CTkScrollableFrame(master=app)
scrollable_frame.pack(pady=20, padx=60, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=scrollable_frame, text="RSA Cryptographie Asymétrique", font=("Roboto", 24))
label_title.pack(pady=12, padx=10)

button_generate_keys = customtkinter.CTkButton(master=scrollable_frame, text="Générer les clés RSA", command=generate_keys)
button_generate_keys.pack(pady=(20, 10), padx=10)

status_label = customtkinter.CTkLabel(master=scrollable_frame, text="", text_color="green")
status_label.pack(pady=5, padx=10)

label_public_key = customtkinter.CTkLabel(master=scrollable_frame, text="Clé Publique (pour chiffrer) :")
label_public_key.pack(pady=(10, 0), padx=10, anchor="w")
output_public_key = customtkinter.CTkTextbox(master=scrollable_frame, height=80)
output_public_key.pack(pady=5, padx=10, fill="x")

label_private_key = customtkinter.CTkLabel(master=scrollable_frame, text="Clé Privée (pour déchiffrer) :")
label_private_key.pack(pady=(10, 0), padx=10, anchor="w")
output_private_key = customtkinter.CTkTextbox(master=scrollable_frame, height=80)
output_private_key.pack(pady=5, padx=10, fill="x")

label_message = customtkinter.CTkLabel(master=scrollable_frame, text="Message à chiffrer :")
label_message.pack(pady=(20, 0), padx=10, anchor="w")
entry_message = customtkinter.CTkEntry(master=scrollable_frame, placeholder_text="Entrez votre message ici...", width=500)
entry_message.pack(pady=5, padx=10, fill="x")

button_encrypt = customtkinter.CTkButton(master=scrollable_frame, text="Chiffrer", command=encrypt_message)
button_encrypt.pack(pady=5, padx=10)

label_encrypted = customtkinter.CTkLabel(master=scrollable_frame, text="Message chiffré :")
label_encrypted.pack(pady=(10, 0), padx=10, anchor="w")
output_encrypted_message = customtkinter.CTkTextbox(master=scrollable_frame, height=50)
output_encrypted_message.pack(pady=5, padx=10, fill="x")

button_decrypt = customtkinter.CTkButton(master=scrollable_frame, text="Déchiffrer", command=decrypt_message)
button_decrypt.pack(pady=5, padx=10)

label_decrypted = customtkinter.CTkLabel(master=scrollable_frame, text="Message déchiffré :")
label_decrypted.pack(pady=(10, 0), padx=10, anchor="w")
output_decrypted_message = customtkinter.CTkTextbox(master=scrollable_frame, height=50)
output_decrypted_message.pack(pady=5, padx=10, fill="x")

app.mainloop()