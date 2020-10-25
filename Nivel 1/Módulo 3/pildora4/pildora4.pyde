
dimension = 5

def setup():
    size(600, 400)
    
def draw():
    pass

def keyPressed():
    global dimension
    background(200, 37, 100)
    letra = loadFont("letra.vlw")
    textFont(letra, dimension)
    text("Hola mundo!", 0, 200)
    if dimension < 130:
        dimension += 1
    if dimension == 130:
        textFont(letra, 30)
        text("Has llegado a la dimension maxima", 0, 300)
