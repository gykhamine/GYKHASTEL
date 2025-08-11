import subprocess
import sys

def download_source_packages_from_file(file_path):
    """
    Lit les noms de paquets à partir d'un fichier et télécharge leurs sources.
    :param file_path: Le chemin vers le fichier texte contenant la liste des paquets.
    """
    package_names = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                # Dnf list inclut souvent des lignes d'en-tête et des informations de version.
                # On ne prend que le nom du paquet qui est le premier mot de chaque ligne.
                if line.strip() and not line.startswith("Last metadata"):
                    package_name = line.split()[0]
                    # Parfois le nom du paquet est suivi d'un suffixe d'architecture (ex: .x86_64)
                    # On le supprime pour avoir le nom de base
                    if '.' in package_name and not package_name.startswith('.'):
                        package_name = package_name.split('.')[0]
                        
                    package_names.append(package_name)

    except FileNotFoundError:
        print(f"Erreur: Le fichier '{file_path}' n'a pas été trouvé.")
        return

    if not package_names:
        print("Erreur: Le fichier ne contient aucun nom de paquet valide.")
        return

    print(f"Début du téléchargement des sources pour {len(package_names)} paquets...")

    # On exécute la commande DNF en une seule fois pour tous les paquets pour plus d'efficacité
    command = ["dnf", "download", "--source"] + package_names
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        for line in process.stdout:
            print(line, end='')
        
        process.wait()
        
        if process.returncode == 0:
            print("\n✔️ Tous les paquets sources ont été téléchargés avec succès.")
        else:
            print(f"\n❌ Erreur: Le téléchargement a échoué avec le code de sortie {process.returncode}.")
            
    except FileNotFoundError:
        print("Erreur: La commande 'dnf' n'a pas été trouvée. Assurez-vous qu'elle est installée et dans le PATH.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue: {e}")

if __name__ == "__main__":
    # Remplacez "dnf_list_complet.txt" par le nom de votre fichier
    file_with_packages = "dnf_list_complet.txt"
    
    download_source_packages_from_file(file_with_packages)