from PIL import Image #import l'ensemble des fonctionnalités de manipulation d'image de la bibliothèque PIL (pillow)
# does compile, makes the image, but black
def draw():
    userInput = int(input("Enter a value betweeen 0-255"))

    width = 365
    height = 141
    gray = None  # Initialise la variable gray a None
    gray = Image.new('RGB', (width, height))  # Crée une image vide <<<

    with gray as im:
        for x in range(0, width):  # Itère sur l'image <<<
            for y in range(0, height):
                r, g, b = im.getpixel((x, y))  # lit un pixel, ici l'image est en couleur, en niveau de gris getpixel renvoie une seule valeur <<<
                value = (r + g + b) / 3.  # moyenne les valeurs de couleurs pour créer une valeur de gris
                value = int(value)  # la valeur précédente est un réel, elle est transformée en entier
                if (userInput > value):
                    im.putpixel((x, y), 0)
                else:
                    im.putpixel((x, y), 255)
        im.show()  # afiche le résultat en niveau de gris <<<

if True:
    draw()