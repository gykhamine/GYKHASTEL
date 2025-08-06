import customtkinter as ctk

class GrubConfigApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime de GRUB2 sur Fedora")
        self.geometry("950x750")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        # --- Création du système d'onglets ---
        self.tab_view = ctk.CTkTabview(self, width=900, height=700)
        self.tab_view.pack(padx=20, pady=20, fill="both", expand=True)

        # Création des onglets
        self.tab_view.add("Introduction & Fichiers")
        self.tab_view.add("Commandes (CLI)")
        self.tab_view.add("Variables de Configuration")
        self.tab_view.add("Prise en main de 'grub rescue'")
        self.tab_view.add("Personnalisation")
        self.tab_view.add("Dépannage avancé")
        
        # Initialisation du contenu pour chaque onglet
        self.create_intro_tab()
        self.create_commands_tab()
        self.create_variables_tab()
        self.create_rescue_tab()
        self.create_customization_tab()
        self.create_advanced_troubleshooting_tab()

    def create_text_box(self, parent_tab, content):
        """Crée et configure une boîte de texte pour un onglet."""
        text_box = ctk.CTkTextbox(parent_tab, wrap="word", font=("Arial", 14), activate_scrollbars=True)
        text_box.pack(fill="both", expand=True, padx=10, pady=10)
        text_box.insert("0.0", content)
        text_box.configure(state="disabled")

    def create_intro_tab(self):
        content = (
            "**Introduction à GRUB2 sur Fedora** 🐧\n"
            "Fedora utilise GRUB2 avec le **Boot Loader Specification (BLS)**. Les entrées de démarrage sont gérées via des fichiers `.conf` séparés, simplifiant la maintenance. Les modifications se font principalement via l'outil `grubby`.\n\n"
            "**Fichiers et Répertoires clés :**\n"
            "1.  **`/etc/default/grub`** : Fichier principal pour les paramètres globaux (timeout, défaut).\n"
            "2.  **`/etc/grub.d/`** : Contient les scripts générant `grub.cfg`. Moins pertinent avec BLS, mais important pour les personnalisations avancées.\n"
            "3.  **`/boot/grub2/grub.cfg`** : Le fichier final, généré. Ne pas le modifier directement.\n"
            "4.  **`/boot/loader/entries/*.conf`** : Le cœur du BLS. Chaque fichier `.conf` est une entrée de menu pour un noyau, contenant `title`, `linux`, `initrd` et `options`."
        )
        self.create_text_box(self.tab_view.tab("Introduction & Fichiers"), content)

    def create_commands_tab(self):
        content = (
            "**Commandes de gestion de GRUB2 et des noyaux** 🛠️\n"
            "**Commandes générales de GRUB :**\n"
            "1.  **`sudo grub2-mkconfig -o /boot/grub2/grub.cfg`** : Génère le fichier de configuration final.\n"
            "2.  **`grub2-mkconfig`** : Affiche la configuration générée dans la console.\n"
            "3.  **`sudo grub2-install /dev/sdX`** : Réinstalle GRUB2 sur un disque (MBR/GPT).\n"
            "4.  **`sudo grubby --info=ALL`** : Affiche toutes les entrées de démarrage.\n"
            "5.  **`sudo grubby --info /boot/vmlinuz-$(uname -r)`** : Affiche les détails du noyau actuel.\n\n"
            "**Commandes de l'outil `grubby` (pour le BLS) :**\n"
            "1.  **`sudo grubby --default-kernel`** : Affiche le noyau par défaut.\n"
            "2.  **`sudo grubby --set-default=/boot/vmlinuz-...`** : Définit un noyau spécifique comme par défaut.\n"
            "3.  **`sudo grubby --update-kernel=ALL --args=\"nomodeset\"`** : Ajoute un argument de noyau à toutes les entrées.\n"
            "4.  **`sudo grubby --remove-args=\"rhgb quiet\" --update-kernel=/boot/vmlinuz-$(uname -r)`** : Supprime des arguments pour le noyau actuel.\n"
            "5.  **`sudo grubby --remove-kernel=/boot/vmlinuz-old_kernel...`** : Supprime une entrée de noyau.\n"
            "6.  **`grubby --set-root=/dev/sdX`** : Définit la partition racine.\n"
            "7.  **`grubby --initrd /chemin/vers/initrd`** : Modifie le chemin de l'initrd.\n"
            "8.  **`grubby --add-kernel=/chemin/vers/vmlinuz`** : Ajoute une nouvelle entrée de noyau."
        )
        self.create_text_box(self.tab_view.tab("Commandes (CLI)"), content)

    def create_variables_tab(self):
        content = (
            "**Variables de `/etc/default/grub` et arguments du noyau** ⚙️\n"
            "Ce fichier est le point de départ de la configuration de GRUB2. Les variables sont lues par `grub2-mkconfig` pour générer le `grub.cfg` final.\n\n"
            "**Variables de comportement :**\n"
            "1.  **`GRUB_TIMEOUT=5`** : Nombre de secondes pour afficher le menu. `-1` pour l'afficher indéfiniment.\n"
            "2.  **`GRUB_TIMEOUT_STYLE=menu`** : Style de l'affichage. `hidden` pour ne pas afficher le menu (sauf si on appuie sur une touche).\n"
            "3.  **`GRUB_DEFAULT=saved`** : Indique de démarrer sur la dernière entrée choisie. Nécessite `GRUB_SAVEDEFAULT=true`.\n"
            "4.  **`GRUB_SAVEDEFAULT=true`** : Enregistre l'entrée de démarrage actuelle comme défaut pour la prochaine fois.\n"
            "5.  **`GRUB_CMDLINE_LINUX=\"...\"`** : Arguments de démarrage passés au noyau (ex: `rhgb quiet`). Ces arguments sont ajoutés à toutes les entrées de noyau via les fichiers BLS.\n"
            "6.  **`GRUB_DISABLE_OS_PROBER=false`** : Active ou désactive la détection d'autres systèmes d'exploitation.\n\n"
            "**Variables d'apparence :**\n"
            "1.  **`GRUB_TERMINAL_OUTPUT=\"console\"`** : Force la sortie console. `vga_text` pour un terminal texte de base.\n"
            "2.  **`GRUB_GFXMODE=1920x1080x32,1024x768,800x600`** : Résolution du menu. GRUB utilise la première résolution prise en charge.\n"
            "3.  **`GRUB_GFXPAYLOAD_LINUX=keep`** : Garde la résolution choisie par GRUB pour le noyau Linux. Sinon, le noyau peut passer à une autre résolution.\n"
            "4.  **`GRUB_THEME=\"/chemin/vers/theme.txt\"`** : Spécifie le chemin d'un thème graphique pour GRUB2.\n"
            "5.  **`GRUB_BACKGROUND=\"/chemin/vers/image.png\"`** : Définit un fond d'écran pour le menu.\n\n"
            "**Variables de menu :**\n"
            "1.  **`GRUB_MENU_TITLE=\"Mon super système d'exploitation\"`** : Personnalise le titre du menu de démarrage.\n"
            "2.  **`GRUB_DISABLE_RECOVERY=\"true\"`** : Masque les entrées de récupération du noyau dans le menu.\n"
            "3.  **`GRUB_DISABLE_SUBMENU=y`** : Affiche les entrées de récupération directement au lieu de les cacher dans un sous-menu.\n\n"
            "**Arguments de noyau importants :**\n"
            "1.  **`rhgb quiet`** : `rhgb` pour l'écran de démarrage graphique, `quiet` pour masquer les messages.\n"
            "2.  **`nomodeset`** : Désactive le Kernel Mode Setting. Essentiel pour les problèmes graphiques au démarrage.\n"
            "3.  **`acpi=off`** : Désactive l'ACPI, utile pour les problèmes de gestion d'énergie.\n"
            "4.  **`rd.break`** : Lance un shell d'urgence avant le montage de la partition racine.\n"
            "5.  **`single` ou `1`** : Démarre en mode mono-utilisateur pour la maintenance."
        )
        self.create_text_box(self.tab_view.tab("Variables de Configuration"), content)

    def create_rescue_tab(self):
        content = (
            "**Prise en main du mode 'grub rescue'** 🆘\n"
            "Ce mode s'active lorsque GRUB ne parvient pas à trouver ses fichiers de configuration. L'environnement est très limité, mais il permet un dépannage manuel.\n\n"
            "**Les commandes disponibles (très peu) :** `ls`, `set`, `unset`, `insmod`, `linux`, `initrd`, `normal`, `boot`.\n\n"
            "**Procédure de dépannage pas à pas :**\n"
            "1.  **Identifier les partitions :** Utilisez la commande **`ls`** pour lister tous les disques et partitions disponibles. Vous obtiendrez une liste comme `(hd0)`, `(hd0,msdos1)`, `(hd1,gpt2)`, etc.\n\n"
            "2.  **Trouver la partition racine :** Parcourez les partitions pour trouver celle qui contient votre système Linux. Vous pouvez utiliser `ls (hdX,Y)/` pour voir le contenu de chaque partition. Cherchez le répertoire `/boot` et le fichier `vmlinuz-`.\n\n"
            "3.  **Définir les variables d'environnement :** Une fois que vous avez trouvé la bonne partition (ex: `(hd0,gpt2)`), définissez les variables `root` et `prefix`.\n"
            "    - `grub rescue> set root=(hd0,gpt2)`\n"
            "    - `grub rescue> set prefix=(hd0,gpt2)/boot/grub`\n\n"
            "4.  **Charger les modules nécessaires :** Le mode rescue ne charge pas les modules par défaut. Vous devez charger le module `normal` pour accéder au menu GRUB complet.\n"
            "    - `grub rescue> insmod normal`\n\n"
            "5.  **Lancer le mode normal :** Cette commande va charger le `grub.cfg` de la partition que vous avez définie et afficher le menu GRUB.\n"
            "    - `grub rescue> normal`\n\n"
            "6.  **Si `normal` ne fonctionne pas :** Chargez manuellement le noyau et le fichier `initrd`. Trouvez les noms exacts en utilisant `ls (hd0,gpt2)/boot/`.\n"
            "    - `grub rescue> linux /boot/vmlinuz-5.18.10-200.fc36.x86_64 root=/dev/sda2 ro`\n"
            "    - `grub rescue> initrd /boot/initramfs-5.18.10-200.fc36.x86_64.img`\n"
            "    - `grub rescue> boot`\n\n"
            "7.  **Une fois démarré, réparer GRUB :** Après avoir accédé à votre système, ouvrez un terminal et exécutez ces commandes pour réparer définitivement l'installation :\n"
            "    - `sudo grub2-install /dev/sdX`\n"
            "    - `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`"
        )
        self.create_text_box(self.tab_view.tab("Prise en main de 'grub rescue'"), content)

    def create_customization_tab(self):
        content = (
            "**Personnalisation de l'apparence et des entrées** 🎨\n"
            "**Thèmes et Apparence :**\n"
            "1.  **Thèmes GRUB** : Un thème est un répertoire contenant un fichier `theme.txt`. Il faut définir `GRUB_THEME=\"/chemin/vers/votre/theme/theme.txt\"`.\n"
            "2.  **Couleurs** : Utilisez des variables comme `GRUB_COLOR_NORMAL` et `GRUB_COLOR_HIGHLIGHT` dans `/etc/default/grub`.\n\n"
            "**Gestion des entrées :**\n"
            "1.  **Fichier `40_custom`** : Créez un script pour ajouter des entrées de menu pour des OS non détectés ou des options avancées.\n"
            "2.  **Fichiers BLS (`/boot/loader/entries/`)** : Pour modifier une entrée, il est plus sûr d'utiliser `grubby` que d'éditer manuellement ces fichiers. Par exemple, pour renommer une entrée, vous pouvez modifier le `title` via `grubby`.\n"
            "3.  **Dual-Boot** : Assurez-vous que le script `30_os-prober` est exécutable et que `GRUB_DISABLE_OS_PROBER=false` est défini pour détecter d'autres OS."
        )
        self.create_text_box(self.tab_view.tab("Personnalisation"), content)

    def create_advanced_troubleshooting_tab(self):
        content = (
            "**Dépannage avancé de GRUB2** 🆘\n"
            "**Réparation de GRUB après un écrasement (ex: Windows) :**\n"
            "1.  Démarrez sur une clé USB Fedora en mode **live**.\n"
            "2.  Montez les partitions : `sudo mount /dev/sdX# /mnt` et `sudo mount /dev/sdY# /mnt/boot`.\n"
            "3.  Entrez dans le chroot : `sudo chroot /mnt`.\n"
            "4.  Réinstallez GRUB2 : `sudo grub2-install /dev/sdX` (remplacez `sdX` par votre disque).\n"
            "5.  Générez `grub.cfg` : `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`.\n\n"
            "**Cas spécifique UEFI :**\n"
            "Si votre système utilise l'UEFI, la commande peut être différente et doit cibler la partition ESP (`/boot/efi`).\n"
            "`sudo grub2-install --target=x86_64-efi --efi-directory=/boot/efi`\n\n"
            "**Points de contrôle importants :**\n"
            "- Vérifiez que le drapeau `boot` est bien activé sur la partition de démarrage.\n"
            "- Assurez-vous que le disque de démarrage est bien le premier dans l'ordre de démarrage du BIOS/UEFI.\n"
            "- Utilisez `efibootmgr` (sur les systèmes UEFI) pour vérifier et modifier l'ordre de démarrage."
        )
        self.create_text_box(self.tab_view.tab("Dépannage avancé"), content)


if __name__ == "__main__":
    app = GrubConfigApp()
    app.mainloop()