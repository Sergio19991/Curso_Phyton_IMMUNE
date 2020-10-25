
def setup():
    size(1000, 600)
    background(255)

def draw():
    fill(0, 0, random(255))
    ellipse(random(100, 900), random(100, 500), 50, 50)
