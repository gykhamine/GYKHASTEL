import customtkinter
import tkinter.filedialog as filedialog
import os

# --- Variables globales et configuration ---
app = customtkinter.CTk()
app.title("Représentation Binaire de Fichiers")
app.geometry("800x600")

def select_file_and_display_binary():
    """Ouvre une boîte de dialogue pour sélectionner un fichier et affiche sa représentation binaire."""
    filepath = filedialog.askopenfilename(
        title="Sélectionnez un fichier",
        filetypes=[("Tous les fichiers", "*.*")]
    )
    if not filepath:
        return

    try:
        entry_file_path.delete(0, "end")
        entry_file_path.insert(0, filepath)
        
        with open(filepath, 'rb') as f:
            content = f.read()

        max_size = 10 * 1024 * 1024  # 10 Mo
        if len(content) > max_size:
            status_label.configure(text=f"Le fichier est trop volumineux ({len(content) / (1024*1024):.2f} Mo). Limite : 10 Mo", text_color="red")
            return
            
        # Créer une liste de chaînes binaires avec numérotation
        binary_lines = []
        for i, byte in enumerate(content):
            # i+1 pour une numérotation qui commence à 1
            line = f"{i+1:04d}: {format(byte, '08b')}"
            binary_lines.append(line)
        
        binary_representation = "\n".join(binary_lines)

        output_text.delete("1.0", "end")
        output_text.insert("1.0", binary_representation.strip())

        status_label.configure(text=f"Fichier chargé : '{os.path.basename(filepath)}'", text_color="green")
        
    except Exception as e:
        status_label.configure(text=f"Erreur lors de la lecture du fichier : {e}", text_color="red")

# --- Widgets de l'interface graphique ---
scrollable_frame = customtkinter.CTkScrollableFrame(master=app)
scrollable_frame.pack(pady=20, padx=60, fill="both", expand=True)

label_title = customtkinter.CTkLabel(master=scrollable_frame, text="Représentation Binaire de Fichiers", font=("Roboto", 24))
label_title.pack(pady=12, padx=10)

button_select_file = customtkinter.CTkButton(master=scrollable_frame, text="Sélectionner un fichier", command=select_file_and_display_binary)
button_select_file.pack(pady=(20, 10), padx=10)

status_label = customtkinter.CTkLabel(master=scrollable_frame, text="Aucun fichier sélectionné.", text_color="blue")
status_label.pack(pady=5, padx=10)

entry_file_path = customtkinter.CTkEntry(master=scrollable_frame, placeholder_text="Chemin du fichier sélectionné...", width=500)
entry_file_path.pack(pady=5, padx=10, fill="x")

label_binary = customtkinter.CTkLabel(master=scrollable_frame, text="Contenu binaire : (numérotation et un octet par ligne)")
label_binary.pack(pady=(20, 0), padx=10, anchor="w")

output_text = customtkinter.CTkTextbox(master=scrollable_frame, width=500, height=300)
output_text.pack(pady=5, padx=10, fill="both", expand=True)

app.mainloop()