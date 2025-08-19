import customtkinter
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

# Configuration de la fenêtre principale
app = customtkinter.CTk()
app.title("AES-256 Cryptographie avec CTk")
app.geometry("700x500")

# Variables pour stocker la clé, le nonce et le tag
key = None
nonce = None
ciphertext = None
tag = None

def encrypt_message():
    """Chiffre le message de l'entrée et affiche le résultat."""
    global key, nonce, ciphertext, tag

    # Récupère le message de l'entrée
    message_str = entry_message.get()
    if not message_str:
        output_label.configure(text="Veuillez entrer un message à chiffrer.", text_color="red")
        return
    message_bytes = message_str.encode("utf-8")

    # 1. Génère une nouvelle clé AES-256 et un nonce GCM
    key = urandom(32)
    nonce = urandom(12)

    # 2. Chiffrement
    try:
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message_bytes) + encryptor.finalize()
        tag = encryptor.tag

        # Affiche les résultats dans la zone de texte
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "--- Message Chiffré ---\n")
        output_text.insert("end", f"Texte chiffré (hex) : {ciphertext.hex()}\n")
        output_text.insert("end", f"Tag (hex) : {tag.hex()}\n")
        output_text.insert("end", f"Nonce (hex) : {nonce.hex()}\n")
        output_label.configure(text="Chiffrement réussi !", text_color="green")
    except Exception as e:
        output_label.configure(text=f"Erreur de chiffrement : {e}", text_color="red")
        
def decrypt_message():
    """Déchiffre les données en utilisant la clé, le nonce et le tag stockés."""
    global key, nonce, ciphertext, tag

    if key is None or nonce is None or ciphertext is None or tag is None:
        output_label.configure(text="Veuillez d'abord chiffrer un message.", text_color="red")
        return

    # 3. Déchiffrement
    try:
        cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_message_bytes = decryptor.update(ciphertext) + decryptor.finalize_with_tag(tag)
        
        # Affiche le message déchiffré
        decrypted_text.delete("1.0", "end")
        decrypted_text.insert("1.0", "--- Message Déchiffré ---\n")
        decrypted_text.insert("end", decrypted_message_bytes.decode("utf-8"))
        output_label.configure(text="Déchiffrement réussi !", text_color="green")
    except Exception as e:
        output_label.configure(text=f"Échec du déchiffrement : {e}", text_color="red")
        decrypted_text.delete("1.0", "end")
        decrypted_text.insert("1.0", "Erreur : le message a peut-être été altéré.")

# Création des widgets
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=frame, text="AES-256 Cryptographie", font=("Roboto", 24))
label_title.pack(pady=12, padx=10)

label_message = customtkinter.CTkLabel(master=frame, text="Message à chiffrer :")
label_message.pack(pady=(20, 0), padx=10, anchor="w")

entry_message = customtkinter.CTkEntry(master=frame, placeholder_text="Entrez votre texte ici...", width=500)
entry_message.pack(pady=(0, 10), padx=10, fill="x")

button_encrypt = customtkinter.CTkButton(master=frame, text="Chiffrer", command=encrypt_message)
button_encrypt.pack(pady=10, padx=10)

output_label = customtkinter.CTkLabel(master=frame, text="", text_color="green")
output_label.pack(pady=(10, 0), padx=10)

output_text = customtkinter.CTkTextbox(master=frame, width=500, height=100)
output_text.pack(pady=10, padx=10, fill="x")

button_decrypt = customtkinter.CTkButton(master=frame, text="Déchiffrer", command=decrypt_message)
button_decrypt.pack(pady=10, padx=10)

decrypted_text = customtkinter.CTkTextbox(master=frame, width=500, height=50)
decrypted_text.pack(pady=(0, 20), padx=10, fill="x")

app.mainloop()