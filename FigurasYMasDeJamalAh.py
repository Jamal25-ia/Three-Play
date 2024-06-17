import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective
from math import *

def Draw_Text(x, y, Text, Tamaño, SinFondo):
    font = pygame.font.SysFont('arial', Tamaño)

    if SinFondo == False:
        textSurface = font.render(Text, True, (0, 0, 255, 255), (0, 66, 0, 255)) #Fondo Verde feo
    else:
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        textSurface = font.render(Text, True, (0, 0, 255, 255)).convert_alpha()
        
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)

def draw_pyramidColor(size=1.0, R=0,G=0,A=0):
    glColor3f(R,G,A)  # Rojo
    return draw_pyramid(size=1.0)

def draw_pyramid(size=1.0):

    half_size = size / 2.0
    height = size * 0.5  # Ajusta la altura según sea necesario

    glBegin(GL_TRIANGLES)
    
    # Base
    glVertex3f(-half_size, 0, -half_size)
    glVertex3f(half_size, 0, -half_size)
    glVertex3f(half_size, 0, half_size)
    
    glVertex3f(-half_size, 0, -half_size)
    glVertex3f(half_size, 0, half_size)
    glVertex3f(-half_size, 0, half_size)
    
    # Caras laterales
    glVertex3f(-half_size, 0, -half_size)
    glVertex3f(half_size, 0, -half_size)
    glVertex3f(0, height, 0)
    
    glVertex3f(half_size, 0, -half_size)
    glVertex3f(half_size, 0, half_size)
    glVertex3f(0, height, 0)
    
    glVertex3f(half_size, 0, half_size)
    glVertex3f(-half_size, 0, half_size)
    glVertex3f(0, height, 0)
    
    glVertex3f(-half_size, 0, half_size)
    glVertex3f(-half_size, 0, -half_size)
    glVertex3f(0, height, 0)
    
    glEnd()

def draw_sphere(radius, slices, stacks):
    for i in range(stacks):
        lat0 = pi * (-0.5 + (i / stacks))
        lat1 = pi * (-0.5 + ((i + 1) / stacks))

        for j in range(slices):
            lon0 = 2 * pi * (j / slices)
            lon1 = 2 * pi * ((j + 1) / slices)

            x0 = radius * cos(lon0) * cos(lat0)
            y0 = radius * sin(lon0) * cos(lat0)
            z0 = radius * sin(lat0)

            x1 = radius * cos(lon1) * cos(lat0)
            y1 = radius * sin(lon1) * cos(lat0)
            z1 = radius * sin(lat0)

            x2 = radius * cos(lon0) * cos(lat1)
            y2 = radius * sin(lon0) * cos(lat1)
            z2 = radius * sin(lat1)

            x3 = radius * cos(lon1) * cos(lat1)
            y3 = radius * sin(lon1) * cos(lat1)
            z3 = radius * sin(lat1)

            glBegin(GL_QUADS)
            glVertex3f(x0, y0, z0)
            glVertex3f(x1, y1, z1)
            glVertex3f(x3, y3, z3)
            glVertex3f(x2, y2, z2)
            glEnd()

def draw_cylinder(radius, height, slices):
    for i in range(slices):
        angle0 = 2 * pi * (i / slices)
        angle1 = 2 * pi * ((i + 1) / slices)

        x0 = radius * cos(angle0)
        y0 = radius * sin(angle0)
        x1 = radius * cos(angle1)
        y1 = radius * sin(angle1)

        glBegin(GL_QUADS)
        glVertex3f(x0, y0, 0)
        glVertex3f(x1, y1, 0)
        glVertex3f(x1, y1, height)
        glVertex3f(x0, y0, height)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex3f(x0, y0, 0)
        glVertex3f(x1, y1, 0)
        glVertex3f(0, 0, 0)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex3f(x0, y0, height)
        glVertex3f(x1, y1, height)
        glVertex3f(0, 0, height)
        glEnd()

def draw_cube2D():
    glBegin(GL_QUADS)
    glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1, -1)
    glVertex3f( 1,  1, -1)
    glVertex3f(-1,  1, -1)
    glEnd()

def draw_cube(size=1.0):
    glBegin(GL_QUADS)
    glVertex3f(-size, -size, -size)
    glVertex3f( size, -size, -size)
    glVertex3f( size,  size, -size)
    glVertex3f(-size,  size, -size)
    
    glVertex3f(-size, -size,  size)
    glVertex3f( size, -size,  size)
    glVertex3f( size,  size,  size)
    glVertex3f(-size,  size,  size)
    
    glVertex3f(-size, -size, -size)
    glVertex3f( size, -size, -size)
    glVertex3f( size, -size,  size)
    glVertex3f(-size, -size,  size)
    
    glVertex3f(-size,  size, -size)
    glVertex3f( size,  size, -size)
    glVertex3f( size,  size,  size)
    glVertex3f(-size,  size,  size)
    
    glVertex3f(-size, -size, -size)
    glVertex3f(-size,  size, -size)
    glVertex3f(-size,  size,  size)
    glVertex3f(-size, -size,  size)
    
    glVertex3f( size, -size, -size)
    glVertex3f( size,  size, -size)
    glVertex3f( size,  size,  size)
    glVertex3f( size, -size,  size)
    glEnd()


def draw_cubeTexturizado3D(size=1.0, texture=None, color = (1,1,1)):
    if texture:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)

    glColor3f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)

    glBegin(GL_QUADS)

    # Cara frontal
    glTexCoord2f(0, 0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1)
    glVertex3f(size, size, -size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, -size)

    # Cara posterior
    glTexCoord2f(1, 0)
    glVertex3f(-size, -size, size)
    glTexCoord2f(1, 1)
    glVertex3f(-size, size, size)
    glTexCoord2f(0, 1)
    glVertex3f(size, size, size)
    glTexCoord2f(0, 0)
    glVertex3f(size, -size, size)

    # Cara superior
    glTexCoord2f(0, 1)
    glVertex3f(-size, size, -size)
    glTexCoord2f(0, 0)
    glVertex3f(size, size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(size, size, size)
    glTexCoord2f(1, 1)
    glVertex3f(-size, size, size)

    # Cara inferior
    glTexCoord2f(1, 1)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(0, 1)
    glVertex3f(-size, -size, size)
    glTexCoord2f(0, 0)
    glVertex3f(size, -size, size)
    glTexCoord2f(1, 0)
    glVertex3f(size, -size, -size)

    # Cara lateral izquierda
    glTexCoord2f(0, 1)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(0, 0)
    glVertex3f(-size, size, -size)
    glTexCoord2f(1, 0)
    glVertex3f(-size, size, size)
    glTexCoord2f(1, 1)
    glVertex3f(-size, -size, size)

    # Cara lateral derecha
    glTexCoord2f(1, 1)
    glVertex3f(size, -size, -size)
    glTexCoord2f(0, 1)
    glVertex3f(size, -size, size)
    glTexCoord2f(0, 0)
    glVertex3f(size, size, size)
    glTexCoord2f(1, 0)
    glVertex3f(size, size, -size)

    glEnd()

    if texture:
        glDisable(GL_TEXTURE_2D)

def draw_Murcielago():
    glBegin(GL_POINTS)
    glVertex3f(0, 0, 0)
    glVertex3f(-1, -0.5, 0)
    glVertex3f(-1.2, -0.8, 0)
    glVertex3f(-2, -0.4, 0)
    glVertex3f(-2.2, -0.6, 0)
    glVertex3f(1, -0.5, 0)
    glVertex3f(1.2, -0.8, 0)
    glVertex3f(2, -0.4, 0)
    glVertex3f(2.2, -0.6, 0)
    glVertex3f(-0.5, -1, 0)
    glVertex3f(0.5, -1, 0)
    glVertex3f(0, -1.4, 0)
    glEnd()


def draw_textured_cube():
    glBegin(GL_QUADS)
    
    # Front face
    glTexCoord2f(1, 1); glVertex3f(-1, -1,  -1)
    glTexCoord2f(0, 1); glVertex3f( 1, -1,  -1)
    glTexCoord2f(0, 0); glVertex3f( 1,  1,  -1)
    glTexCoord2f(1, 0); glVertex3f(-1,  1,  -1)

    glEnd()
    
def draw_cubeTextura(size=1.0, Activar3D = True):
    glBegin(GL_QUADS)

    # Cara frontal
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-size, -size, -size)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(size, -size, -size)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(size, size, -size)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-size, size, -size)

    if Activar3D == True:
        # Cara posterior
        glTexCoord2f(0.0, 0.0)
        glVertex3f(size, -size, size)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-size, -size, size)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-size, size, size)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(size, size, size)

        # Cara izquierda
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-size, -size, size)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-size, -size, -size)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-size, size, -size)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-size, size, size)

        # Cara derecha
        glTexCoord2f(0.0, 0.0)
        glVertex3f(size, -size, -size)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(size, -size, size)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(size, size, size)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(size, size, -size)

        # Cara superior
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-size, size, -size)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(size, size, -size)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(size, size, size)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-size, size, size)

        # Cara inferior
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-size, -size, size)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(size, -size, size)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(size, -size, -size)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-size, -size, -size)
    
    glEnd()
"""--------------------------Documentacion---------------

GL_POINTS: Para dibujar puntos.
glPointSize(5.0)
GL_LINES: Para dibujar líneas.
GL_POLYGON: Para dibujar polígonos.
GL_TRIANGLES: Para dibujar triángulos.
GL_TRIANGLE_STRIP: Dibuja una tira de triángulos conectados. Cada nuevo vértice define un nuevo triángulo junto con los dos últimos vértices
GL_TRIANGLE_FAN: Dibuja triángulos conectados a un vértice central. Cada nuevo vértice junto con el vértice central forma un nuevo triángulo.
GL_LINE_STRIP: Para dibujar una tira de líneas conectadas.
GL_LINE_LOOP: Similar a GL_LINE_STRIP, pero con el último punto conectado al primero.
GL_QUADS: Para dibujar cuadriláteros.
GL_QUAD_STRIP: Para dibujar una tira de cuadriláteros conectados.


Transformaciones:
glTranslatef(x, y, z) #Traslacion
glRotatef(angle, x, y, z) #Rotar glRotatef(45.0, 0.0, 1.0, 0.0)  # Rotación de 45 grados alrededor del eje y
glScalef(x, y, z) #Escalar

Camara:
Mira de camara:
gluLookAt(eyeX,eyeY,eyeZ, CenterX, CenterY, CenterZ, upX, upY, upZ)
ejemplo:
gluLookAt(0,0,3, 0,0,0, 0,1,0)


Descripción: Define una proyección ortográfica, donde los objetos se ven del mismo tamaño sin importar su distancia.
Parámetros:
left, right: Coordenadas x del plano de la vista izquierda y derecha.
bottom, top: Coordenadas y del plano de la vista inferior y superior.
near, far: Distancia del plano de la vista cercano y lejano.
glOrtho(left, right, bottom, top, near, far):
glOrtho(-1.0, 1.0, -1.0, 1.0, 0.1, 100.0)

Descripción: Define una proyección en perspectiva truncada (frustum), donde los objetos más cercanos son más grandes que los objetos más lejanos.
Parámetros:
left, right: Coordenadas x del plano de la vista izquierda y derecha.
bottom, top: Coordenadas y del plano de la vista inferior y superior.
near, far: Distancia del plano de la vista cercano y lejano.
glFrustum(left, right, bottom, top, near, far):
glFrustum(-1.0, 1.0, -1.0, 1.0, 1.0, 100.0)

Descripción: Define una proyección en perspectiva, donde los objetos más cercanos son más grandes que los objetos más lejanos.
Parámetros:
fovy: Campo de visión en grados en la dirección y.
aspect: Relación de aspecto (ancho/altura).
zNear, zFar: Distancia del plano de la vista cercano y lejano.
gluPerspective(fovy, aspect, zNear, zFar):
gluPerspective(45.0, (width/height), 0.1, 100.0)


----------------------------Matrices:----------------

glLoadIdentity() #Elimina cualquier transformación previa. Puedes usarlo para comenzar una nueva serie de transformaciones.
glPopMatrix()  # Restaurar la matriz de modelo-vista anterior
glPushMatrix()  # Guardar la matriz de modelo-vista actual





-------- ----------------Documentacion LUZ----------


Hay varias configuraciones que puedes ajustar para la iluminación en OpenGL. Algunas de las configuraciones más comunes son:

Intensidad de la Luz:
Puedes ajustar la intensidad de la luz modificando los componentes de difusión y especular. Por ejemplo, puedes hacer que la luz sea más intensa cambiando los valores en GL_DIFFUSE y GL_SPECULAR a valores más altos (por ejemplo, (1.0, 1.0, 1.0, 1.0)).

python
Copy code
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))  # Difusión más intensa
glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))  # Especular más intenso
Color de la Luz:
Además de la intensidad, también puedes cambiar el color de la luz ajustando los componentes de difusión y especular.

python
Copy code
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))  # Luz difusa gris
glLightfv(GL_LIGHT0, GL_SPECULAR, (0.8, 0.8, 0.8, 1.0))  # Luz especular gris
Atenuación de la Luz:
Puedes simular la atenuación de la luz con la distancia ajustando los parámetros de atenuación. Esto puede hacer que la luz sea más intensa cerca de la fuente de luz y se atenúe a medida que se aleja.

python
Copy code
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.02)
glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.01)
Puedes experimentar con los valores para obtener el efecto deseado.

Dirección de la Luz (para luces direccionales):
Si estás utilizando una luz direccional en lugar de una luz puntual, también puedes establecer la dirección de la luz.

python
Copy code
glLightfv(GL_LIGHT0, GL_POSITION, (1.0, 1.0, 1.0, 0.0))  # Último componente 0 para luz direccional
Tipo de Luz:
Puedes cambiar el tipo de luz entre luz puntual, direccional y spotlight. Ajusta el último componente de la posición de la luz para cambiar entre ellos.

python
Copy code
# Luz puntual
glLightfv(GL_LIGHT0, GL_POSITION, (1.0, 1.0, -5.0, 1.0))

# Luz direccional
glLightfv(GL_LIGHT0, GL_POSITION, (1.0, 1.0, 1.0, 0.0))

# Spotlight
glLightfv(GL_LIGHT0, GL_POSITION, (1.0, 1.0, -5.0, 1.0))
glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, (-1.0, -1.0, 1.0))
glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 30.0)  # Ángulo del cono de la spotlight
----------------------------


"""
