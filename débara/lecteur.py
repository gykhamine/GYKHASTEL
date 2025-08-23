import cv2

# Créez une instance du détecteur de QR code.
qr_detector = cv2.QRCodeDetector()

# Chemin d'accès à votre image de QR code.
chemin_image = "/home/gykhamine/AO.png"

# Lisez l'image à partir du fichier.
image = cv2.imread(chemin_image)

# Vérifiez que l'image a bien été chargée.
if image is None:
    print(f"Erreur : Le fichier '{chemin_image}' n'a pas pu être lu.")
else:
    # Détectez et décodez le QR code.
    data, points, _ = qr_detector.detectAndDecode(image)

    # Affichez les résultats.
    if data:
        print("QR Code détecté et décodé!")
        print(f"Données : {data}")
    else:
        print("Aucun QR Code n'a été trouvé dans l'image.")