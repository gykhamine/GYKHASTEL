import cv2
import os

# Définir le chemin d'accès aux fichiers Haar Cascade
HAAR_CASCADES_PATH = '/home/gykhamine/GitHub/GYKHASTEL/voir/haarcascades/'

# Vérifier si le chemin existe
if not os.path.exists(HAAR_CASCADES_PATH):
    print(f"Erreur : Le répertoire '{HAAR_CASCADES_PATH}' n'existe pas.")
    exit()

# Charger tous les classificateurs
cascades = {
    'frontalface': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_frontalface_default.xml')),
    'profileface': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_profileface.xml')),
    'eye_eyeglasses': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_eye_tree_eyeglasses.xml')),
    'eye': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_eye.xml')),
    'smile': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_smile.xml')),
    'fullbody': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_fullbody.xml')),
    'upperbody': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_upperbody.xml')),
    'catface': cv2.CascadeClassifier(os.path.join(HAAR_CASCADES_PATH, 'haarcascade_frontalcatface.xml')),
    # ... ajoutez les autres si vous voulez
}

# Vérifier que les classificateurs ont été chargés
for name, cascade in cascades.items():
    if cascade.empty():
        print(f"Erreur : '{name}' n'a pas pu être chargé.")
        exit()

# Initialiser la capture vidéo
cap = cv2.VideoCapture(0)
print("Détecteur universel en cours. Appuyez sur 'q' pour quitter.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur: Impossible de lire le flux de la caméra.")
        break
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Détection des visages (point de départ de la hiérarchie)
    faces = cascades['frontalface'].detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)  # Rouge pour le visage
        cv2.putText(frame, 'Visage', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        # Région d'intérêt pour les détections plus spécifiques (yeux, sourires)
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Détection des yeux avec et sans lunettes dans la zone du visage
        eyes_with_glasses = cascades['eye_eyeglasses'].detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes_with_glasses:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2) # Bleu pour les yeux
            cv2.putText(roi_color, 'Yeux', (ex, ey-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
        
        # Détection des sourires
        smiles = cascades['smile'].detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2) # Vert pour le sourire
            cv2.putText(roi_color, 'Sourire', (sx, sy-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    # Détections indépendantes (corps, chat, etc.)
    # Ces détections sont faites sur l'ensemble du frame, car elles ne sont pas hiérarchiquement liées au visage
    
    # Détection des corps
    full_bodies = cascades['fullbody'].detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=3)
    for (bx, by, bw, bh) in full_bodies:
        cv2.rectangle(frame, (bx, by), (bx+bw, by+bh), (255, 255, 0), 2) # Cyan pour le corps
        cv2.putText(frame, 'Corps', (bx, by-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        
    # Détection des chats
    cat_faces = cascades['catface'].detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    for (cx, cy, cw, ch) in cat_faces:
        cv2.rectangle(frame, (cx, cy), (cx+cw, cy+ch), (0, 255, 255), 2) # Jaune pour le chat
        cv2.putText(frame, 'Chat', (cx, cy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Afficher le résultat
    cv2.imshow('Detecteur Multi-Modele', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()