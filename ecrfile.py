import customtkinter
import tkinter.filedialog as filedialog
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# --- Variables globales et configuration ---
app = customtkinter.CTk()
app.title("Chiffrement de Fichiers AES-256")
app.geometry("700x600")

def generate_aes_key():
    """Génère une clé AES-256 aléatoire et l'insère dans le champ de saisie."""
    aes_key = os.urandom(32) # 32 octets = 256 bits
    entry_key.delete(0, "end")
    entry_key.insert(0, aes_key.hex())
    status_label.configure(text="Clé AES-256 générée !", text_color="green")

def select_input_file():
    """Ouvre une boîte de dialogue pour sélectionner un fichier à chiffrer."""
    filepath = filedialog.askopenfilename(title="Sélectionnez le fichier à chiffrer")
    if filepath:
        entry_input_file.delete(0, "end")
        entry_input_file.insert(0, filepath)
        status_label.configure(text=f"Fichier sélectionné : {os.path.basename(filepath)}", text_color="blue")

def select_encrypted_file():
    """Ouvre une boîte de dialogue pour sélectionner un fichier à déchiffrer."""
    filepath = filedialog.askopenfilename(title="Sélectionnez le fichier à déchiffrer")
    if filepath:
        entry_encrypted_file.delete(0, "end")
        entry_encrypted_file.insert(0, filepath)
        status_label.configure(text=f"Fichier sélectionné : {os.path.basename(filepath)}", text_color="blue")

def encrypt_file():
    """Chiffre un fichier avec la clé AES fournie."""
    aes_key_hex = entry_key.get()
    if not aes_key_hex:
        status_label.configure(text="Erreur : Veuillez entrer ou générer une clé AES.", text_color="red")
        return
    
    try:
        aes_key = bytes.fromhex(aes_key_hex)
        if len(aes_key) != 32:
            status_label.configure(text="Erreur : La clé doit être de 32 octets (256 bits).", text_color="red")
            return
    except ValueError:
        status_label.configure(text="Erreur : Format de la clé invalide (utilisez du hexadécimal).", text_color="red")
        return

    input_filepath = entry_input_file.get()
    if not os.path.exists(input_filepath):
        status_label.configure(text="Erreur : Fichier d'entrée introuvable.", text_color="red")
        return

    output_filepath = filedialog.asksaveasfilename(
        title="Enregistrer le fichier chiffré sous...",
        defaultextension=".enc",
        filetypes=[("Fichier chiffré", "*.enc"), ("Tous les fichiers", "*.*")]
    )
    if not output_filepath:
        return
    
    try:
        nonce = os.urandom(12)
        cipher = Cipher(algorithms.AES(aes_key), modes.GCM(nonce), backend=default_backend())
        encryptor = cipher.encryptor()
        
        with open(input_filepath, 'rb') as f_in:
            plaintext = f_in.read()
            ciphertext = encryptor.update(plaintext) + encryptor.finalize()
            tag = encryptor.tag
        
        with open(output_filepath, 'wb') as f_out:
            f_out.write(nonce)
            f_out.write(tag)
            f_out.write(ciphertext)
            
        status_label.configure(text=f"✅ Fichier chiffré avec succès ! -> {os.path.basename(output_filepath)}", text_color="green")
    except Exception as e:
        status_label.configure(text=f"❌ Erreur de chiffrement : {e}", text_color="red")

def decrypt_file():
    """Déchiffre un fichier avec la clé AES fournie."""
    aes_key_hex = entry_key.get()
    if not aes_key_hex:
        status_label.configure(text="Erreur : Veuillez entrer ou générer une clé AES.", text_color="red")
        return
    
    try:
        aes_key = bytes.fromhex(aes_key_hex)
        if len(aes_key) != 32:
            status_label.configure(text="Erreur : La clé doit être de 32 octets (256 bits).", text_color="red")
            return
    except ValueError:
        status_label.configure(text="Erreur : Format de la clé invalide (utilisez du hexadécimal).", text_color="red")
        return

    input_filepath = entry_encrypted_file.get()
    if not os.path.exists(input_filepath):
        status_label.configure(text="Erreur : Fichier d'entrée introuvable.", text_color="red")
        return
        
    output_filepath = filedialog.asksaveasfilename(
        title="Enregistrer le fichier déchiffré sous...",
        defaultextension=".txt",
        filetypes=[("Fichier texte", "*.txt"), ("Tous les fichiers", "*.*")]
    )
    if not output_filepath:
        return
        
    try:
        with open(input_filepath, 'rb') as f_in:
            nonce = f_in.read(12)
            tag = f_in.read(16)
            ciphertext = f_in.read()
        
        cipher = Cipher(algorithms.AES(aes_key), modes.GCM(nonce), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize_with_tag(tag)
        
        with open(output_filepath, 'wb') as f_out:
            f_out.write(plaintext)
            
        status_label.configure(text=f"✅ Fichier déchiffré avec succès ! -> {os.path.basename(output_filepath)}", text_color="green")
    except Exception as e:
        status_label.configure(text=f"❌ Échec du déchiffrement : {e}", text_color="red")

# --- Widgets de l'interface graphique ---
scrollable_frame = customtkinter.CTkScrollableFrame(master=app)
scrollable_frame.pack(pady=20, padx=60, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=scrollable_frame, text="Chiffrement de Fichiers AES-256", font=("Roboto", 24))
label_title.pack(pady=12, padx=10)

label_key = customtkinter.CTkLabel(master=scrollable_frame, text="Clé AES (32 octets en hexadécimal) :")
label_key.pack(pady=(20, 0), padx=10, anchor="w")
frame_key = customtkinter.CTkFrame(master=scrollable_frame)
frame_key.pack(pady=5, padx=10, fill="x")
entry_key = customtkinter.CTkEntry(master=frame_key, placeholder_text="Entrez ou générez votre clé...", width=500)
entry_key.pack(side="left", fill="x", expand=True)
button_generate_key = customtkinter.CTkButton(master=frame_key, text="Générer", command=generate_aes_key)
button_generate_key.pack(side="right", padx=(5, 0))

status_label = customtkinter.CTkLabel(master=scrollable_frame, text="", text_color="blue")
status_label.pack(pady=10, padx=10)

label_input_file = customtkinter.CTkLabel(master=scrollable_frame, text="Fichier à chiffrer :")
label_input_file.pack(pady=(20, 0), padx=10, anchor="w")
frame_input = customtkinter.CTkFrame(master=scrollable_frame)
frame_input.pack(pady=5, padx=10, fill="x")
entry_input_file = customtkinter.CTkEntry(master=frame_input, placeholder_text="Chemin du fichier d'entrée...", width=500)
entry_input_file.pack(side="left", fill="x", expand=True)
button_select_input = customtkinter.CTkButton(master=frame_input, text="Parcourir", command=select_input_file)
button_select_input.pack(side="right", padx=(5, 0))

button_encrypt = customtkinter.CTkButton(master=scrollable_frame, text="Chiffrer le Fichier", command=encrypt_file)
button_encrypt.pack(pady=10, padx=10)

label_encrypted_file = customtkinter.CTkLabel(master=scrollable_frame, text="Fichier à déchiffrer :")
label_encrypted_file.pack(pady=(20, 0), padx=10, anchor="w")
frame_decrypt = customtkinter.CTkFrame(master=scrollable_frame)
frame_decrypt.pack(pady=5, padx=10, fill="x")
entry_encrypted_file = customtkinter.CTkEntry(master=frame_decrypt, placeholder_text="Chemin du fichier chiffré...", width=500)
entry_encrypted_file.pack(side="left", fill="x", expand=True)
button_select_encrypted = customtkinter.CTkButton(master=frame_decrypt, text="Parcourir", command=select_encrypted_file)
button_select_encrypted.pack(side="right", padx=(5, 0))

button_decrypt = customtkinter.CTkButton(master=scrollable_frame, text="Déchiffrer le Fichier", command=decrypt_file)
button_decrypt.pack(pady=10, padx=10)

app.mainloop()