
def setup():
    global pizza, refresco
    size(800, 600)
    pizza = loadImage("pizzabox.jpg")
    refresco = loadImage("refresco.jpg")
    

def draw():
    background(255)
    image(refresco, 250, 150)
    image(pizza, 500, 300)
