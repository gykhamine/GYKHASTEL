import customtkinter as ctk

class GrubApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime : GRUB2 et le mode Rescue")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        # --- Création du cadre de navigation latéral ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # --- Création des boutons de navigation ---
        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Introduction et Concepts",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_intro)
        self.home_button.pack(fill="x", padx=10, pady=5)
        
        self.files_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Configuration et Fichiers",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_config_files)
        self.files_button.pack(fill="x", padx=10, pady=5)
        
        self.errors_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Messages d'Erreur",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_error_messages)
        self.errors_button.pack(fill="x", padx=10, pady=5)

        self.commands_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Mode Rescue : Commandes",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_commands)
        self.commands_button.pack(fill="x", padx=10, pady=5)

        self.manual_boot_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Démarrage Manuel",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_manual_boot)
        self.manual_boot_button.pack(fill="x", padx=10, pady=5)

        self.repair_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Réparation Définitive",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.show_repair)
        self.repair_button.pack(fill="x", padx=10, pady=5)
        
        self.architecture_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Architecture x86 vs x64",
                                                 fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 anchor="w", command=self.show_architecture)
        self.architecture_button.pack(fill="x", padx=10, pady=5)
        
        self.disks_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Types de disques et partitions",
                                                 fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 anchor="w", command=self.show_disks)
        self.disks_button.pack(fill="x", padx=10, pady=5)
        
        self.troubleshooting_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Scénarios de Dépannage",
                                                 fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 anchor="w", command=self.show_troubleshooting)
        self.troubleshooting_button.pack(fill="x", padx=10, pady=5)
        
        self.faq_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="FAQ et Notions Avancées",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_faq)
        self.faq_button.pack(fill="x", padx=10, pady=5)

        # --- Création du cadre principal pour le contenu ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")

        # --- Démarrage sur le premier onglet ---
        self.show_intro()
        
    def set_content(self, title, text):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        self.content_textbox.configure(state="disabled")

    def show_intro(self):
        content = (
            "**Introduction à GRUB2 et au mode `grub rescue`** 🚀\n\n"
            "GRUB2 (GRand Unified Bootloader version 2) est le programme de gestion de démarrage standard sur la plupart des distributions Linux. Son rôle est de prendre le contrôle dès l'allumage de l'ordinateur, d'afficher un menu, et de charger le noyau du système d'exploitation que vous choisissez.\n\n"
            "Le **mode `grub rescue`** est un environnement de secours qui se déclenche lorsque GRUB2 ne parvient pas à trouver ses fichiers de configuration essentiels. Cela peut arriver si une partition est supprimée, si une mise à jour a échoué, ou si un autre OS a écrasé l'amorce de démarrage. Cet environnement est très limité, mais il contient les outils de base pour identifier les partitions et démarrer manuellement votre système."
            "\n\n**Concepts Clés :**\n"
            "- **MBR (Master Boot Record)** : Un secteur de démarrage sur les anciens disques (BIOS). GRUB2 peut y être installé pour démarrer le système.\n"
            "- **UEFI (Unified Extensible Firmware Interface)** : Le successeur du BIOS. Il utilise une partition spéciale, la **ESP (EFI System Partition)**, pour stocker les chargeurs de démarrage.\n"
            "- **GPT (GUID Partition Table)** : Le schéma de partitionnement moderne, utilisé avec l'UEFI.\n"
            "- **GRUB.cfg** : Le fichier de configuration final, généré automatiquement. **Ne jamais le modifier directement.**"
        )
        self.set_content("Introduction et Concepts Clés", content)

    def show_error_messages(self):
        content = (
            "**Messages d'erreur courants du mode `grub rescue`** 🚨\n\n"
            "Comprendre le message d'erreur est la première étape pour résoudre le problème. Voici les plus fréquents :\n\n"
            "**1. `error: file '/boot/grub2/i386-pc/normal.mod' not found`**\n"
            "   - **Signification** : GRUB a démarré mais ne parvient pas à trouver ses fichiers modules essentiels, en particulier le module `normal.mod` qui lui permet de charger l'interface complète. Le chemin indiqué (`i386-pc`) est typique des systèmes BIOS.\n"
            "   - **Causes possibles** : Le chemin vers le répertoire de GRUB est incorrect, la partition de démarrage a été supprimée ou corrompue.\n"
            "   - **Solution** : Vous devez d'abord localiser le bon chemin avec la commande `ls` puis utiliser `set root` et `set prefix` pour le corriger temporairement.\n\n"
            "**2. `error: unknown filesystem`**\n"
            "   - **Signification** : GRUB ne reconnaît pas le système de fichiers de la partition sur laquelle il essaie de lire ses fichiers (par exemple, `ext4`).\n"
            "   - **Causes possibles** : Le module de GRUB nécessaire pour lire le système de fichiers n'a pas été chargé ou la partition est corrompue.\n"
            "   - **Solution** : Essayez de charger manuellement le module approprié (par exemple, `insmod ext2` pour une partition `ext4`).\n\n"
            "**3. `error: no such device: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`**\n"
            "   - **Signification** : GRUB recherche une partition par son UUID (identifiant unique), mais ne la trouve pas. Cela se produit si la partition a été reformatée ou supprimée.\n"
            "   - **Solution** : Vous devez trouver la nouvelle désignation de la partition avec `ls` (par exemple, `(hd0,gpt2)`) et l'utiliser pour la commande `set root`.\n\n"
            "**4. `Error 15: File not found` (ancienne erreur GRUB)**\n"
            "   - **Signification** : Le fichier du noyau (`vmlinuz`) ou le fichier de configuration est introuvable. C'est une erreur des anciennes versions de GRUB (GRUB Legacy).\n"
            "   - **Solution** : La logique de dépannage reste la même : utiliser `ls` pour localiser le fichier, puis le charger manuellement.\n\n"
            "**5. `Error 17: Cannot mount selected partition` (ancienne erreur GRUB)**\n"
            "   - **Signification** : GRUB ne peut pas monter ou lire la partition sélectionnée. La partition peut être corrompue ou avoir un système de fichiers inconnu.\n"
            "   - **Solution** : Vérifiez l'intégrité de votre partition depuis un live USB avec `fsck`."
        )
        self.set_content("Messages d'erreur courants", content)

    def show_config_files(self):
        content = (
            "**Fichiers de Configuration et la logique de GRUB2** 📖\n\n"
            "Comprendre où GRUB2 stocke ses informations est essentiel pour le dépannage.\n\n"
            "**1. `/etc/default/grub` : Le fichier de configuration global**\n"
            "   - Contient les variables d'apparence et de comportement du menu.\n"
            "   - Exemples de variables : `GRUB_TIMEOUT=5`, `GRUB_DEFAULT=saved`, `GRUB_CMDLINE_LINUX=\"rhgb quiet\"`.\n"
            "   - **Important :** Toute modification de ce fichier nécessite de lancer `grub2-mkconfig` pour être prise en compte.\n\n"
            "**2. `/etc/grub.d/ : Les scripts générateurs**\n"
            "   - Ce répertoire contient des scripts qui sont exécutés dans un ordre numérique pour construire `grub.cfg`.\n"
            "   - `10_linux` : Détecte les noyaux Linux installés.\n"
            "   - `30_os-prober` : Cherche et ajoute d'autres systèmes d'exploitation (Windows, autres Linux).\n"
            "   - `40_custom` : Le script idéal pour ajouter vos propres entrées de démarrage manuelles.\n\n"
            "**3. `/boot/grub2/grub.cfg : Le fichier final**\n"
            "   - C'est le résultat de l'exécution des scripts de `/etc/grub.d/`.\n"
            "   - C'est le fichier que GRUB2 lit pour afficher le menu. Il est généré automatiquement et ne doit jamais être édité à la main."
        )
        self.set_content("Fichiers de Configuration et la logique de GRUB2", content)
    
    def show_commands(self):
        content = (
            "**Commandes de dépannage dans le mode `grub rescue`** ⚙️\n\n"
            "Voici une explication plus approfondie des commandes disponibles.\n\n"
            "**`ls` : La commande de reconnaissance**\n"
            "   - **Fonction :** Affiche la liste des disques et partitions connus par GRUB. C'est l'étape de diagnostic principale pour trouver où se trouve votre OS.\n"
            "   - **Syntaxe :** `ls` pour les disques. `ls (hd0,gpt1)/` pour explorer une partition.\n"
            "   - **Exemple :** Si `ls (hd0,gpt2)/` affiche des répertoires comme `boot`, `etc`, `home`, il y a de fortes chances que ce soit votre partition racine.\n\n"
            "**`set` : La commande de configuration temporaire**\n"
            "   - **Fonction :** Permet de définir les chemins vers les fichiers de GRUB pour que les autres commandes fonctionnent. Ces réglages ne sont valables que pour la session en cours.\n"
            "   - **Syntaxe :** `set root=(hdX,Y)` et `set prefix=(hdX,Y)/boot/grub`.\n"
            "   - **Exemple :** `set root=(hd0,gpt2)` et `set prefix=(hd0,gpt2)/boot/grub` pour indiquer à GRUB de regarder sur cette partition.\n\n"
            "**`insmod` : La commande de chargement des modules**\n"
            "   - **Fonction :** Charge des modules GRUB. Le plus vital est le module `normal` pour accéder à la pleine puissance de GRUB et afficher le menu.\n"
            "   - **Syntaxe :** `insmod normal`\n\n"
            "**`linux` et `initrd` : Les commandes de démarrage manuel**\n"
            "   - **Fonction :** Ces deux commandes sont les plus importantes pour lancer un système sans passer par le menu GRUB. Elles chargent le noyau (`linux`) et le système de fichiers initial (`initrd`).\n"
            "   - **Syntaxe :** `linux /boot/vmlinuz-... root=/dev/sdXY` et `initrd /boot/initramfs-...img`.\n"
            "   - **Note :** Le chemin doit correspondre aux fichiers que vous avez trouvés avec `ls`. Le paramètre `root=/dev/sdXY` est crucial : il doit pointer vers le nom de votre partition racine, par exemple `/dev/sda2`.\n\n"
            "**`boot` : La commande d'exécution**\n"
            "   - **Fonction :** Démarre le système après que les commandes `linux` et `initrd` ont été exécutées avec succès."
        )
        self.set_content("Commandes de dépannage dans le mode `grub rescue`", content)
        
    def show_manual_boot(self):
        content = (
            "**Procédure de Démarrage Manuelle depuis `grub rescue`** 🚀\n\n"
            "Suivez ces étapes dans l'ordre pour démarrer temporairement votre système et pouvoir le réparer.\n\n"
            "**Étape 1 : Localiser les fichiers essentiels**\n"
            "   - À l'invite `grub rescue>`, commencez par lister les périphériques pour identifier vos partitions. Par exemple : `ls`.\n"
            "   - Ensuite, explorez chaque partition jusqu'à ce que vous trouviez celle qui contient le répertoire `/boot` et le sous-répertoire `/boot/grub`. C'est votre partition de démarrage.\n"
            "   - `grub rescue> ls (hd0,gpt2)/`\n"
            "   - `grub rescue> ls (hd0,gpt2)/boot/grub`\n"
            "   - `grub rescue> ls (hd0,gpt2)/boot/` (pour trouver les noms des fichiers `vmlinuz` et `initramfs`).\n\n"
            "**Étape 2 : Définir les variables d'environnement**\n"
            "   - Maintenant que vous avez trouvé la bonne partition (par exemple, `(hd0,gpt2)`), dites à GRUB où se trouve le reste de ses fichiers.\n"
            "   - `grub rescue> set root=(hd0,gpt2)`\n"
            "   - `grub rescue> set prefix=(hd0,gpt2)/boot/grub`\n\n"
            "**Étape 3 : Tenter de revenir au menu normal**\n"
            "   - C'est la solution la plus simple si les fichiers de GRUB sont intacts mais que le chemin est perdu.\n"
            "   - `grub rescue> insmod normal`\n"
            "   - `grub rescue> normal`\n"
            "   - Si le menu de GRUB apparaît, vous pouvez démarrer votre système et passer à l'étape de réparation définitive.\n\n"
            "**Étape 4 : Démarrer manuellement le noyau**\n"
            "   - Si l'étape 3 échoue, c'est que quelque chose ne va pas avec le module `normal` ou `grub.cfg`. Vous devez alors démarrer le noyau et l'initrd manuellement.\n"
            "   - **Attention :** Les noms des fichiers `vmlinuz` et `initramfs` dépendent de la version de votre noyau. Utilisez `ls` pour les trouver.\n"
            "   - `grub rescue> linux /boot/vmlinuz-5.18.10-200.fc36.x86_64 root=/dev/sda2 ro`\n"
            "   - `grub rescue> initrd /boot/initramfs-5.18.10-200.fc36.x86_64.img`\n"
            "   - `grub rescue> boot`"
        )
        self.set_content("Procédure de Démarrage Manuelle", content)

    def show_repair(self):
        content = (
            "**Réparation Définitive après le démarrage** 🔧\n\n"
            "Une fois que vous avez réussi à démarrer votre système, il est crucial de réparer GRUB pour éviter que le problème ne se reproduise.\n\n"
            "**1. Réinstaller le chargeur de démarrage**\n"
            "   - Ouvrez un terminal. Les commandes varient selon que vous utilisez le BIOS/MBR ou l'UEFI.\n"
            "   - **Pour BIOS/MBR :** Réinstallez GRUB sur le MBR du disque. `sdX` doit être remplacé par le nom de votre disque dur (ex: `sda`), et non une partition.\n"
            "     `sudo grub2-install /dev/sdX`\n"
            "   - **Pour UEFI :** Réinstallez GRUB sur la partition ESP (`/boot/efi`).\n"
            "     `sudo grub2-install --target=x86_64-efi --efi-directory=/boot/efi`\n\n"
            "**2. Générer le fichier de configuration**\n"
            "   - Une fois GRUB réinstallé, vous devez créer un nouveau fichier `grub.cfg` propre qui reflète l'état actuel de votre système.\n"
            "   - `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`\n\n"
            "**3. Vérification**\n"
            "   - Après ces deux étapes, redémarrez votre machine. Le menu de démarrage devrait apparaître normalement et vous permettre de choisir votre système."
        )
        self.set_content("Réparation Définitive", content)

    def show_architecture(self):
        content = (
            "**Impact de l'architecture x86 vs x64 sur GRUB** 🖥️\n\n"
            "La différence d'architecture est cruciale car elle détermine les fichiers et les commandes que vous devez utiliser. Une erreur ici peut empêcher la réparation de fonctionner.\n\n"
            "**1. Fichiers du noyau et de l'initramfs**\n"
            "   - Les noms des fichiers du noyau (`vmlinuz`) et de l'initramfs (`initramfs`) reflètent l'architecture.\n"
            "   - **x64** : `vmlinuz-...**.x86_64**` ou `initramfs-...**.x86_64**.img`\n"
            "   - **x86** : `vmlinuz-...**.i686**` ou `initramfs-...**.i686**.img`\n"
            "   - **Conséquence** : Tenter de démarrer un noyau de la mauvaise architecture ne fonctionnera pas. Il est vital de vérifier les noms de fichiers avec `ls`.\n\n"
            "**2. Commandes de réinstallation de GRUB2**\n"
            "   - Les commandes pour réinstaller GRUB sur un système **UEFI** sont spécifiques à l'architecture.\n"
            "   - **x64** : `sudo grub2-install --target=**x86_64-efi** --efi-directory=/boot/efi`\n"
            "   - **x86** : `sudo grub2-install --target=**i386-efi** --efi-directory=/boot/efi`\n"
            "   - **Conséquence** : Utiliser la mauvaise commande installera un chargeur de démarrage incompatible, laissant le système non amorçable. Assurez-vous de connaître l'architecture de votre système avant de lancer ces commandes."
        )
        self.set_content("Architecture x86 vs x64", content)
        
    def show_disks(self):
        content = (
            "**Types de disques, de partitions et leur rôle** 💾\n\n"
            "Une bonne compréhension des types de disques et des schémas de partitionnement est fondamentale pour un dépannage réussi.\n\n"
            "**1. Schémas de partitionnement :**\n"
            "   - **MBR (Master Boot Record) :** Le schéma de partitionnement historique. Il supporte jusqu'à 4 partitions primaires et est limité à des disques de 2 To. Le chargeur de démarrage est stocké dans le premier secteur du disque, le MBR.\n"
            "   - **GPT (GUID Partition Table) :** Le standard moderne pour l'UEFI. Il supporte un nombre de partitions virtuellement illimité et des disques de grande taille. Le chargeur de démarrage est stocké sur une partition dédiée, l'**ESP (EFI System Partition)**.\n\n"
            "**2. Le rôle du chargeur de démarrage :**\n"
            "   - **BIOS :** Le BIOS (Basic Input/Output System) lit le MBR du disque principal. Le code du MBR contient une partie de GRUB2 qui pointe vers le reste des fichiers de GRUB. C'est l'amorce.\n"
            "   - **UEFI :** L'UEFI lit les informations de l'ESP pour savoir quel chargeur de démarrage lancer. GRUB2 se trouve dans un répertoire de l'ESP et est directement exécuté par l'UEFI."
        )
        self.set_content("Types de disques et partitions", content)
        
    def show_troubleshooting(self):
        content = (
            "**Scénarios de Dépannage courants et leurs solutions** 🛠️\n\n"
            "**Scénario 1 : `grub rescue` après une mise à jour de noyau**\n"
            "   - **Problème :** Le nouveau noyau n'est pas correctement configuré ou les liens symboliques pointant vers le bon noyau sont cassés.\n"
            "   - **Solution :** Suivez la procédure de **démarrage manuel** pour démarrer avec l'ancien noyau qui fonctionnait. Une fois le système démarré, réinstallez GRUB2 avec `grub2-mkconfig`.\n\n"
            "**Scénario 2 : `grub rescue` après l'installation de Windows**\n"
            "   - **Problème :** L'installation de Windows a écrasé le MBR ou l'ESP et a remplacé GRUB2 par son propre chargeur de démarrage.\n"
            "   - **Solution :** Démarrez sur un système live (clé USB Fedora) et suivez les instructions de la section **Réparation Définitive** pour réinstaller GRUB2 sur le MBR ou l'ESP.\n\n"
            "**Scénario 3 : `grub rescue` après la suppression d'une partition**\n"
            "   - **Problème :** La partition contenant les fichiers GRUB ou le noyau a été supprimée ou formatée.\n"
            "   - **Solution :** Si les données sont irrécupérables, vous devrez réinstaller le système d'exploitation. Si la partition est simplement déconnectée ou corrompue, vous pouvez essayer de la réparer avec des outils comme `fsck` depuis un live CD. L'objectif est de rendre la partition de boot lisible pour GRUB."
        )
        self.set_content("Scénarios de Dépannage", content)

    def show_faq(self):
        content = (
            "**FAQ et Notions Avancées** ❓\n\n"
            "**Q: Pourquoi les noms de partitions (ex: `sda2`) sont différents de ceux de GRUB (ex: `(hd0,gpt2)`) ?**\n"
            "   - R: GRUB utilise sa propre notation pour les disques et les partitions. `(hd0)` correspond généralement à `sda`, `(hd1)` à `sdb`, etc. De même, `gpt2` correspond à la deuxième partition GPT (`sda2`).\n\n"
            "**Q: Que faire si ma partition `/boot` est séparée de ma partition racine ?**\n"
            "   - R: Dans ce cas, les commandes `set root` et `set prefix` doivent pointer vers la partition `/boot`, et non vers la partition racine. La commande `linux` devra toujours utiliser l'argument `root=/dev/sdX` pour pointer vers la partition racine réelle."
        )
        self.set_content("FAQ et Notions Avancées", content)

if __name__ == "__main__":
    app = GrubApp()
    app.mainloop()