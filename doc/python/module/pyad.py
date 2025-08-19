import customtkinter as ctk
import pyaudio
import wave
import numpy as np
from scipy.signal import butter, lfilter

# Constantes pour l'enregistrement audio
CHUNK = 1024  # Taille des "chunks" (morceaux de données)
FORMAT = pyaudio.paInt16 # Format des échantillons (16 bits)
CHANNELS = 1 # Mono
RATE = 44100 # Taux d'échantillonnage (44.1 kHz, qualité CD)
RECORD_SECONDS = 5 # Durée de l'enregistrement

class PyAudioApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime : Introduction à PyAudio")
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
        self.intro_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Introduction à PyAudio",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_intro)
        self.intro_button.pack(fill="x", padx=10, pady=5)
        
        self.devices_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Périphériques Audio",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_devices)
        self.devices_button.pack(fill="x", padx=10, pady=5)

        self.record_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Enregistrement Audio",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_record)
        self.record_button.pack(fill="x", padx=10, pady=5)

        self.play_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Lecture d'un fichier .wav",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_play)
        self.play_button.pack(fill="x", padx=10, pady=5)
        
        self.volume_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Contrôle du volume",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_volume)
        self.volume_button.pack(fill="x", padx=10, pady=5)

        self.filter_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Filtrage Audio (Passe-Haut)",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_filter)
        self.filter_button.pack(fill="x", padx=10, pady=5)

        self.realtime_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Traitement Audio en Direct",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_realtime)
        self.realtime_button.pack(fill="x", padx=10, pady=5)

        # --- Création du cadre principal pour le contenu ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")
        
        # --- Démarrage sur le premier onglet ---
        self.show_intro()
        
    def set_content(self, title, text, code=None):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        if code:
            self.content_textbox.insert("end", f"\n\n```python\n{code}\n```")
        
        self.content_textbox.configure(state="disabled")

    def show_intro(self):
        content = (
            "**Introduction à la bibliothèque PyAudio** 🎤\n\n"
            "**PyAudio** est une bibliothèque Python qui fournit des liaisons pour la bibliothèque **PortAudio**, une API multiplateforme qui permet la lecture et l'enregistrement audio. Elle est essentielle pour quiconque souhaite travailler avec des fonctionnalités audio en direct en Python.\n\n"
            "**Concepts Clés :**\n"
            "- **Flux (Stream) :** C'est le canal par lequel les données audio sont lues ou écrites. Un flux peut être en mode **Entrée** (pour l'enregistrement) ou en mode **Sortie** (pour la lecture).\n"
            "- **Chunks :** PyAudio ne traite pas le son en une seule fois, mais par petits morceaux de données appelés *chunks*.\n"
            "- **Taux d'échantillonnage (Rate) :** C'est le nombre d'échantillons audio capturés ou lus par seconde, généralement exprimé en Hertz (Hz). Par exemple, 44100 Hz est la qualité standard d'un CD audio.\n"
            "- **Format :** Le format de l'échantillon définit la résolution de l'audio (par exemple, 16 bits)."
        )
        self.set_content("Introduction à PyAudio", content)
    
    def show_devices(self):
        code_example = (
            "import pyaudio\n\n"
            "p = pyaudio.PyAudio()\n"
            "info = p.get_host_api_info_by_index(0)\n"
            "numdevices = info.get('deviceCount')\n\n"
            "print('--- Périphériques audio disponibles ---')\n"
            "for i in range(0, numdevices):\n"
            "    device = p.get_device_info_by_host_api_device_index(0, i)\n"
            "    print(f\"ID {i}: {device.get('name')} | Entrées: {device.get('maxInputChannels')} | Sorties: {device.get('maxOutputChannels')}\")\n\n"
            "p.terminate()\n"
        )
        content = (
            "**Liste des périphériques audio disponibles** 💻\n\n"
            "La première étape de tout projet audio est de savoir quels périphériques (microphones, haut-parleurs) sont connectés à votre système.\n\n"
            "**Comment ça marche :**\n"
            "   - On initialise d'abord l'objet **`PyAudio`**.\n"
            "   - On parcourt ensuite la liste des périphériques pour récupérer des informations telles que leur nom (`'name'`), le nombre de canaux d'entrée (`'maxInputChannels'`) et de sortie (`'maxOutputChannels'`).\n"
            "   - C'est l'**ID du périphérique** (l'index `i`) qui nous permettra de le sélectionner plus tard pour l'enregistrement ou la lecture.\n\n"
            "**Conseil :** Le périphérique par défaut a généralement l'ID 0, mais il est toujours bon de vérifier les ID pour les périphériques spécifiques."
        )
        self.set_content("Périphériques Audio", content, code_example)
        
    def show_record(self):
        code_example = (
            "import pyaudio\n"
            "import wave\n"
            "import time\n\n"
            "CHUNK = 1024\n"
            "FORMAT = pyaudio.paInt16\n"
            "CHANNELS = 1\n"
            "RATE = 44100\n"
            "RECORD_SECONDS = 5\n"
            "WAVE_OUTPUT_FILENAME = 'output.wav'\n\n"
            "p = pyaudio.PyAudio()\n"
            "try:\n"
            "    stream = p.open(format=FORMAT,\n"
            "                    channels=CHANNELS,\n"
            "                    rate=RATE,\n"
            "                    input=True,\n"
            "                    frames_per_buffer=CHUNK)\n"
            "    print('Enregistrement en cours...')\n"
            "    frames = []\n"
            "    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):\n"
            "        data = stream.read(CHUNK)\n"
            "        frames.append(data)\n"
            "    print('Enregistrement terminé.')\n"
            "finally:\n"
            "    if stream.is_active():\n"
            "        stream.stop_stream()\n"
            "    stream.close()\n"
            "    p.terminate()\n\n"
            "wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')\n"
            "wf.setnchannels(CHANNELS)\n"
            "wf.setsampwidth(p.get_sample_size(FORMAT))\n"
            "wf.setframerate(RATE)\n"
            "wf.writeframes(b''.join(frames))\n"
            "wf.close()\n"
        )
        content = (
            "**Enregistrement Audio et sauvegarde en .wav** 💾\n\n"
            "Cette section vous montre comment enregistrer un flux audio depuis un microphone et le sauvegarder dans un fichier `.wav`, le format audio le plus simple et sans compression.\n\n"
            "**Étapes clés :**\n"
            "1.  **Initialisation :** On crée une instance de `PyAudio` et on ouvre un `stream` en mode `input=True`.\n"
            "2.  **Capture de données :** Une boucle lit les données audio par *chunks* à l'aide de `stream.read()`. Chaque chunk est ajouté à une liste.\n"
            "3.  **Fermeture :** Une fois l'enregistrement terminé, il est crucial d'arrêter le flux (`stop_stream()`), de le fermer (`close()`) et de terminer l'instance de `PyAudio` (`terminate()`).\n"
            "4.  **Sauvegarde :** Le module natif **`wave`** est utilisé pour écrire les données capturées dans un fichier `.wav`, en spécifiant les paramètres (`channels`, `sampwidth`, `framerate`).\n\n"
            "**Gestion des erreurs :** L'ajout de blocs `try...finally` garantit que les ressources sont correctement fermées, même si une erreur se produit pendant l'enregistrement."
        )
        self.set_content("Enregistrement Audio", content, code_example)
        
    def show_play(self):
        code_example = (
            "import pyaudio\n"
            "import wave\n"
            "import time\n\n"
            "CHUNK = 1024\n"
            "WAVE_INPUT_FILENAME = 'output.wav'\n\n"
            "try:\n"
            "    wf = wave.open(WAVE_INPUT_FILENAME, 'rb')\n"
            "    p = pyaudio.PyAudio()\n"
            "    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),\n"
            "                    channels=wf.getnchannels(),\n"
            "                    rate=wf.getframerate(),\n"
            "                    output=True)\n"
            "    print('Lecture du fichier en cours...')\n"
            "    data = wf.readframes(CHUNK)\n"
            "    while data:\n"
            "        stream.write(data)\n"
            "        data = wf.readframes(CHUNK)\n"
            "    print('Lecture terminée.')\n"
            "except FileNotFoundError:\n"
            "    print(f\"Erreur: Le fichier {WAVE_INPUT_FILENAME} est introuvable. Veuillez l'enregistrer d'abord.\")\n"
            "finally:\n"
            "    if 'stream' in locals() and stream.is_active():\n"
            "        stream.stop_stream()\n"
            "        stream.close()\n"
            "    if 'p' in locals():\n"
            "        p.terminate()\n"
            "    if 'wf' in locals():\n"
            "        wf.close()\n"
        )
        content = (
            "**Lecture d'un fichier .wav** 🎶\n\n"
            "Cette section montre comment lire un fichier `.wav` existant et le diffuser via la sortie audio par défaut (haut-parleurs).\n\n"
            "**Étapes clés :**\n"
            "1.  **Ouverture du fichier :** Le module `wave` est utilisé pour ouvrir le fichier `.wav` en mode lecture (`'rb'`). On récupère ses paramètres (canaux, taux d'échantillonnage, etc.).\n"
            "2.  **Ouverture du flux :** On ouvre un flux PyAudio en mode `output=True`. Les paramètres du flux sont définis à partir de ceux du fichier `.wav` pour garantir une lecture correcte.\n"
            "3.  **Lecture et écriture :** Une boucle lit les données du fichier par *chunks* (`wf.readframes()`) et les écrit directement dans le flux PyAudio (`stream.write()`).\n"
            "4.  **Fermeture :** Comme pour l'enregistrement, il est crucial de fermer toutes les ressources (`stream`, `p`, `wf`) après la lecture.\n\n"
            "**Gestion des erreurs :** Le bloc `try...except FileNotFoundError` permet de gérer le cas où le fichier audio n'existe pas, évitant ainsi un crash de l'application."
        )
        self.set_content("Lecture d'un fichier .wav", content, code_example)
    
    def show_volume(self):
        code_example = (
            "import pyaudio\n"
            "import numpy as np\n\n"
            "CHUNK = 1024\n"
            "FORMAT = pyaudio.paInt16\n"
            "CHANNELS = 1\n"
            "RATE = 44100\n\n"
            "p = pyaudio.PyAudio()\n"
            "stream = p.open(format=FORMAT,\n"
            "                channels=CHANNELS,\n"
            "                rate=RATE,\n"
            "                input=True,\n"
            "                output=True,\n"
            "                frames_per_buffer=CHUNK)\n\n"
            "print('Traitement du volume en cours... (5s)')\n"
            "volume_factor = 2.0  # Double le volume\n"
            "for i in range(0, int(RATE / CHUNK * 5)):\n"
            "    data_in = stream.read(CHUNK)\n"
            "    # Convertir en tableau NumPy (int16)\n"
            "    numpy_data = np.frombuffer(data_in, dtype=np.int16)\n"
            "    \n"
            "    # Augmenter le volume en multipliant par un facteur\n"
            "    amplified_data = numpy_data * volume_factor\n"
            "    \n"
            "    # Assurer que les valeurs ne dépassent pas les limites du format (int16)\n"
            "    amplified_data = np.clip(amplified_data, -32768, 32767)\n"
            "    \n"
            "    # Convertir de nouveau en données binaires pour la lecture\n"
            "    data_out = amplified_data.astype(np.int16).tobytes()\n"
            "    \n"
            "    stream.write(data_out)\n\n"
            "stream.stop_stream()\n"
            "stream.close()\n"
            "p.terminate()\n"
        )
        content = (
            "**Contrôle du volume en temps réel** 🎚️\n\n"
            "PyAudio, en combinaison avec NumPy, vous permet de manipuler les données audio en direct, comme l'augmentation ou la diminution du volume. Le principe est de lire les données, de les traiter, puis de les réécrire dans le flux.\n\n"
            "**Étapes clés :**\n"
            "1.  **Flux d'entrée/sortie :** On ouvre un seul flux avec `input=True` et `output=True` pour lire depuis l'entrée et écrire vers la sortie simultanément.\n"
            "2.  **Conversion et manipulation :** Les données binaires lues sont converties en un tableau NumPy. On peut alors simplement les multiplier par un facteur pour ajuster le volume.\n"
            "3.  **Gestion des limites :** L'opération de multiplication peut provoquer un **écrêtage (clipping)** si les valeurs dépassent les limites du format (ici `-32768` à `32767` pour `int16`). La fonction `np.clip()` est utilisée pour éviter cela.\n"
            "4.  **Re-conversion :** Les données traitées sont reconverties en format binaire avec `tobytes()` et écrites dans le flux de sortie."
        )
        self.set_content("Contrôle du volume", content, code_example)
        
    def show_filter(self):
        code_example = (
            "import pyaudio\n"
            "import numpy as np\n"
            "from scipy.signal import butter, lfilter\n\n"
            "def butter_highpass(cutoff, fs, order=5):\n"
            "    nyq = 0.5 * fs\n"
            "    normal_cutoff = cutoff / nyq\n"
            "    b, a = butter(order, normal_cutoff, btype='high', analog=False)\n"
            "    return b, a\n\n"
            "def highpass_filter(data, cutoff, fs, order=5):\n"
            "    b, a = butter_highpass(cutoff, fs, order=order)\n"
            "    y = lfilter(b, a, data)\n"
            "    return y\n\n"
            "CHUNK = 1024\n"
            "FORMAT = pyaudio.paInt16\n"
            "CHANNELS = 1\n"
            "RATE = 44100\n"
            "CUTOFF_FREQ = 500  # Fréquence de coupure du filtre passe-haut (en Hz)\n\n"
            "p = pyaudio.PyAudio()\n"
            "stream = p.open(format=FORMAT,\n"
            "                channels=CHANNELS,\n"
            "                rate=RATE,\n"
            "                input=True,\n"
            "                output=True,\n"
            "                frames_per_buffer=CHUNK)\n\n"
            "print('Filtrage passe-haut en cours... (5s)')\n"
            "for i in range(0, int(RATE / CHUNK * 5)):\n"
            "    data_in = stream.read(CHUNK)\n"
            "    numpy_data = np.frombuffer(data_in, dtype=np.int16)\n"
            "    \n"
            "    # Appliquer le filtre passe-haut aux données\n"
            "    filtered_data = highpass_filter(numpy_data, CUTOFF_FREQ, RATE)\n"
            "    \n"
            "    # Convertir et écrire la sortie\n"
            "    data_out = filtered_data.astype(np.int16).tobytes()\n"
            "    stream.write(data_out)\n\n"
            "stream.stop_stream()\n"
            "stream.close()\n"
            "p.terminate()\n"
        )
        content = (
            "**Filtrage audio en temps réel (Passe-Haut)** 🎧\n\n"
            "Le filtrage est une opération essentielle pour manipuler des signaux audio. Un **filtre passe-haut** est un filtre électronique ou numérique qui laisse passer les hautes fréquences tout en atténuant (bloquant) les basses fréquences. Il est souvent utilisé pour éliminer le bruit de fond (bourdonnements, vents) d'un enregistrement vocal.\n\n"
            "**Comment ça marche :**\n"
            "1.  **Définition du filtre :** Les fonctions `butter_highpass()` et `highpass_filter()` utilisent la bibliothèque **`scipy.signal`** pour créer un filtre de Butterworth. On définit une `fréquence de coupure` (ici 500 Hz), ce qui signifie que toutes les fréquences en dessous de 500 Hz seront atténuée.\n"
            "2.  **Traitement des données :** Dans la boucle principale, après avoir lu et converti le *chunk* audio en tableau NumPy, on applique la fonction de filtrage. Le tableau filtré est ensuite reconverti en binaire pour être lu.\n\n"
            "**Note :** Pour utiliser ce code, vous devrez d'abord installer `scipy` (`pip install scipy`)."
        )
        self.set_content("Filtrage Audio (Passe-Haut)", content, code_example)
        
    def show_realtime(self):
        code_example = (
            "import pyaudio\n"
            "import numpy as np\n"
            "import time\n\n"
            "CHUNK = 1024\n"
            "FORMAT = pyaudio.paInt16\n"
            "CHANNELS = 1\n"
            "RATE = 44100\n"
            "THRESHOLD = 500  # Seuil pour la détection sonore\n\n"
            "p = pyaudio.PyAudio()\n"
            "stream = p.open(format=FORMAT,\n"
            "                channels=CHANNELS,\n"
            "                rate=RATE,\n"
            "                input=True,\n"
            "                frames_per_buffer=CHUNK)\n\n"
            "print('Analyse en direct en cours... Parlez fort pour déclencher une alerte.')\n"
            "try:\n"
            "    while True:\n"
            "        data = stream.read(CHUNK)\n"
            "        # Convertir les données binaires en tableau NumPy\n"
            "        numpy_data = np.frombuffer(data, dtype=np.int16)\n"
            "        \n"
            "        # Calcul de l'amplitude maximale pour détecter le volume\n"
            "        amplitude_max = np.max(np.abs(numpy_data))\n"
            "        \n"
            "        if amplitude_max > THRESHOLD:\n"
            "            print(f\"ALERTE! Son détecté. Amplitude: {amplitude_max}\")\n"
            "        \n"
            "except KeyboardInterrupt:\n"
            "    print('Arrêt du traitement en direct.')\n"
            "finally:\n"
            "    stream.stop_stream()\n"
            "    stream.close()\n"
            "    p.terminate()\n"
        )
        content = (
            "**Traitement audio en direct : détection sonore** 🔊\n\n"
            "En plus de simplement lire ou enregistrer, PyAudio vous permet de traiter le son en temps réel pour des applications interactives, comme la détection de son ou la visualisation de l'amplitude. Ici, nous allons voir un exemple de détection simple basée sur le volume.\n\n"
            "**Étapes clés :**\n"
            "1.  **Capture et conversion :** Le principe de base est de capturer un `chunk` de données audio binaires à l'aide de `stream.read()`, puis de le convertir en un tableau **NumPy**.\n"
            "2.  **Analyse d'amplitude :** On peut facilement calculer l'amplitude maximale du signal dans chaque *chunk* avec `np.max(np.abs(numpy_data))`. L'amplitude est un bon indicateur du volume sonore.\n"
            "3.  **Détection :** En comparant cette amplitude à un `THRESHOLD` prédéfini, on peut déclencher une action (comme imprimer un message) lorsque le son dépasse un certain niveau.\n"
            "4.  **Boucle infinie :** La boucle `while True` permet une analyse continue, et un `try...except KeyboardInterrupt` gère l'arrêt du script par l'utilisateur (avec `Ctrl+C`)."
        )
        self.set_content("Traitement Audio en Direct", content, code_example)


if __name__ == "__main__":
    app = PyAudioApp()
    app.mainloop()