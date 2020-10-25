
dimension = 5

def setup():
    size(600, 400)
    
def draw():
    global dimension
    background(200, 37, 100)
    letra = loadFont("letra.vlw")
    textFont(letra, dimension)
    text("Hola mundo!", 0, 200)

def keyPressed():
    global dimension
    if key == "a":
        dimension += 3
    elif keyCode == DOWN:
        dimension = dimension - 3
