
posicionX = 120
posicionY = 30
movimientoX = 3
movimientoY = 3

def setup():
    size(1200, 600)
    background(255)

def draw():
    global posicionX, posicionY, movimientoY, movimientoX
    fill(random(255), random(255), random(255))
    ellipse(posicionX, posicionY, 50, 50)
    posicionX = posicionX + movimientoX
    posicionY = posicionY + movimientoY
    if posicionY > height - 50/2 or posicionY < 50/2:
        movimientoY = -movimientoY
    if posicionX > width - 50/2 or posicionX < 50/2:
        movimientoX = -movimientoX
        
        
        
        
     #Sergio Bejarano Arroyo.
