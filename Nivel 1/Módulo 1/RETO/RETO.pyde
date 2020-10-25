
def setup():
    size(200, 300)   #Este comando establece las dimensiones de la ventanta en píxeles (Ancho po Alto); respectivamente.
    background(64, 88, 234)   #Este comando establece el fondo de la ventana en RGB; respectivamente.
    pass   #Este comando se utiliza para detener la ejecución de lo anterior escrito.
    
def draw():
         #Aquí empieza las dos bolas grandes:
    fill(255, 255, 255)   #Este comando establece el color de las figuras que se escribirán debajo.
    noStroke()   #Este comando se utiliza para quitar los bordes de las figuras.
    ellipse(100, 210, 130, 130)   #Comando que establece el tipo de figura, seguido de la Posición en píxeles (Eje X por Eje Y respectivamente), y la Dimensión en píxeles (Ancho por Alto respectivamente).
    ellipse(100, 110, 100, 100)   #Los ejes X e Y empizan desde la parte superior izquierda; a partir de ahí se va desplazando en píxeles.
         #Aquí empieza las tres bolitas engras:
    fill(0, 0, 0)
    noStroke()
    ellipse(100, 250, 10, 10)
    ellipse(100, 220, 10, 10)
    ellipse(100, 190, 10, 10)
         #Aquí empieza la bufanda:
    fill(222, 127, 11)
    noStroke()
    rect(45, 135, 110, 25)
    rect(45, 135, 25, 110)
         #Aquí empeiza la boca:
    fill(0, 0, 0)
    noStroke()
    ellipse(100, 125, 40, 10)
    fill(255, 255, 255)
    noStroke()
    ellipse(100, 120, 40, 10)
         #Aquí empiezan los dos ojos:
    fill(0, 0, 0)
    noStroke()
    ellipse(80, 95, 15, 15)
    ellipse(120, 95, 15, 15)
         #Aquí empeiza la nariz:
    fill(200, 100, 20)
    stroke(0, 0, 0)
    ellipse(100, 110, 15, 15)
         #Aquí empieza el sombrero:
    fill(255, 0, 0)
    noStroke()
    rect(50, 55, 100, 10)
    rect(65, 20, 70, 40)
    fill(255, 255, 0)
    stroke(0, 0, 0)
    rect(65, 35, 70, 8)
    pass
    
    """Comando para figuras:
        -rect = Rectángulo/Cuadrado.
        -ellipse = Elipse/Círculo."""
    
#Sergio Bejarano Arroyo.
