#-----------16 horas invertidas D:

import pygame
import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective
from math import *
from FigurasYMasDeJamal import *
import time

import pygame.mixer #Para msica
# Inicializar el mixer de pygame
pygame.mixer.init()
file_path = "XDPruebadwa.mp3"  # Reemplazar con la ruta correcta
            
# IMPORT OBJECT LOADER
from objloader import *

def Agregar_Meteorito(matrizMeteoritosNave, N=1):
    global columnas
    for _ in range(N):
        posA = random.randint(0, columnas-1)
        while matrizMeteoritosNave[6][posA] == 1:
            posA = random.randint(0, 7)

        matrizMeteoritosNave[6][posA] = 2

def SufrirDaño():
    global congelar, Vida, GameOver
    Vida -= 1
    global animacionDaño
    animacionDaño = 0
    if Vida < 1:
        congelar = 1
        GameOver = 1
    else:
        pygame.mixer.music.load("Daños.mp3")
        pygame.mixer.music.play()
        animacionDaño = 4


def mover_Nave(matriz, direccion):
    for i, fila in enumerate(matriz):
        indices_unos = [j for j, valor in enumerate(fila) if valor == 1]
        for indice_uno in indices_unos:
            if direccion == 1:  # Derecha
                if indice_uno < len(fila) - 1:
                    # Verificar si hay un "2" a la derecha
                    if matriz[0][indice_uno + 1] == 2:
                        SufrirDaño()
                        matriz[0][indice_uno + 1] = 0
                    elif matriz[1][indice_uno + 1] == 2:
                        SufrirDaño()
                        matriz[1][indice_uno + 1] = 0
                    else:
                        # Mover 1 a la derecha (si es posible)
                        if matriz[i][indice_uno + 1] == 0:
                            matriz[i][indice_uno], matriz[i][indice_uno + 1] = matriz[i][indice_uno + 1], matriz[i][indice_uno]
            elif direccion == 0:  # Izquierda
                if indice_uno > 0:
                    # Verificar si hay un "2" a la izquierda
                    if matriz[0][indice_uno - 1] == 2:
                        SufrirDaño()
                        matriz[0][indice_uno - 1] = 0
                    elif matriz[1][indice_uno - 1] == 2:
                        SufrirDaño()
                        matriz[1][indice_uno - 1] = 0
                    else:
                        # Mover 1 a la izquierda (si es posible)
                        if matriz[i][indice_uno - 1] == 0:
                            matriz[i][indice_uno], matriz[i][indice_uno - 1] = matriz[i][indice_uno - 1], matriz[i][indice_uno]

def mover_Asteroide(matrizMeteoritosNave):
    global congelar, Vida, GameOver
    num_filas = len(matrizMeteoritosNave)
    num_columnas = len(matrizMeteoritosNave[0])

    # Verifica si la fila 3 Chocara con la nave
    for j in range(num_columnas):
        if matrizMeteoritosNave[1][j] == 1 and matrizMeteoritosNave[2][j] == 2:
            matrizMeteoritosNave[2][j] = 0
            SufrirDaño()

    # Convertir los valores "2" en la última fila a "0"
    for j in range(num_columnas):
        if matrizMeteoritosNave[0][j] == 2:
            matrizMeteoritosNave[0][j] = 0

    for j in range(num_columnas):
        indices_dos = [i for i in range(num_filas) if matrizMeteoritosNave[i][j] == 2]
        for indice_dos in indices_dos:
            if indice_dos > 0 and matrizMeteoritosNave[indice_dos][j] == 2:
                matrizMeteoritosNave[indice_dos][j], matrizMeteoritosNave[indice_dos - 1][j] = matrizMeteoritosNave[indice_dos - 1][j], matrizMeteoritosNave[indice_dos][j]

def Recargar_Disparos(matrizMeteoritosNave):
    global Balas
    #---------------Recargar----------------
    print("Balas")
    print(Balas)
    if Balas < 0:
        Balas += 1
        if Balas == -10:
            for i, fila in enumerate(matrizMeteoritosNave):
                for j, valor in enumerate(fila):
                    if valor == 3:
                        matrizMeteoritosNave[i][j] = 0
                        break
        elif Balas == 0:
            Balas = 1


def CrearDisparo(matrizMeteoritosNave):
    global Balas
    UbicColumna = DondeEstaLaNave(matrizMeteoritosNave)

    if Balas == 1:
        Balas = -12 #Desactivar para balas infinitas :C

        for j in range(5):
            matrizMeteoritosNave[2+j][UbicColumna] = 0

        matrizMeteoritosNave[2][UbicColumna] = 3


def DondeEstaLaNave(matriz):
    for fila in matriz:
        if 1 in fila:
            columna = fila.index(1)
            return columna
    # Si no se encuentra el valor "1" en ninguna fila, puedes manejarlo según tus necesidades
    return None

def Reiniciar(matriz):

    global columnas, animacion1
    filas = 7
    columnas = 10
    # Crear una matriz llena de ceros (puedes ajustar según tus necesidades)
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    matriz[0][4] = 1
    matriz[1][4] = 1

    Agregar_Meteorito(matriz)

    global animacion1
    animacion1 = 0
    global congelar
    global Score
    global Vida
    global GameOver
    global Balas
    Balas = 1
    GameOver = 0
    congelar = 0
    Vida = 5
    Score = 0
    global animacionDaño
    animacionDaño = 0
    animacionDaño1 = 0



def main():
    # Initialize the game engine
    pygame.init()

    # Definir las dimensiones de la matriz
    global columnas, animacion1
    filas = 7
    columnas = 10


    # Crear una matriz llena de ceros (puedes ajustar según tus necesidades)
    matrizMeteoritosNave = [[0 for _ in range(columnas)] for _ in range(filas)]
    #matrizMeteoritosNave = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
    
    matrizMeteoritosNave[0][4] = 1
    matrizMeteoritosNave[1][4] = 1

    Agregar_Meteorito(matrizMeteoritosNave)

    #print(matrizMeteoritosNave)

    size = (700, 550)
    display = size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | FULLSCREEN)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(-7, -0.5, -4)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    pygame.display.set_caption("Nave")

    Draw_Text(150, 340, 'Llevas la cura a un planeta afectado por una enfermedad letal.', 25, True)
    Draw_Text(180, 310, 'Tu misión: entregar la cura antes de que todos mueran.', 25, True)
    Draw_Text(190, 280, 'La ruta más rápida atraviesa un campo de asteroides.', 25, True)
    pygame.display.flip()

    # LOAD OBJECT AFTER PYGAME INIT
    obj = OBJ("Model_Nave/Aircraft_obj.obj", swapyz=True)
    obj.generate()
    
    
    obj2 = OBJ("Model_Roca/Rock1.obj", swapyz=True)
    obj2.generate()

    animacion1 = 0
    global congelar
    global Score
    global Vida
    global GameOver
    global Balas
    Balas = 1
    GameOver = 0
    congelar = 0
    Vida = 5
    Score = 0
    global animacionDaño
    animacionDaño = 0
    animacionDaño1 = 0

    # Definir una variable para el temporizador
    tiempo_ultimo_mover_asteroide = time.time()
    tiempo_ultimo_crear_asteroide = time.time()

    clock = pygame.time.Clock()
    while True:
        clock.tick(40) #40 Fps por segundo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            # Detectar la pulsación de tecla
            if event.type == pygame.KEYDOWN and congelar == 0:
                if event.key == pygame.K_LEFT:
                    mover_Nave(matrizMeteoritosNave, 0)
                elif event.key == pygame.K_RIGHT:
                    mover_Nave(matrizMeteoritosNave, 1)
                elif event.key == pygame.K_SPACE:
                    CrearDisparo(matrizMeteoritosNave)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    Reiniciar(matrizMeteoritosNave)

        # Verificar el temporizador para ralentizar mover_Asteroide()
        tiempo_actual = time.time() #0.35 en caso de bug
        if tiempo_actual - tiempo_ultimo_mover_asteroide >= 0.30 and congelar == 0:  # Ajusta el valor según sea necesario
            mover_Asteroide(matrizMeteoritosNave)
            Recargar_Disparos(matrizMeteoritosNave)
            tiempo_ultimo_mover_asteroide = tiempo_actual

        if tiempo_actual - tiempo_ultimo_crear_asteroide >= 2 and congelar == 0:  # Ajusta el valor según sea necesario
            Agregar_Meteorito(matrizMeteoritosNave, random.randint(2, 6))
            tiempo_ultimo_crear_asteroide = tiempo_actual - random.uniform(0.3,0.6)

        print("\n"+str(matrizMeteoritosNave))
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        #--------------------Dibujar--------------------------

        #---------------------------NAVE--------------------
        glPushMatrix()  # Guardar la matriz de modelo-vista actual
        glTranslate((DondeEstaLaNave(matrizMeteoritosNave)*0.4)+5, -1, -1)
        if animacion1 < 90:
            congelar = 1
            animacion1 += 4
            if animacion1 > 89:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                congelar = 0
                animacion1 = 90

        glRotate(-animacion1*2, 0, 0, 1)

        if animacionDaño > 0:
            animacionDaño -= 1
            if animacionDaño1 == 1:
                animacionDaño1 =0
                glRotate(10, 0, 0, 1)
            else:
                animacionDaño1 =1
                glRotate(-10, 0, 0, 1)

            if animacionDaño < 1:
                animacionDaño = 0
                animacionDaño1 = 0
                glRotate(10, 0, 0, 1)

        glScalef(0.16, 0.16, 0.16)
        obj.render()
        glPopMatrix()  # Restaurar la matriz de modelo-vista anterior


        #---------------------DIbujar Disparos------------------
        for i, fila in enumerate(matrizMeteoritosNave):
            for j, valor in enumerate(fila):
                if valor == 3:
                    y = i
                    x = j
                    glPushMatrix()  # Guardar la matriz de modelo-vista actual
                    #print(str(y)+"x: "+str(x))
                    glTranslate((x*0.4)+5, (y*1.9)-1, -1)
                    glScalef(0.02, 3, 0)
                    glColor3f(1.0, 0.0, 0.0)  # Color rojo
                    draw_cube2D()
                    glPopMatrix()  # Restaurar la matriz de modelo-vista anterior

        #---------------------DIbujar Asteroides
        for i, fila in enumerate(matrizMeteoritosNave):
            for j, valor in enumerate(fila):
                if valor == 2:
                    y = i
                    x = j
                    glPushMatrix()  # Guardar la matriz de modelo-vista actual
                    #print(coordenada)
                    glColor3f(1.0, 1.0, 1.0)  # Color blanco
                    glTranslate((x*0.4)+5, (y*0.5)-1, -1)
                    glRotate(Score, 0, 0, 1)
                    glScalef(0.10, 0.10, 0.10)
                    obj2.render()
                    glPopMatrix()  # Restaurar la matriz de modelo-vista anterior

        #---------------------DIbujar Fondo
        # Dibujar cuadrados pequeños de forma aleatoria
        for _ in range(30):  # Puedes ajustar la cantidad de cuadrados
            x = random.randint(-300, size[0]*2)  # Ajusta el rango según el tamaño del cuadrado
            y = random.randint(-300, size[1]*2)
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3f(1.0, 1.0, 1.0)  # Color blanco
            glTranslate((x*0.01)+1.7, (y*0.01)-2.8, -14)
            glScalef(0.03, 0.03, 0.03)
            draw_cube2D()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior

        if GameOver != 0:
            Draw_Text(300, 300, "Game Over", 40, True)
            Draw_Text(80, 270, "Preciona Ctrl para reintentar o Esc para salir", 40, True)
        elif congelar == 0:
            Score += 1

        ScorString = "Score: "+str(Score)
        VidaString = "Vida: "+str(int((Vida/5)*100))+"%"
        if Balas >0:
            Tiros = "Disparos: Listo"
        else:
            Tiros = "Disparos: Recargando..."

        Draw_Text(500, 340, Tiros, 29, True)
        Draw_Text(500, 370, ScorString, 40, True)
        Draw_Text(500, 400, VidaString, 40, True)


        pygame.display.flip()

if __name__ == "__main__":
    # Registra la función para que se ejecute al cerrar el programa
    main()





















"""
#!/usr/bin/env python
# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloader import *

pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

# LOAD OBJECT AFTER PYGAME INIT
obj = OBJ("Model_Nave/Aircraft_obj.obj", swapyz=True)
obj.generate()


obj2 = OBJ("Model_Roca/Rock1.obj", swapyz=True)
obj2.generate()

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False

c = 0
while 1:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # RENDER OBJECT
    glPushMatrix()  # Guardar la matriz de modelo-vista actual
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    obj.render()
    glPopMatrix()  # Restaurar la matriz de modelo-vista anterior


    c += 5
    glPushMatrix()  # Guardar la matriz de modelo-vista actual
    #glRotate(c,1,1, 1)
    glTranslate(1, 1, -10)

    obj2.render()
    glPopMatrix()  # Restaurar la matriz de modelo-vista anterior

    pygame.display.flip()

"""