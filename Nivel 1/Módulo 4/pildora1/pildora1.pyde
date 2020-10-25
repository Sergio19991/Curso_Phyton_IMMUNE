
tam = 5
def setup():
    size(600, 400)

def draw():
    global tam
    background(0)
    fuente = loadFont("letra.vlw")
    textFont(fuente, tam)
    text("Hola mundo!", 10, 200)
    tam += 1
    delay(50)
