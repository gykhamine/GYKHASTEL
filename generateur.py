import qrcode
from PIL import Image

# Texte ou URL à encoder
data = "https://gykhamine.github.io/GCI/1.html"

# Génération du QR code
qr = qrcode.make(data)


# Sauvegarde dans un fichier image
qr.save("/home/gykhamine/1.png")