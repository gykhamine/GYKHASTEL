import os
from transformers import pipeline

# Définir le répertoire où les modèles seront sauvegardés.
# Le script créera ce dossier s'il n'existe pas.
SAVE_DIR = "./local_hf_pipelines"
os.makedirs(SAVE_DIR, exist_ok=True)
print(f"Les modèles seront sauvegardés dans : {SAVE_DIR}\n")

# Dictionnaire des tâches et des noms de modèles par défaut.
# Chaque paire clé-valeur représente une tâche et le modèle associé.
tasks_to_download = {
    # Tâches de Traitement du Langage Naturel (NLP)
    "sentiment-analysis": "distilbert-base-uncased-finetuned-sst-2-english", # Tâche : analyse de sentiment (détecter si un texte est positif ou négatif).
    "text-generation": "gpt2",                                             # Tâche : génération de texte (compléter une phrase ou créer un texte).
    "summarization": "facebook/bart-large-cnn",                            # Tâche : résumé de texte (réduire un texte long en une version plus courte).
    "translation_en_to_fr": "Helsinki-NLP/opus-mt-en-fr",                    # Tâche : traduction (convertir un texte d'une langue à une autre).
    "question-answering": "distilbert-base-cased-distilled-squad",           # Tâche : réponse aux questions (extraire une réponse d'un texte).
    "ner": "dbmdz/bert-large-cased-finetuned-conll03-english",              # Tâche : reconnaissance d'entités nommées (identifier personnes, lieux, etc.).
    "zero-shot-classification": "facebook/bart-large-mnli",                 # Tâche : classification sans exemple (catégoriser un texte sans entraînement préalable).
    "fill-mask": "bert-base-uncased",                                       # Tâche : remplissage de masques (prédire le mot manquant dans une phrase).

    # Tâches de Vision par Ordinateur
    "image-classification": "google/vit-base-patch16-224",                 # Tâche : classification d'images (attribuer une étiquette à une image entière).
    "object-detection": "facebook/detr-resnet-50",                          # Tâche : détection d'objets (identifier des objets avec des boîtes).
    "image-to-text": "nlpconnect/vit-gpt2-image-captioning",                # Tâche : légendage d'images (générer une description textuelle pour une image).

    # Tâches Audio
    "automatic-speech-recognition": "openai/whisper-tiny",                 # Tâche : reconnaissance de la parole (transcrire de l'audio en texte).
    "audio-classification": "facebook/wav2vec2-base-960h",                 # Tâche : classification audio (catégoriser un son ou un fichier audio).
}

# Boucle pour télécharger et sauvegarder chaque modèle.
for task_name, model_name in tasks_to_download.items():
    print(f"--- Démarrage du téléchargement pour la tâche : '{task_name}' ---")
    try:
        # Créer le pipeline qui gère le téléchargement et la configuration.
        p = pipeline(task=task_name, model=model_name)

        # Créer un chemin de sauvegarde unique pour ce modèle.
        # Le nom du modèle est nettoyé pour être utilisé comme nom de dossier.
        model_save_path = os.path.join(SAVE_DIR, model_name.replace("/", "_"))
        
        # Sauvegarder les fichiers du modèle et du tokenizer dans le dossier local.
        p.save_pretrained(model_save_path)
        print(f"✅ Modèle '{model_name}' pour la tâche '{task_name}' sauvegardé dans {model_save_path}.\n")
    except Exception as e:
        # En cas d'erreur de téléchargement (ex: pas de connexion), l'utilisateur est notifié.
        print(f"❌ Échec du téléchargement du modèle '{model_name}' pour la tâche '{task_name}'. Erreur : {e}\n")

print("--------------------------------------------------")
print("✅ Le script de téléchargement des modèles est terminé. Tous les modèles spécifiés sont maintenant disponibles localement.")
print("--------------------------------------------------")