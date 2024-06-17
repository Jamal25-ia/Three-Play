"""
#-----------------------------Musica---------
import pygame.mixer #Para msica
# Inicializar el mixer de pygame
pygame.mixer.init()

# Cargar la canción
pygame.mixer.music.load("Y2meta.app - GTA San Andreas Theme Song (REMIX) 2023 (128 kbps).mp3")

# Reproducir en bucle
pygame.mixer.music.play(-1)
"""
#-----------------------------Musica-----Fin----

"""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLU import gluPerspective
from scipy.io.wavfile import read
from numpy import fft
import sys
import time
import pygame, sys, time
from pygame.locals import *

file_path = "GTA.wav"  # Reemplazar con la ruta correcta


def main():
    width, height = 420, 360

    frame_rate, amplitude = read(file_path)
    frame_skip = 96
    amplitude = amplitude[:, 0] + amplitude[:, 1]
    amplitude = amplitude[::frame_skip]
    frequency = list(abs(fft.fft(amplitude)))

    max_amplitude = max(amplitude)
    for i in range(len(amplitude)):
        amplitude[i] = float(amplitude[i]) / max_amplitude * height / 4 + height / 2
    amplitude = [int(height / 2)] * width + list(amplitude)

    pygame.init()
    display = (width, height)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    now = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        # Dibuja la visualización de la onda de audio
        for i in range(len(amplitude[width:])):

            prev_x, prev_y = 0, amplitude[i]
            for x, y in enumerate(amplitude[i + 1:i + 1 + width][::5]):
                y = y-180
                x = x*0.08
                glColor3f(0, 1, 0)
                glBegin(GL_LINES)
                glVertex2f(prev_x * 5, prev_y)
                glVertex2f(x * 5, y)
                glVertex2f((prev_x * 5 - width / 2) * -1 + width / 2, prev_y)
                glVertex2f((x * 5 - width / 2) * -1 + width / 2, y)
                glEnd()
                prev_x, prev_y = x, y

            while time.time() < now + 1.0 / frame_rate * frame_skip:
                time.sleep(.00000000001)
            now = time.time()

            pygame.display.flip()

if __name__ == '__main__':
    main()





"""

#_-----------------------------GOD
file_path = "GTA.wav"  # Reemplazar con la ruta correcta

from scipy.io.wavfile import read
from random import randint
from numpy import fft
import pygame, sys, time
import ctypes

def main():
    
    #graphic interface dimensions
    width, height = 420, 500
    center = [width/2, height/2]
    
    #read amplitude and frequency of music file with defined frame skips
    frame_rate, amplitude = read(file_path)
    frame_skip =600
    amplitude = amplitude[:,0] + amplitude[:,1]
    amplitude = amplitude[::frame_skip]
    frequency = list(abs(fft.fft(amplitude)))
    
    #scale the amplitude to 1/4th of the frame height and translate it to height/2(central line)
    max_amplitude = max(amplitude)
    for i in range(len(amplitude)):
        amplitude[i] = float(amplitude[i])/max_amplitude*height/4 + height/2
    amplitude = [int(height/2)]*width + list(amplitude)


    # Cargar la imagen de fondo
    background_image = pygame.image.load("Sprites//FondoEcualizador.jpeg")  # Reemplaza con la ruta correcta de tu imagen
    background_image = pygame.transform.scale(background_image, (width, height))

    #initiate graphic interface and play audio piece
    pygame.init()
    screen=pygame.display.set_mode([width, height], pygame.NOFRAME)
    # Establecer la posición de la ventana
    ctypes.windll.user32.SetProcessDPIAware()
    Y = 50
    X = 0
    ctypes.windll.user32.SetWindowPos(pygame.display.get_wm_info()['window'], -1, X, Y, 0, 0, 0x0001)

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)
    now = time.time()   
    
    #visualizer animation starts here
    for i in range(len(amplitude[width:])):
        
        #screen.fill([0, 0, 0])
        screen.blit(background_image, (0, 0))  # Dibujar la imagen de fondo

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        try:
            #circular animation: radius of circle depends on magnitude amplitude and color of circle depends on frequency
            try:
                pygame.draw.circle(screen, [0%255, 0%255, 0%255], center, amplitude[i], 3)
            except ValueError:
                pass
            
            #the amplitude graph is being translated from both left and right creating a mirror effect
            prev_x, prev_y = 0, amplitude[i]
            for x, y in enumerate(amplitude[i+1:i+1+width][::5]):
                pygame.draw.line(screen, [0, 0, 0], [prev_x*5, prev_y], [x*5, y], 2)
                pygame.draw.line(screen, [0, 0, 0], [(prev_x*5-width/2)*-1+width/2, prev_y], [(x*5-width/2)*-1+width/2, y], 2)
                prev_x, prev_y = x, y
        
            #time delay to control frame refresh rate
            while time.time()<now+ 1.0000000000/frame_rate*frame_skip:
                time.sleep(.00000000001)
            now = time.time()
        
            pygame.display.flip()

        except ValueError:
            print(ValueError)
            pass

if __name__ == '__main__':
    main()
