# Générateur de QR Code<br>
1. Installez les bibliothèques nécessaires<br>
    ```bash
    pip3 install qrcode[pil]
2. Personalisation<br>
    _l.5_ - Modifie la complexité du QR Code ```version=1```<br>
    _l.6_ - Modifie les dimensions ```box_size=5```<br>
    _l.7_ - Change la bordure (si vous utiliser le lecteur associer la bordure doit être de 1 minimum) ```border=1```<br>
    _l.10_ - Ensuite pour rediriger où vous voulez utiliser ```value=""``` pouvant-être un lien ou un texte<br>
    _l.15_ - Enfin pour changer la couleur des "carrés" ```fill_color="black"```, de l'arrière plan ```back_color="white"```<br>
    _l.16_ - Le nom du QR Code peut-être modifiées<br>
Exécutez le script maker.py pour générer un code QR qui sera enregistré sous le nom "qrcode.png"<br><br>
# Lecteur de QR Code
1. Installez les bibliothèques nécessaires<br>
    ```bash
    pip3 install opencv-python
    
2. Personalisation<br>
    Assurez-vous que le QR code généré correspond à _l.5_<br>

Exécutez le script read.py pour lire le code QR.<br>
Assurez-vous d'ajuster les instructions et les détails selon vos besoins spécifiques.
