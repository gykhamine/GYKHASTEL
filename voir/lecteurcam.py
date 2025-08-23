import cv2

# Créer un objet de détection de QR code
qr_detector = cv2.QRCodeDetector()

# Initialiser la capture vidéo
cap = cv2.VideoCapture(0)

print("Recherche d'un QR Code en cours. La fenêtre se fermera automatiquement après la lecture.")

while True:
    # Lire un frame de la caméra
    ret, frame = cap.read()
    
    # Si la lecture échoue, on quitte
    if not ret:
        print("Erreur: Impossible de lire le flux de la caméra.")
        break
    
    # Décoder le QR code dans le frame
    data, points, _ = qr_detector.detectAndDecode(frame)
    
    # Afficher le flux vidéo dans une fenêtre
    cv2.imshow("Recherche de QR Code...", frame)
    
    # Vérifier si des données ont été trouvées
    if data:
        print(f"QR Code lu : {data}")
        # Sortir de la boucle si un code a été trouvé
        break
    
    # Laisser la boucle continuer si aucune touche n'est pressée
    cv2.waitKey(1)

# Libérer les ressources de la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()