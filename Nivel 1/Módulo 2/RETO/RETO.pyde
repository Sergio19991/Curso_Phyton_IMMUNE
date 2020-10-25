
def setup():
    size(805, 800)   #tamaño de la ventana del programa
    background(183, 241, 247)   #fondo de la ventana de programa
    
def draw():
    
    noStroke()   #define que no hay bordes en la figuras que se irán estableciendo debajo
    
    p = 20   #variable que estabelce el tamaño de cada pixel a dibujar(en este caso 1px equivale a 20px)
    x = 0   #variable que establece dónde empezará cada píxel de tamaño 20px en el eje X
    y = 0   #variable que estabelce dónde empezará cada píxel de tamaño 20px en el eje Y
    
    #Césped:
    fill(76, 175, 80)   #color de la figuras que se irán estebleciendo debajo
    rect(x, y+p*21, p+p*20, p+p*40)   #rect=rectángulo
    rect(x+p*21, y+p*20, p+p*22, p+p*24)
    
    #Nubes:
    fill(84, 110, 122)
        #Primera Nube:
    rect(x+p*2, y+p*2, p*6, p)
    rect(x+p, y+p*3, p*10, p)
    rect(x+p*2, y+p*4, p*9, p)
    rect(x+p*4, y+p*5, p*3, p)
        #Segunda Nube:
    rect(x+p*14, y+p*5, p*6, p)
    rect(x+p*12, y+p*6, p*9, p*2)
    rect(x+p*17, y+p*8, p*3, p)
        #Tercera Nube:
    rect(x+p*25, y+p*2, p*7, p)
    rect(x+p*24, y+p*3, p*12, p)
    rect(x+p*24, y+p*4, p*11, p)
    rect(x+p*28, y+p*5, p*5, p)
    
    #Casa:
        #Fachada:
    fill(93, 64, 55)
    rect(x+p*24, y+p*18, p*12, p*6)
        #Techo:
    fill(62, 39, 35)
    rect(x+p*24, y+p*16, p*12, p*2)
    rect(x+p*25, y+p*15, p*10, p)
    rect(x+p*26, y+p*14, p*8, p)
        #Ventanas:
    fill(255, 255, 0)
    rect(x+p*25, y+p*20, p*2, p*2)
    rect(x+p*33, y+p*20, p*2, p*2)
        #Puerta:
    fill(161, 136, 127)     #La puerta,
    rect(x+p*29, y+p*21, p*2, p*3)
    fill(33, 33, 33)     #El pomo.
    rect(x+p*30, y+p*22, p, p)
    
    #Árboles
    fill(188, 170, 164)
        #Primer Árbol:
    rect(x+p*4, y+p*19, p, p*8)
    rect(x+p*3, y+p*21, p*3, p*2)
    rect(x+p*2, y+p*23, p*5, p*2)
        #Segundo Árbol:
    rect(x+p*11, y+p*21, p, p*8)
    rect(x+p*10, y+p*23, p*3, p*2)
    rect(x+p*9, y+p*25, p*5, p*2)
        #Tercer Árbol:
    rect(x+p*16, y+p*15, p, p*8)
    rect(x+p*15, y+p*17, p*3, p*2)
    rect(x+p*14, y+p*19, p*5, p*2)
    
    #Hielo:
    fill(0, 150, 136)
        #Primer Árbol:
    rect(x+p*3, y+p*26, p, p)
    rect(x+p*5, y+p*26, p, p)
    rect(x+p*3, y+p*27, p*3, p)
        #Segundo Árbol:
    rect(x+p*10, y+p*28, p, p)
    rect(x+p*12, y+p*28, p, p)
    rect(x+p*10, y+p*29, p*3, p)
        #Tercer Árbol:
    rect(x+p*15, y+p*22, p, p)
    rect(x+p*17, y+p*22, p, p)
    rect(x+p*15, y+p*23, p*3, p)
        #Casa:
    rect(x+p*23, y+p*20, p, p*4)
    rect(x+p*23, y+p*24, p*14, p)
    rect(x+p*36, y+p*20, p, p*4)
    
    #Nieve:
    fill(255, 255, 255)
        #Fondo.
    rect(x+p*2, y+p*6, p, p*2)
    rect(x+p*4, y+p*7, p*2, p)
    rect(x+p*36, y+p*6, p*2, p)
    rect(x+p*26, y+p*10, p*2, p)
    rect(x+p*1, y+p*13, p, p)
    rect(x+p*1, y+p*17, p, p)
    rect(x+p*3, y+p*12, p, p)
    rect(x+p*4, y+p*10, p, p)
    rect(x+p*5, y+p*9, p, p)
    rect(x+p*5, y+p*15, p, p)
    rect(x+p*8, y+p*10, p, p)
    rect(x+p*9, y+p*16, p, p)
    rect(x+p*13, y+p*11, p, p)
    rect(x+p*13, y+p*13, p, p)
    rect(x+p*18, y+p*12, p, p)
    rect(x+p*22, y+p*10, p, p)
    rect(x+p*22, y+p*18, p, p)
    rect(x+p*23, y+p*16, p, p)
    rect(x+p*26, y+p*7, p, p)
    rect(x+p*29, y+p*7, p, p)
    rect(x+p*33, y+p*8, p, p)
    rect(x+p*33, y+p*10, p, p)
    rect(x+p*34, y+p*12, p, p)
    rect(x+p*36, y +p*14, p, p)
    rect(x+p*38, y+p*17, p, p)
        #Césped:
    rect(x+p*4, y+p*29, p*2, p)
    rect(x+p*5, y+p*30, p, p)
    rect(x+p*5, y+p*32, p*2, p)
    rect(x+p*6, y+p*33, p, p)
    rect(x+p*3, y+p*36, p, p)
    rect(x+p*9, y+p*37, p*4, p)
    rect(x+p*10, y+p*31, p*2, p*3)
    rect(x+p*12, y+p*31, p*2, p)
    rect(x+p*12, y+p*33, p*2, p)
    rect(x+p*15, y+p*29, p*2, p)
    rect(x+p*18, y+p*28, p*2, p)
    rect(x+p*20, y+p*30, p*2, p)
    rect(x+p*17, y+p*35, p*2, p)
    rect(x+p*21, y+p*37, p*3, p)
    rect(x+p*15, y+p*31, p, p*2)
    rect(x+p*16, y+p*32, p, p)
    rect(x+p*23, y+p*33, p, p)
    rect(x+p*24, y+p*26, p, p)
    rect(x+p*28, y+p*26, p*2, p)
    rect(x+p*29, y+p*27, p*3, p)
    rect(x+p*28, y+p*30, p, p*2)
    rect(x+p*27, y+p*31, p, p)
    rect(x+p*37, y+p*22, p, p)
    rect(x+p*33, y+p*30, p, p*2)
    rect(x+p*32, y+p*33, p*2, p)
    rect(x+p*33, y+p*34, p, p)
        #Casa:
    rect(x+p*24, y+p*17, p*2, p)
    rect(x+p*33, y+p*17, p, p)
    rect(x+p*28, y+p*13, p, p*4)
    rect(x+p*27, y+p*14, p, p)
    rect(x+p*29, y+p*15, p*2, p)
        #Árboles:
    rect(x+p*4, y+p*18, p, p)
    rect(x+p*5, y+p*21, p, p)
    rect(x+p*2, y+p*22, p, p)
    rect(x+p*6, y+p*23, p, p)
    rect(x+p*5, y+p*24, p, p)
    rect(x+p*4, y+p*26, p, p)
    rect(x+p*11, y+p*21, p, p)
    rect(x+p*11, y+p*24, p, p)
    rect(x+p*17, y+p*16, p, p)
    rect(x+p*15, y+p*17, p, p)
    rect(x+p*16, y+p*19, p, p)
    rect(x+p*15, y+p*20, p, p)
    
               
                          
                                     
                                                           
#Sergio Bejarano Arroyo
