import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import zipfile
import tarfile
import threading
import subprocess # Pour exécuter des commandes externes comme rpm2cpio et cpio

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FileArchiverApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestionnaire d'Archives et Paquets (ZIP, TAR.GZ, RPM)")
        self.geometry("750x650") # Taille de fenêtre légèrement augmentée

        # Variables pour les chemins (Compression)
        self.compress_input_path = ctk.StringVar()
        self.compress_output_archive_path = ctk.StringVar()
        self.compress_type_var = ctk.StringVar(value="zip") # Default value

        # Variables pour les chemins (Décompression)
        self.decompress_archive_path = ctk.StringVar()
        self.decompress_output_dir = ctk.StringVar()

        # Variables pour les chemins (Extraction RPM)
        self.rpm_file_path = ctk.StringVar()
        self.rpm_output_directory = ctk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # --- Onglets Compression / Décompression / RPM ---
        self.tabview = ctk.CTkTabview(self, width=730, height=550)
        self.tabview.pack(pady=10, padx=20, fill="both", expand=True)

        self.tabview.add("Compression")
        self.tabview.add("Décompression")
        self.tabview.add("Extraction RPM") # Nouvel onglet pour RPM

        self.tabview.tab("Compression").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Décompression").grid_columnconfigure(1, weight=1)
        self.tabview.tab("Extraction RPM").grid_columnconfigure(1, weight=1)

        # --- Tab "Compression" ---
        comp_frame = self.tabview.tab("Compression")

        ctk.CTkLabel(comp_frame, text="Fichier/Dossier à compresser:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(comp_frame, textvariable=self.compress_input_path, state="readonly").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(comp_frame, text="Parcourir...", command=self.browse_compress_input).grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(comp_frame, text="Nom de l'archive de sortie:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(comp_frame, textvariable=self.compress_output_archive_path).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(comp_frame, text="Enregistrer sous...", command=self.browse_compress_output).grid(row=1, column=2, padx=5, pady=5)

        ctk.CTkLabel(comp_frame, text="Format de compression:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkOptionMenu(comp_frame, variable=self.compress_type_var, values=["zip", "tar.gz"], command=self.update_compress_output_extension).grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.compress_button = ctk.CTkButton(comp_frame, text="Compresser", command=self.start_compression)
        self.compress_button.grid(row=3, column=0, columnspan=3, pady=20)

        # --- Tab "Décompression" ---
        decomp_frame = self.tabview.tab("Décompression")

        ctk.CTkLabel(decomp_frame, text="Fichier archive:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(decomp_frame, textvariable=self.decompress_archive_path, state="readonly").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(decomp_frame, text="Parcourir...", command=self.browse_decompress_archive).grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(decomp_frame, text="Dossier de destination:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(decomp_frame, textvariable=self.decompress_output_dir, state="readonly").grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(decomp_frame, text="Parcourir...", command=self.browse_decompress_output).grid(row=1, column=2, padx=5, pady=5)

        self.decompress_button = ctk.CTkButton(decomp_frame, text="Décompresser", command=self.start_decompression)
        self.decompress_button.grid(row=2, column=0, columnspan=3, pady=20)

        # --- Tab "Extraction RPM" ---
        rpm_frame = self.tabview.tab("Extraction RPM")

        ctk.CTkLabel(rpm_frame, text="Fichier RPM:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(rpm_frame, textvariable=self.rpm_file_path, state="readonly").grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(rpm_frame, text="Parcourir...", command=self.browse_rpm_file).grid(row=0, column=2, padx=5, pady=5)

        ctk.CTkLabel(rpm_frame, text="Dossier d'extraction:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ctk.CTkEntry(rpm_frame, textvariable=self.rpm_output_directory, state="readonly").grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(rpm_frame, text="Parcourir...", command=self.browse_rpm_output_directory).grid(row=1, column=2, padx=5, pady=5)

        self.rpm_extract_button = ctk.CTkButton(rpm_frame, text="Extraire le RPM", command=self.start_rpm_extraction)
        self.rpm_extract_button.grid(row=2, column=0, columnspan=3, pady=20)


        # --- Zone de log globale ---
        self.log_text = ctk.CTkTextbox(self, width=730, height=100, state="disabled")
        self.log_text.pack(pady=10, padx=20, fill="x")

    def log_message(self, message):
        """Ajoute un message à la zone de log."""
        self.log_text.configure(state="normal")
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
        self.update_idletasks() # Force GUI update

    def clear_log(self):
        """Vide la zone de log."""
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", "end")
        self.log_text.configure(state="disabled")


    # --- Fonctions de Compression ---
    def browse_compress_input(self):
        """Permet de sélectionner un fichier ou un dossier à compresser."""
        choice = messagebox.askyesno("Sélection", "Voulez-vous compresser un dossier entier ?\n\nOui: Sélectionner un dossier\nNon: Sélectionner un fichier")
        if choice: # Folder
            path = filedialog.askdirectory(title="Sélectionner le dossier à compresser")
        else: # File
            path = filedialog.askopenfilename(title="Sélectionner le fichier à compresser")

        if path:
            self.compress_input_path.set(path)
            self.update_compress_output_extension() # Mettre à jour l'extension suggérée

    def update_compress_output_extension(self, *args):
        """Met à jour l'extension par défaut de l'archive de sortie en fonction du type de compression choisi."""
        input_path_val = self.compress_input_path.get()
        if input_path_val:
            base_name = os.path.basename(input_path_val)
            current_dir = os.path.dirname(input_path_val) or os.path.expanduser("~")
            
            # Supprimer l'ancienne extension si elle existe pour ne pas empiler
            for ext in [".zip", ".tar.gz", ".tar"]:
                if base_name.lower().endswith(ext):
                    base_name = base_name[:-len(ext)]
                    break

            default_archive_name = os.path.join(current_dir, base_name + "." + self.compress_type_var.get())
            self.compress_output_archive_path.set(default_archive_name)

    def browse_compress_output(self):
        """Permet de définir le nom et l'emplacement de l'archive de sortie."""
        file_type_ext = self.compress_type_var.get()
        file_path = filedialog.asksaveasfilename(
            title="Enregistrer l'archive sous...",
            defaultextension=f".{file_type_ext}",
            filetypes=[(f"{file_type_ext.upper()} files", f"*.{file_type_ext}"), ("All files", "*.*")]
        )
        if file_path:
            self.compress_output_archive_path.set(file_path)

    def start_compression(self):
        """Lance l'opération de compression dans un thread séparé."""
        input_path = self.compress_input_path.get()
        output_archive = self.compress_output_archive_path.get()
        compress_type = self.compress_type_var.get()

        if not input_path:
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier ou un dossier à compresser.")
            return
        if not output_archive:
            messagebox.showerror("Erreur", "Veuillez spécifier le nom de l'archive de sortie.")
            return

        self.clear_log()
        self.log_message(f"Début de la compression de : {input_path}")
        self.log_message(f"Vers : {output_archive}")
        self.log_message(f"Format : {compress_type.upper()}")

        self.compress_button.configure(state="disabled", text="Compression en cours...")
        self.decompress_button.configure(state="disabled")
        self.rpm_extract_button.configure(state="disabled")

        compression_thread = threading.Thread(target=self._compress_files, args=(input_path, output_archive, compress_type))
        compression_thread.start()

    def _compress_files(self, input_path, output_archive, compress_type):
        """Logique de compression réelle."""
        try:
            if compress_type == "zip":
                if os.path.isfile(input_path):
                    with zipfile.ZipFile(output_archive, 'w', zipfile.ZIP_DEFLATED) as zf:
                        zf.write(input_path, os.path.basename(input_path))
                elif os.path.isdir(input_path):
                    with zipfile.ZipFile(output_archive, 'w', zipfile.ZIP_DEFLATED) as zf:
                        for root, _, files in os.walk(input_path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, os.path.dirname(input_path))
                                zf.write(file_path, arcname)
            elif compress_type == "tar.gz":
                if os.path.isfile(input_path):
                    with tarfile.open(output_archive, 'w:gz') as tar:
                        tar.add(input_path, arcname=os.path.basename(input_path))
                elif os.path.isdir(input_path):
                    with tarfile.open(output_archive, 'w:gz') as tar:
                        tar.add(input_path, arcname=os.path.basename(input_path))
            else:
                raise ValueError("Format de compression non supporté.")

            self.log_message("Compression terminée avec succès !")
            messagebox.showinfo("Succès", f"Les fichiers ont été compressés avec succès dans :\n{output_archive}")

        except Exception as e:
            self.log_message(f"Erreur de compression : {e}")
            messagebox.showerror("Erreur de compression", f"Une erreur est survenue pendant la compression : {e}")
        finally:
            self.compress_button.configure(state="normal", text="Compresser")
            self.decompress_button.configure(state="normal")
            self.rpm_extract_button.configure(state="normal")


    # --- Fonctions de Décompression ---
    def browse_decompress_archive(self):
        """Permet de sélectionner un fichier archive à décompresser."""
        file_path = filedialog.askopenfilename(
            title="Sélectionner le fichier archive",
            filetypes=[("Archives supportées", "*.zip *.tar.gz *.tgz *.tar.bz2 *.tbz *.tar.xz *.txz"), ("All files", "*.*")]
        )
        if file_path:
            self.decompress_archive_path.set(file_path)
            # Suggérer un dossier de sortie par défaut
            archive_name = os.path.basename(file_path)
            # Enlève toutes les extensions connues
            for ext in ['.zip', '.tar.gz', '.tgz', '.tar.bz2', '.tbz', '.tar.xz', '.txz', '.tar']:
                if archive_name.lower().endswith(ext):
                    archive_name = archive_name[:-len(ext)]
                    break
            default_output = os.path.join(os.path.dirname(file_path) or os.path.expanduser("~"), f"extracted_{archive_name}")
            self.decompress_output_dir.set(default_output)

    def browse_decompress_output(self):
        """Permet de définir le dossier où l'archive sera décompressée."""
        dir_path = filedialog.askdirectory(
            title="Sélectionner le dossier de destination"
        )
        if dir_path:
            self.decompress_output_dir.set(dir_path)

    def start_decompression(self):
        """Lance l'opération de décompression dans un thread séparé."""
        archive_path = self.decompress_archive_path.get()
        output_dir = self.decompress_output_dir.get()

        if not archive_path:
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier archive à décompresser.")
            return
        if not output_dir:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier de destination.")
            return
        if not os.path.exists(archive_path):
            messagebox.showerror("Erreur", "Le fichier archive spécifié n'existe pas.")
            return

        self.clear_log()
        self.log_message(f"Début de la décompression de : {os.path.basename(archive_path)}")
        self.log_message(f"Vers le dossier : {output_dir}")

        self.decompress_button.configure(state="disabled", text="Décompression en cours...")
        self.compress_button.configure(state="disabled")
        self.rpm_extract_button.configure(state="disabled")

        decompression_thread = threading.Thread(target=self._decompress_archive, args=(archive_path, output_dir))
        decompression_thread.start()

    def _decompress_archive(self, archive_path, output_dir):
        """Logique de décompression réelle."""
        try:
            os.makedirs(output_dir, exist_ok=True) # Crée le dossier de destination si inexistant

            if zipfile.is_zipfile(archive_path):
                with zipfile.ZipFile(archive_path, 'r') as zf:
                    zf.extractall(output_dir)
            elif tarfile.is_tarfile(archive_path):
                with tarfile.open(archive_path, 'r:*') as tar: # 'r:*' auto-détecte le type de compression (gz, bz2, xz)
                    tar.extractall(output_dir)
            else:
                raise ValueError("Format d'archive non reconnu ou corrompu (seuls .zip et .tar.* sont supportés).")

            self.log_message("Décompression terminée avec succès !")
            messagebox.showinfo("Succès", f"L'archive a été décompressée avec succès dans :\n{output_dir}")
            self._open_directory(output_dir)

        except Exception as e:
            self.log_message(f"Erreur de décompression : {e}")
            messagebox.showerror("Erreur de décompression", f"Une erreur est survenue pendant la décompression : {e}")
        finally:
            self.decompress_button.configure(state="normal", text="Décompresser")
            self.compress_button.configure(state="normal")
            self.rpm_extract_button.configure(state="normal")


    # --- Fonctions d'Extraction RPM ---
    def browse_rpm_file(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionner un fichier RPM",
            filetypes=[("RPM packages", "*.rpm")]
        )
        if file_path:
            self.rpm_file_path.set(file_path)
            # Suggérer un dossier de sortie par défaut basé sur le nom du RPM
            rpm_name = os.path.splitext(os.path.basename(file_path))[0]
            default_output = os.path.join(os.path.dirname(file_path) or os.path.expanduser("~"), f"rpm_extracted_{rpm_name}")
            self.rpm_output_directory.set(default_output)

    def browse_rpm_output_directory(self):
        dir_path = filedialog.askdirectory(
            title="Sélectionner le dossier d'extraction pour RPM"
        )
        if dir_path:
            self.rpm_output_directory.set(dir_path)

    def start_rpm_extraction(self):
        rpm_file = self.rpm_file_path.get()
        output_dir = self.rpm_output_directory.get()

        if not rpm_file:
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier RPM.")
            return
        if not output_dir:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier d'extraction.")
            return
        if not os.path.exists(rpm_file):
            messagebox.showerror("Erreur", "Le fichier RPM spécifié n'existe pas.")
            return
        if not rpm_file.lower().endswith(".rpm"):
            messagebox.showerror("Erreur", "Le fichier sélectionné ne semble pas être un fichier RPM.")
            return

        self.clear_log()
        self.log_message(f"Début de l'extraction de : {os.path.basename(rpm_file)}")
        self.log_message(f"Vers le dossier : {output_dir}")

        self.rpm_extract_button.configure(state="disabled", text="Extraction RPM en cours...")
        self.compress_button.configure(state="disabled")
        self.decompress_button.configure(state="disabled")

        extraction_thread = threading.Thread(target=self._extract_rpm, args=(rpm_file, output_dir))
        extraction_thread.start()

    def _extract_rpm(self, rpm_file, output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
            self.log_message(f"Dossier d'extraction créé/vérifié: {output_dir}")

            # Commande complète avec pipe pour plus de simplicité dans Popen
            full_command = f"rpm2cpio \"{rpm_file}\" | cpio -idmv"
            self.log_message(f"Exécution : {full_command}")

            process = subprocess.Popen(full_command, shell=True, cwd=output_dir,
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True, encoding='utf-8') # Use text mode for easier output capture

            # Lire la sortie en temps réel (optionnel, mais utile pour de gros fichiers)
            for line in process.stdout:
                self.log_message(f"Stdout: {line.strip()}")
            
            # Attendre la fin du processus et capturer les erreurs restantes
            stderr_output = process.stderr.read()
            if stderr_output:
                self.log_message(f"Stderr: {stderr_output.strip()}")

            return_code = process.wait() # Attend la fin du processus et récupère le code de retour

            if return_code == 0:
                self.log_message("Extraction RPM terminée avec succès !")
                messagebox.showinfo("Succès", f"Le paquet RPM a été extrait avec succès dans :\n{output_dir}")
                self._open_directory(output_dir)
            else:
                self.log_message(f"Erreur d'extraction RPM. Code de sortie : {return_code}")
                self.log_message("Vérifiez que 'rpm2cpio' et 'cpio' sont installés et dans votre PATH.")
                messagebox.showerror("Erreur d'extraction RPM",
                                     f"L'extraction a échoué. Code de sortie : {return_code}\n"
                                     "Vérifiez les logs pour plus de détails et assurez-vous que 'rpm2cpio' et 'cpio' sont installés.")

        except FileNotFoundError:
            self.log_message("Erreur : 'rpm2cpio' ou 'cpio' introuvable.")
            self.log_message("Veuillez vous assurer que ces outils sont installés sur votre système et dans votre PATH.")
            messagebox.showerror("Outils manquants",
                                 "Les outils 'rpm2cpio' et/ou 'cpio' sont introuvables.\n"
                                 "Veuillez les installer (par exemple : sudo apt install rpm2cpio cpio sur Debian/Ubuntu).")
        except Exception as e:
            self.log_message(f"Une erreur inattendue est survenue lors de l'extraction RPM : {e}")
            messagebox.showerror("Erreur inattendue", f"Une erreur est survenue pendant l'extraction RPM : {e}")
        finally:
            self.rpm_extract_button.configure(state="normal", text="Extraire le RPM")
            self.compress_button.configure(state="normal")
            self.decompress_button.configure(state="normal")

    # --- Fonction utilitaire pour ouvrir un répertoire ---
    def _open_directory(self, path):
        """Ouvre un répertoire dans l'explorateur de fichiers par défaut du système."""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(path)
            elif os.uname().sysname == 'Darwin':  # macOS
                subprocess.run(['open', path])
            else:  # Linux / Unix-like
                subprocess.run(['xdg-open', path])
        except Exception as e:
            self.log_message(f"Impossible d'ouvrir le dossier '{path}' : {e}")

if __name__ == "__main__":
    app = FileArchiverApp()
    app.mainloop()