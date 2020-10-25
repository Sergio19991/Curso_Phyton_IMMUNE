
posicionX = -200
posicionY = -100

def setup():
    size(600, 400)
    

def draw():
    background(200, 37, 100)
    global posicionX, posicionY
    fill(255, 120, 255)
    ellipse(posicionX, posicionY, 50, 50)
    fill(0)
    rect(200, 100, 200, 200)
    posicionX = posicionX + 2
    posicionY = posicionY + 1
