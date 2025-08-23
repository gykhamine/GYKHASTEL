import cv2

# Charge le classificateur pré-entraîné pour la détection de visages
# L'objet 'haarcascade_frontalface_default.xml' doit être dans le même dossier
# ou son chemin complet doit être spécifié.
# Vous pouvez trouver ce fichier dans le dépôt GitHub d'OpenCV :
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('/home/gykhamine/GitHub/GYKHASTEL/voir/haarcascades/haarcascade_frontalface_default.xml')

# Initialise la capture vidéo de la caméra par défaut (index 0)
cap = cv2.VideoCapture(0)

print("Détection faciale en cours. Appuyez sur 'q' pour quitter.")

while True:
    # Lire un frame (image) de la caméra
    ret, frame = cap.read()
    
    # Si la lecture échoue, on quitte la boucle
    if not ret:
        print("Erreur: Impossible de lire le flux de la caméra.")
        break
    
    # Convertit l'image en niveaux de gris
    # C'est plus rapide et souvent plus précis pour les algorithmes de détection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Détecte les visages dans l'image en niveaux de gris
    # Le résultat est une liste de rectangles (x, y, largeur, hauteur) pour chaque visage
    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1, # Facteur d'échelle, ajuste la taille de recherche
        minNeighbors=5,  # Combien de voisins doit avoir un rectangle pour être conservé
        minSize=(30, 30) # Taille minimale du visage à détecter
    )
    
    # Dessine un rectangle autour de chaque visage détecté
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Affiche le flux vidéo avec les rectangles
    cv2.imshow('Detection de Visages', frame)
    
    # Quitte la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libère les ressources de la caméra et ferme toutes les fenêtres
cap.release()
cv2.destroyAllWindows()