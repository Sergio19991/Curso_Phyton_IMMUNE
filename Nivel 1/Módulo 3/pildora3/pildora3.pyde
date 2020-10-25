
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
    dimension += 1
