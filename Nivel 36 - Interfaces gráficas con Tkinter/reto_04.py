import sys
import tkinter

# VENTANA DEL PROGRAMA

ventana = tkinter.Tk()

ventana.title('Mi aplicación')
'''
Al indicar la geometría podemos indicar las coordenadas de la ubicación de la ventana en pantalla, 
para que siempre se muestre en la misma posición. Para esto indicamos después de las dimensiones 
el parámetro del eje X y del eje Y separados con el signo más (+) de las dimensiones.
'''
# ventana.geometry('800x500+900+400')

'''
Para evitar la redimensión de la ventana usaríamos el siguiente código:
ventana.resizable(width=False, height=False)
también se podría poner así:
ventana.resizable(False, False)
En el caso de que queramos permitir la redimensión pondríamos True en lugar de False en el ancho o el alto.
'''

# ventana.minsize(width=400, height=250)      # Establecemos unos mínimos de redimensión
# ventana.maxsize(width=1200, height=800)     # Establecemos unos máximos de redimensión
# ventana.configure(background="grey")

# DEFINIMOS FUNCIONES

contador = 0

def cuenta_numeros():
    global contador
    contador += 1
    numero['text'] = contador

# CREACIÓN DE WIDGETS

rotulo_titulo = tkinter.Label(ventana,
                         text='CONTADOR',
                         font='consolas 20 bold',
                         # También se podría poner así: font=('consolas', 20, 'bold'))
                         background='lightgreen',
                         foreground='darkblue',
                         padx=20, pady=20,      # Espacio entre el texto y el borde del widget en píxeles
                         # width=40, height=3,  # Espacio entre el texto y el borde del widget en espacios
                         anchor='center',       # También se podría indicar así: anchor=tkinter.CENTER
                         justify='right',       # Justificación del texto, también: justify=tkinter.RIGHT
                         relief='groove',       # Borde de la etiqueta, también: relief=tkinter.RAISED
                         border=10              # Tamaño del borde
                         )
'''
En lugar de los parámetros padx y pady para los márgenes podemos usar width y height, pero en lugar 
de píxeles indicamos espacios. Hemos puesto 40 espacios en el eje X y 3 espacios en el eje Y. 
Depende del tamaño de la fuente el tamaño de los espacios del eje X e Y.
'''
rotulo_titulo.pack()

numero = tkinter.Label(ventana,
                       text='0',
                       font=('arial', 48),
                       bg='darkgreen', fg='lightblue',
                       padx=20, pady=20
                       )
numero.pack()

contar = tkinter.Button(ventana,
                        text='contar',
                        font=('arial', 18),
                        bg='lightgrey', fg='black',
                        padx=20, pady=20,
                        relief=tkinter.GROOVE, bd=10,
                        command=cuenta_numeros
                        )
contar.pack()




ventana.mainloop()
