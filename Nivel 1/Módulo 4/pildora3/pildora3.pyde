
def setup():
    global foto
    size(600, 338)
    foto = loadImage("mario.jpg")

def draw():
    global foto
    image(foto, 0, 0)
    fill(0, 0, 255)
    rect(100, 100, 30, 30)
