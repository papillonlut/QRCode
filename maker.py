import qrcode

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    version=1, # Taille, type, complexité
    box_size=5, # Dimension
    border=1 # Bordure externe
)

value = "https://github.com/papillonlut/qrcode"

qr.add_data(value)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')