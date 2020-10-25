
dimension = 5

def setup():
    size(600, 400)
    
def draw():
    global dimension
    background(200, 37, 100)
    letra = loadFont("letra.vlw")
    textFont(letra, dimension)
    text("Hola mundo!", 0, 200)
    textFont(letra, 30)
    text("Estais bien?", 20, 250)
    dimension += 1
