import customtkinter
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption
from cryptography.hazmat.backends import default_backend

# Configuration de la fenêtre principale
app = customtkinter.CTk()
app.title("Signature Numérique RSA")
app.geometry("800x800")

# Variables pour stocker les clés et la signature
private_key = None
public_key = None
signature = None
message_to_sign = None

# --- Fonctions de Cryptographie ---

def generate_keys():
    """Génère une paire de clés RSA et les affiche."""
    global private_key, public_key
    
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        
        private_pem = private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo
        )

        output_private_key.delete("1.0", "end")
        output_private_key.insert("1.0", private_pem.decode("utf-8"))
        output_public_key.delete("1.0", "end")
        output_public_key.insert("1.0", public_pem.decode("utf-8"))
        
        status_label.configure(text="Paire de clés RSA générée !", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Erreur lors de la génération des clés : {e}", text_color="red")


def sign_message():
    """Signe un message avec la clé privée."""
    global signature, message_to_sign
    
    message_to_sign_str = entry_message.get()
    if not private_key or not message_to_sign_str:
        status_label.configure(text="Veuillez générer des clés et entrer un message.", text_color="red")
        return
        
    message_to_sign = message_to_sign_str.encode("utf-8")
    
    try:
        # 1. Création de la signature avec la clé privée
        signature = private_key.sign(
            message_to_sign,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        output_signature.delete("1.0", "end")
        output_signature.insert("1.0", signature.hex())
        status_label.configure(text="Message signé !", text_color="green")
    except Exception as e:
        status_label.configure(text=f"Erreur lors de la signature : {e}", text_color="red")
        
        
def verify_signature():
    """Vérifie une signature avec la clé publique."""
    global signature, message_to_sign
    
    if not public_key or not signature or not message_to_sign:
        status_label.configure(text="Veuillez d'abord signer un message.", text_color="red")
        return

    try:
        # 2. Vérification de la signature avec la clé publique
        public_key.verify(
            signature,
            message_to_sign,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        verify_label.configure(text="✅ Signature vérifiée et valide !", text_color="green")
    except Exception as e:
        verify_label.configure(text="❌ Signature invalide !", text_color="red")
        print(e)
        
# --- Widgets de l'interface graphique ---

scrollable_frame = customtkinter.CTkScrollableFrame(master=app)
scrollable_frame.pack(pady=20, padx=60, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=scrollable_frame, text="Signature Numérique RSA", font=("Roboto", 24))
label_title.pack(pady=12, padx=10)

button_generate_keys = customtkinter.CTkButton(master=scrollable_frame, text="Générer les clés RSA", command=generate_keys)
button_generate_keys.pack(pady=(20, 10), padx=10)

status_label = customtkinter.CTkLabel(master=scrollable_frame, text="", text_color="green")
status_label.pack(pady=5, padx=10)

label_public_key = customtkinter.CTkLabel(master=scrollable_frame, text="Clé Publique (pour vérifier) :")
label_public_key.pack(pady=(10, 0), padx=10, anchor="w")
output_public_key = customtkinter.CTkTextbox(master=scrollable_frame, height=80)
output_public_key.pack(pady=5, padx=10, fill="x")

label_private_key = customtkinter.CTkLabel(master=scrollable_frame, text="Clé Privée (pour signer) :")
label_private_key.pack(pady=(10, 0), padx=10, anchor="w")
output_private_key = customtkinter.CTkTextbox(master=scrollable_frame, height=80)
output_private_key.pack(pady=5, padx=10, fill="x")

label_message = customtkinter.CTkLabel(master=scrollable_frame, text="Message à signer :")
label_message.pack(pady=(20, 0), padx=10, anchor="w")
entry_message = customtkinter.CTkEntry(master=scrollable_frame, placeholder_text="Entrez votre message ici...", width=500)
entry_message.pack(pady=5, padx=10, fill="x")

button_sign = customtkinter.CTkButton(master=scrollable_frame, text="Signer le message", command=sign_message)
button_sign.pack(pady=5, padx=10)

label_signature = customtkinter.CTkLabel(master=scrollable_frame, text="Signature :")
label_signature.pack(pady=(10, 0), padx=10, anchor="w")
output_signature = customtkinter.CTkTextbox(master=scrollable_frame, height=50)
output_signature.pack(pady=5, padx=10, fill="x")

button_verify = customtkinter.CTkButton(master=scrollable_frame, text="Vérifier la signature", command=verify_signature)
button_verify.pack(pady=5, padx=10)

verify_label = customtkinter.CTkLabel(master=scrollable_frame, text="", font=("Roboto", 16))
verify_label.pack(pady=(10, 20), padx=10)

app.mainloop()