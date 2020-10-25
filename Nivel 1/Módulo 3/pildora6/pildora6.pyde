
dimensionX = 20
dimensionY = 20

def setup():
    size(600, 400)

def draw():
    pass

def mousePressed():
    background(240, 70, 180)
    global dimensionX, dimensionY
    dimensionX = mouseX
    dimensionY = mouseY
    ellipse(200, 200, dimensionX, dimensionY)
