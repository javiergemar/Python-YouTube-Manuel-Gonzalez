import sys
import tkinter

# VENTANA DEL PROGRAMA

ventana = tkinter.Tk()

ventana.title('Mi aplicación')

# DEFINIMOS FUNCIONES

def cuenta_numeros():
    contador = int(numero['text'])              # Lo convertimos a tipo int, ya que está declarado como string.
    contador += 1
    numero['text'] = contador                   # También se podría poner así: numero.config(text=contador)

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

rotulo_titulo.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20, ipadx=20, ipady=20)

numero = tkinter.Label(ventana,
                       text='0',
                       # Podríamos definir también text=0 (directamente como int) y no necesitamos hacer la conversión.
                       font=('arial', 48),
                       bg='darkgreen', fg='lightblue'
                       )
numero.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20, ipadx=20, ipady=20)

contar = tkinter.Button(ventana,
                        text='Contar',
                        font=('arial', 18),
                        bg='lightgrey', fg='black',
                        padx=20, pady=20,
                        relief=tkinter.GROOVE, bd=10,
                        command=cuenta_numeros
                        )
contar.pack(fill=tkinter.BOTH, expand=True, padx=20, pady=20, ipadx=20, ipady=20)

# BUCLE PRINCIPAL

ventana.mainloop()
