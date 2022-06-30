import tkinter as tk

# VENTANA DEL PROGRAMA

ventana = tk.Tk()

ventana.title('Mi aplicación')
'''
Al indicar la geometría podemos indicar las coordenadas de la ubicación de la ventana en pantalla, 
para que siempre se muestre en la misma posición. Para esto indicamos después de las dimensiones 
el parámetro del eje X y del eje Y separados con el signo más (+) de las dimensiones.
'''
ventana.geometry('800x500+900+400')

'''
Para evitar la redimensión de la ventana usaríamos el siguiente código:
ventana.resizable(width=False, height=False)
también se podría poner así:
ventana.resizable(False, False)
En el caso de que queramos permitir la redimensión pondríamos True en lugar de False en el ancho o el alto.
'''

ventana.minsize(width=400, height=250)      # Establecemos unos mínimos de redimensión
ventana.maxsize(width=1200, height=800)     # Establecemos unos máximos de redimensión
ventana.configure(background="grey")

# CREACIÓN DE WIDGETS

rotulo = tk.Label(ventana,
                  text='TÍTULO DE LA APLICACIÓN\nEN TKINTER',
                  font='consolas 20 bold',
                  # También se podría poner así: font=('consolas', 20, 'bold'))
                  background='lightblue',
                  foreground='red',
                  #padx=40, pady=20,        # Espacio entre el texto y el borde del widget en píxeles
                  width=40, height=3,       # Espacio entre el texto y el borde del widget en espacios
                  anchor='center',          # También se podría indicar así: anchor=tk.CENTER
                  justify='right',          # Justificación del texto, también: justify=tk.RIGHT
                  relief='groove',          # Borde de la etiqueta, también: relief=tk.RAISED
                  border=10                 # Tamaño del borde
                  )
'''
En lugar de los parámetros padx y pady para los márgenes podemos usar width y height, pero en lugar 
de píxeles indicamos espacios. Hemos puesto 40 espacios en el eje X y 3 espacios en el eje Y. 
Depende del tamaño de la fuente el tamaño de los espacios del eje X e Y.
'''
rotulo.pack()


ventana.mainloop()

