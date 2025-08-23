import pyaudio
import wave
import speech_recognition as sr
import os

# --- PARTIE 1 : ENREGISTREMENT AUDIO AVEC PyAudio ---

# Paramètres d'enregistrement
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
TEMP_FILENAME = "temp_recording.wav"

p = pyaudio.PyAudio()

print("Enregistrement en cours...")

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

frames = []
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Enregistrement terminé.")

# Arrêt et fermeture du flux
stream.stop_stream()
stream.close()
p.terminate()

# Écriture du fichier audio temporaire
wf = wave.open(TEMP_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# --- PARTIE 2 : RECONNAISSANCE VOCALE AVEC SpeechRecognition ---

# Initialisation du reconnaisseur
r = sr.Recognizer()

# Utilisation du fichier audio comme source
with sr.AudioFile(TEMP_FILENAME) as source:
    audio = r.record(source)  # Lit l'intégralité du fichier audio

try:
    print("Analyse de l'audio en cours...")
    # Reconnaissance avec Google Web Speech API (nécessite une connexion Internet)
    texte = r.recognize_google(audio, language="fr-FR")
    print(f"Vous avez dit : {texte}")
except sr.UnknownValueError:
    print("Désolé, je n'ai pas pu comprendre l'audio.")
except sr.RequestError as e:
    print(f"Erreur de l'API de reconnaissance vocale; {e}")
finally:
    # Suppression du fichier temporaire
    if os.path.exists(TEMP_FILENAME):
        os.remove(TEMP_FILENAME)