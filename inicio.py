import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import sys
import os

def ejecutar_juego(juego):
    # Reemplaza 'ruta_al_juego.py' con la ruta real al script del juego
    
    if juego == "Tetris":
        #pygame.quit()
        ruta_absoluta = os.path.abspath("Tetris +Ecualizador.pyw")
        os.startfile(ruta_absoluta)
        #sys.exit()
    elif juego == "Ahorcado":
        ruta_absoluta = os.path.abspath("Ahorcado.pyw")
        os.startfile(ruta_absoluta)
        #sys.exit()
    elif juego == "The Ship":
        ruta_absoluta = os.path.abspath("Nave.pyw")
        os.startfile(ruta_absoluta)
        #sys.exit()

#
#LaNave

def seleccionar_juego(juego):
    #label_juego.config(text=f"Juego seleccionado: {juego}")
    mostrar_mensaje_carga()
    ejecutar_juego(juego)


def mostrar_mensaje_carga():
    label_juego.config(text=f"Cargando...")
    ventana.update()
    # Esperar 30 segundos
    ventana.after(20000, quitar_mensaje_carga)

def quitar_mensaje_carga():
    label_juego.config(text="")
    ventana.update()

def salir():
    sys.exit()

def mostrar_controles():
    texto_controles = "Controles Tetris:\n\n" \
                      "Mover: derecha, abajo, izquierda\n" \
                      "Rotar: arriba\n" \
                      "Caer Rápido: Espacio\n" \
                      "Salir: Esc\n" \
                      "Reintentar: Ctrl\n\n\n\n"\
                      "Controles Ahorcado:\n\n" \
                      "Letras: A-z\n" \
                      "Salir: Esc\n" \
                      "Reintentar: Ctrl\n\n\n\n" \
                      "Controles Nave:\n\n" \
                      "Mover: A, D\n" \
                      "Disparar: Espacio\n" \
                      "Salir: Esc\n" \
                      "Reintentar: Ctrl\n"

    # Crear una ventana emergente con el texto de los controles
    messagebox.showinfo("Ayuda", texto_controles)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Selector de Juegos")
# Configuración para pantalla completa
ventana.attributes('-fullscreen', True)


# Configuración del fondo
# Reemplaza 'ruta_a_tu_imagen.jpg' con la ruta real de tu imagen de fondo
ruta_imagen = 'incioF.png'
imagen = Image.open(ruta_imagen)
imagen_fondo = ImageTk.PhotoImage(imagen)

# Agregar un Canvas en lugar de un Label
canvas = tk.Canvas(ventana, bg='black', width=ventana.winfo_screenwidth(), height=ventana.winfo_screenheight())
canvas.pack()

# Obtener las dimensiones de la imagen
ancho_imagen, alto_imagen = imagen.size

# Calcular la posición para centrar la imagen
posicion_x = (ventana.winfo_screenwidth() - ancho_imagen) // 2
posicion_y = (ventana.winfo_screenheight() - alto_imagen) // 2

# Agregar la imagen al Canvas en la posición centrada
canvas.create_image(posicion_x, posicion_y, anchor=tk.NW, image=imagen_fondo)

"""
# Configuración del marco para centrar elementos
marco_centro = tk.Frame(ventana, bg='#2c3171')
marco_centro.place(relx=0.5, rely=0.54, anchor=tk.CENTER, relwidth=0.25, relheight=0.26)
"""

# Cambia el color del texto aquí
color_texto = 'yellow'  # Cambia este valor al color deseado

# Configuración del menú
#opciones_juegos = ['Tetris', 'Ahorcado', 'LaNave']
"""
menu_label = tk.Label(marco_centro, text="Seleccione el juego que desea ejecutar", font=('Helvetica', 11), bg='#2c3171', fg=color_texto)
menu_label.pack(pady=10)
"""
# Cambia el color de fondo de los botones aquí
color_boton = 'yellow'  # Cambia este valor al color deseado


# Agregar botónes de juegos
boton1 = tk.Button(ventana, text='Tetris', command=lambda j='Tetris': seleccionar_juego(j), font=('Helvetica', 10), bg=color_boton)
boton1.place(relx=0.38, rely=0.95, anchor=tk.SE)
boton2 = tk.Button(ventana, text='Ahorcado', command=lambda j='Ahorcado': seleccionar_juego(j), font=('Helvetica', 10), bg=color_boton)
boton2.place(relx=0.38+0.08, rely=0.95, anchor=tk.SE)
boton3 = tk.Button(ventana, text='The Ship', command=lambda j='The Ship': seleccionar_juego(j), font=('Helvetica', 10), bg=color_boton)
boton3.place(relx=0.38+(0.08*2), rely=0.95, anchor=tk.SE)

# Crear un botón que mostrará los controles al hacer clic
boton_controles = tk.Button(ventana, text="Controles", command=mostrar_controles, font=('Helvetica', 10), bg=color_boton)
boton_controles.place(relx=0.38+(0.08*3), rely=0.95, anchor=tk.SE)
#boton_controles.place(relx=0.53, rely=0.48, anchor=tk.SE)

# Agregar botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir, font=('Helvetica', 10), bg=color_boton)
boton_salir.place(relx=0.38+(0.074*4), rely=0.95, anchor=tk.SE)


# Etiqueta para mostrar el juego seleccionado
label_juego = tk.Label(ventana, text="", font=('Helvetica', 12), bg='lightgray')
label_juego.place(relx=0.5, rely=0.63, anchor=tk.SE)


ventana.mainloop()
