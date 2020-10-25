
posicionY = 195

def setup():
    size(800, 500)
    
def draw():
    noStroke()
    background(13, 34, 255)
    global posicionX, posicionY
    fill(255, 141, 46)
    ellipse(600, posicionY, 100, 100)
    fill(0, 167, 7)
    rect(0, 250, 800, 250)
    posicionY = posicionY + 1
    
    
    
    
     #Sergio Bejarano Arroyo
