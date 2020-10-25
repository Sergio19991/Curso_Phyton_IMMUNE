
priemra_vez = True

primera_vez = True

def setup():
    global foto, primera_vez
    size(1280, 720)
    foto = loadImage("balon.jpg")

def draw():
    global foto, primera_vez
    background(138, 245, 245)
    image(foto, random(1000), random(400))
    fill(0)
    fuente = loadFont("letra.vlw")
    textFont(fuente, 50)
    text("El mejor balon de balonmano!!!", 200, 360)
    if primera_vez == True:
        primera_vez = False
    elif primera_vez == False:
        delay(200)     #Sirve para realentizar la ejecución anterior (Un Segundo = 1000)
        
        
        
        
       #Sergio Bejarano Arroyo.      
