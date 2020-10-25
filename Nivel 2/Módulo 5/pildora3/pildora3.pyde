
posicionX = 120
posicionY = 10
dimensionX = 2
dimensionY = 2

def setup():
    size(1000, 600)

def draw():
    background(255)
    global posicionX, posicionY, dimensionX, dimensionY
    fill(0, 0, random(255))
    ellipse(posicionX, posicionY, dimensionX, dimensionY)
    posicionX = posicionX + 1
    posicionY = posicionY + 1
    dimensionX += 1
    dimensionY += 1
