
def setup():
    global mi_fuente
    size(600, 400)
    mi_fuente = loadFont("fuente.vlw")

def draw():
    background(255)
    fill(0)
    textFont(mi_fuente, 30)
    text("Hola Mundoooooo!", 40, 100, 200, 200)
