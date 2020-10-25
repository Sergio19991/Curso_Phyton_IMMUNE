
i = 0

def setup():
    global pizza, refresco, kleenex, imagenes
    size(800, 600)
    pizza = loadImage("pizza.jpg")
    refresco = loadImage("refresco.jpg")
    kleenex = loadImage("kleenex.jpg")
    #Lista
    imagenes = [pizza, refresco, kleenex]

def draw():
    background(255)
    image(imagenes[i], 375, 275)

def mouseClicked():
    global i
    i = i + 1
    if i == 3:
        i = 0
