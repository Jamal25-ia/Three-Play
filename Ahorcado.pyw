
#!/usr/bin/env python
# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame
import random
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from objloaderAhorcado import *
from FigurasYMasDeJamalAh import *
import time


# Lista de palabras
palabras = ["PYTHON", "JUEGO", "AHORCADO", "PROGRAMACION", "COMPUTADORA", "VIDEOJUEGO", "PYGAME", "COMIDA", "ARBOL", "AGUA"]

def IniciarJuego():
    global palabra_secreta, intentos, letras_adivinadas
    palabra_secreta = random.choice(palabras)
    intentos = 0
    letras_adivinadas = set()

def main():
    # Initialize the game engine
    pygame.init()

    size = (700, 550)
    display = size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | FULLSCREEN)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -7)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    pygame.display.set_caption("Ahorcado")

    Draw_Text(0, 340, 'Estas perdido en el medio del bosque sin comida y tras 3 dias de vagar sin llegar a la civilizacion.', 20, True)
    Draw_Text(0, 320, 'Empiezas a pensar en suicidarte con la cuerda en las manos encuentras un poste conveniente para colgarte.', 20, True)
    Draw_Text(0, 300, 'Tu misión: Evita que se suicide.', 20, True)
    pygame.display.flip()

    time.sleep(20)
    # LOAD OBJECT AFTER PYGAME INIT
    obj = OBJ("EscenarioModel/Verde.obj", swapyz=True)
    obj.generate()
    obj2 = OBJ("EscenarioModel/Marron.obj", swapyz=True)
    obj2.generate()
    Descuartizado1 = OBJ("EscenarioModel/cuerpo1.obj", swapyz=True)
    Descuartizado1.generate()
    Descuartizado2 = OBJ("EscenarioModel/cuerpo2.obj", swapyz=True)
    Descuartizado2.generate()
    Cabeza = OBJ("EscenarioModel/Cabeza.obj", swapyz=True)
    Cabeza.generate()
    Descuartizado3 = OBJ("EscenarioModel/cuerpo3.obj", swapyz=True)
    Descuartizado3.generate()
    Descuartizado4 = OBJ("EscenarioModel/cuerpo4.obj", swapyz=True)
    Descuartizado4.generate()
    Descuartizado5 = OBJ("EscenarioModel/cuerpo5.obj", swapyz=True)
    Descuartizado5.generate()
    Descuartizado6 = OBJ("EscenarioModel/cuerpo6.obj", swapyz=True)
    Descuartizado6.generate()
    Descuartizado7 = OBJ("EscenarioModel/cuerpo7.obj", swapyz=True)
    Descuartizado7.generate()

    clock = pygame.time.Clock()


    glRotate(90, 0, 1, 0)
    glRotate(180, 1, 0, 0)
    glRotate(90, 1, 0, 0)
    glRotate(90, 0, 0, 1)

    glScalef(0.13, 0.13, 0.13)
    #glTranslatef(0, 0, 0) #Traslacion
    global palabra_secreta, intentos, letras_adivinadas
    IniciarJuego()

    MaximoIntentos = 8 #Constante NO tocar
    while True:
        clock.tick(40) #40 Fps por segundo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letra = chr(event.key).upper()
                    if letra not in letras_adivinadas:
                        letras_adivinadas.add(letra)
                        if letra not in palabra_secreta:
                            intentos += 1
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    IniciarJuego()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        #--------------------Dibujar--------------------------


        #---------------------------VERDE DE --------------------
        glPushMatrix()  # Guardar la matriz de modelo-vista actual
        glColor3fv((0, 1, 0))  # Color verde
        obj.render()
        glPopMatrix()  # Restaurar la matriz de modelo-vista anterior



        #---------------------------Marron--------------------
        glPushMatrix()  # Guardar la matriz de modelo-vista actual
        glColor3fv((0.6, 0.4, 0.2))  # Marrón
        obj2.render()
        glPopMatrix()  # Restaurar la matriz de modelo-vista anterior


        #----------Texto-


        # Lógica del juego
        palabra_mostrada = "".join([letra if letra in letras_adivinadas else " _" for letra in palabra_secreta])

        # Generar el texto con guiones
        Draw_Text(150, 150, f"Adivina la palabra: {palabra_mostrada}", 30, True)

        
        texto_adivinanza = f"Intentos restantes: {max(0, MaximoIntentos - intentos)}"
        Draw_Text(150, 100, texto_adivinanza, 25, True)


        #-Dibujar cuerpo:

        # Dibujar ahorcado
        if intentos > 0:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((0.6, 0.4, 0.2))  # Marrón
            Descuartizado1.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 1:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((0.6, 0.4, 0.2))  # Marrón
            Descuartizado2.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 2:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((1.0, 0.8, 0.6)) #Piel brazo
            Cabeza.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 3:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((1.0, 0.8, 0.6)) #Piel brazo
            Descuartizado3.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 4:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((1.0, 0.8, 0.6)) #Piel Brazo
            Descuartizado4.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 5:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((0.6, 0.8, 1.0))  # azul
            Descuartizado5.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 6:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((0.6, 0.8, 1.0))  # azul
            Descuartizado6.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
        if intentos > 7:
            glPushMatrix()  # Guardar la matriz de modelo-vista actual
            glColor3fv((0.6, 0.8, 1.0))  # azul
            Descuartizado7.render()
            glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
    

        # Mostrar mensaje de victoria o derrota
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            Draw_Text(200, 500, "Has Ganado", 20, True)
            Draw_Text(200, 450, "Preciona Ctrl para volver a jugar o Esc para salir", 20, True)
        elif intentos >= MaximoIntentos:
            Draw_Text(200, 500, f"¡Has perdido! La palabra era {palabra_secreta}", 20, True)
            Draw_Text(200, 450, "Preciona Ctrl para reintentar o Esc para salir", 20, True)


        pygame.display.flip()

if __name__ == "__main__":
    # Registra la función para que se ejecute al cerrar el programa
    main()