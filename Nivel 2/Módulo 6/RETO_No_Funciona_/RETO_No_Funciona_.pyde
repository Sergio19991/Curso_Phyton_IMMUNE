
i = 0
f = 0

def setup():
    size(800, 600)

    global botella, pizza, leche, comida, pilas

    global verde, azul, amarillo, gris, puntolimpio

    global imagenes, frases

    botella = loadImage("botella.jpg")
    pizza = loadImage("pizza.jpg")
    leche = loadImage("leche.jpg")
    comida = loadImage("comida.jpg")
    pilas = loadImage("pilas.jpg")

    verde = loadFont("fuente.vlw")
    azul = loadFont("fuente.vlw")
    amarillo = loadFont("fuente.vlw")
    gris = loadFont("fuente.vlw")
    puntolimpio = loadFont("fuente.vlw")

    imagenes = [botella, pizza, leche, comida, pilas]
    frases = [verde, azul, amarillo, gris, puntolimpio]

    background(255)

def draw():
    image(imagenes[i], 250, 100)
    fill(0)
    textFont(frases[f], 20)
    verde = text("Esto va en el contenedor VERDE", 20, 20)
    azul = text("Esto va en el contenedor AZUL", 20, 20)
    amarillo = text("Esto va en el contenedor AMARILLO", 20, 20)
    gris = text("Esto va en el contenedor GRIS", 20, 20)
    puntolimpio = text("Esto va al PUNTO LIMPIO", 20, 20)    

def mouseClicked():
    global i, f

    i = i + 1
    if i == 5:
        i = 0

    f = f + 1
    if f == 5:
        f = 0
        
        
        
        
             #Sergio Bejarano Arroyo.
