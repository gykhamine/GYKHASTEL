import customtkinter as ctk
import subprocess
from tkinter import messagebox

def run_firewall_command(action, port, protocol, permanent):
    """Exécute une commande firewalld pour ouvrir ou fermer un port."""
    command = ["sudo", "firewall-cmd"]

    if action == "add":
        command.append(f"--add-port={port}/{protocol}")
    elif action == "remove":
        command.append(f"--remove-port={port}/{protocol}")
    else:
        messagebox.showerror("Erreur", "Action non valide spécifiée.")
        return False

    if permanent:
        command.append("--permanent")

    try:
        # Exécuter la commande firewalld
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Recharger firewalld si le changement est permanent
        if permanent:
            reload_command = ["sudo", "firewall-cmd", "--reload"]
            reload_result = subprocess.run(reload_command, capture_output=True, text=True, check=True)
            messagebox.showinfo("Succès & Rechargement",
                                f"Port {port}/{protocol} {action}ed.\n"
                                f"Message Firewalld: {result.stdout.strip()}\n"
                                f"Firewalld rechargé: {reload_result.stdout.strip()}")
        else:
            messagebox.showinfo("Succès", f"Port {port}/{protocol} {action}ed.\n"
                                          f"Message Firewalld: {result.stdout.strip()}")
        return True

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erreur Firewalld",
                                f"Erreur lors de l'exécution de firewalld pour {action}er le port:\n"
                                f"Commande: {' '.join(e.cmd)}\n"
                                f"Sortie standard: {e.stdout.strip()}\n"
                                f"Erreur standard: {e.stderr.strip()}")
        return False
    except FileNotFoundError:
        messagebox.showerror("Erreur",
                                "La commande 'sudo' ou 'firewall-cmd' n'a pas été trouvée.\n"
                                "Assurez-vous qu'ils sont installés et dans votre PATH.")
        return False
    except Exception as e:
        messagebox.showerror("Erreur Inconnue", f"Une erreur inattendue est survenue : {e}")
        return False

def handle_port_action(action):
    """Gère l'action d'ouverture ou de fermeture du port."""
    port = port_entry.get().strip()
    protocol = protocol_var.get()
    permanent = permanent_var.get()

    if not port.isdigit():
        messagebox.showerror("Erreur", "Le numéro de port doit être un nombre valide.")
        return

    if action == "open":
        run_firewall_command("add", port, protocol, permanent)
    elif action == "close":
        run_firewall_command("remove", port, protocol, permanent)

# --- Configuration de l'interface utilisateur avec customtkinter ---
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.title("Contrôleur de Port Firewalld")
app.geometry("400x380")

# Cadre principal
frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Titre
title_label = ctk.CTkLabel(frame, text="Gérer un Port Firewalld", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=(10, 20))

# Numéro de port
port_label = ctk.CTkLabel(frame, text="Numéro de port:")
port_label.pack(pady=(0, 5))
port_entry = ctk.CTkEntry(frame, width=200, placeholder_text="Ex: 8080")
port_entry.pack(pady=(0, 10))

# Protocole
protocol_label = ctk.CTkLabel(frame, text="Protocole:")
protocol_label.pack(pady=(0, 5))
protocol_var = ctk.StringVar(value="tcp") # Valeur par défaut
protocol_optionmenu = ctk.CTkOptionMenu(frame, values=["tcp", "udp"], variable=protocol_var)
protocol_optionmenu.pack(pady=(0, 10))

# Permanent
permanent_var = ctk.BooleanVar(value=True) # Valeur par défaut: permanent
permanent_checkbox = ctk.CTkCheckBox(frame, text="Rendre permanent (rechargement nécessaire)", variable=permanent_var)
permanent_checkbox.pack(pady=(0, 15))

# Boutons d'action
button_frame = ctk.CTkFrame(frame, fg_color="transparent")
button_frame.pack(pady=10)

open_button = ctk.CTkButton(button_frame, text="Ouvrir le port", command=lambda: handle_port_action("open"))
open_button.pack(side="left", padx=10)

close_button = ctk.CTkButton(button_frame, text="Fermer le port", command=lambda: handle_port_action("close"))
close_button.pack(side="right", padx=10)

# Lancer l'application
app.mainloop()