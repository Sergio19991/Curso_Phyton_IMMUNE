
add_library("sound")

def setup():
    global cancion
    size(600, 337)
    cancion = SoundFile(this, "mario.mp3")
    cancion.play()
  
def draw():
    image(loadImage("mario.jpg"), 0, 0)
    fill(0, 0, 255)
    rect(random(600), random(400), 50, 50)
