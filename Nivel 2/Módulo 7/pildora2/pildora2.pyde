
i = 0
primera_vez = True

def setup():

    global pizza, refresco, kleenex, imagenes

    size(800, 600)
    pizza = loadImage("pizza.jpg")
    refresco = loadImage("refresco.jpg")
    kleenex = loadImage("kleenex.jpg")

    #Lista
    imagenes = [pizza, refresco, kleenex]

def draw():

    global i, primera_vez, tiempo

    if primera_vez == True:
        tiempo = millis()
        primera_vez = False

    background(255)
    image(imagenes[i], 375, 275)

    #hasta que no pase un segundo, no sumo uno a i

    if tiempo + 1000 < millis():
        i = i+1
        if i == 3:
            i = 0
        primera_vez = True

    print(tiempo)
