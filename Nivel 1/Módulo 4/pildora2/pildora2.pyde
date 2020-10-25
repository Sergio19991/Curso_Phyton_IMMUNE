
tam = 20
primera_vez = True

def setup():
    size(600, 400)

def draw():
    global tam, primera_vez
    background(0)
    fuente = loadFont("letra.vlw")
    textFont(fuente, tam)
    text("Hola mundo!", 10, 200)
    tam += 1
    if primera_vez == True:
        priemera_vez = False
    elif primera_vez == False:
        delay(1000)
