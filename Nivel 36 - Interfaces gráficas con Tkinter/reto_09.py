import tkinter

# VENTANA PRINCIPAL

ventana = tkinter.Tk()
ventana.title('Conversor')
ventana.geometry('400x500+700+100')
ventana.configure(bg='lightblue')

# FUNCIONES

def convertir():
    try:
        grados = entrada_grados.get()           # Recogemos los datos introducidos en el widget Entry entrada_grados.
        resultado = (float(grados) * 1.8) + 32  # Convertimos la temperatura de grados a fahrenheit.
        rotulo_resultado.config(text=resultado)
    except VelueError:
        pass

# LABEL TITULO

rotulo_titulo = tkinter.Label(ventana, text='CONVERSOR TEMPERATURAS', bg='lightblue', fg='black', font=('consolas', 20, 'bold'), relief='groove', bd=2, padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)

# FRAME PRIMERO (Esto va a funcionar como una subventana dentro de nuestra ventana principal)

cuadro1 = tkinter.Frame(ventana, bg='lightblue')    # Lo que pongamos aquí dentro aparecerá dentro de este Frame.

rotulo_celsius = tkinter.Label(cuadro1, text='Celsius:    ', bg='lightblue', font='consolas 18 bold')
rotulo_celsius.pack(side='left', padx=20, pady=20)
entrada_grados = tkinter.Entry(cuadro1, bg='white', fg='black', font=('consolas', 18, 'bold'), relief=tkinter.SUNKEN, width=10, justify=tkinter.RIGHT)       # Justificamos el texto a la derecha
entrada_grados.pack(side='left', padx=10, pady=10)

cuadro1.pack()

# FRAME SEGUNDO

cuadro2 = tkinter.Frame(ventana, bg='lightblue')

rotulo_fahrenheit = tkinter.Label(cuadro2, text='Fahrenheit: ', bg='lightblue', font='consolas 18 bold')
rotulo_fahrenheit.pack(side='left', padx=20, pady=20)
rotulo_resultado = tkinter.Label(cuadro2, text='', bg='lightgreen', font=('consolas', 18, 'bold'), width=10, relief='groove', anchor=tkinter.E)
rotulo_resultado.pack(side=tkinter.LEFT, padx=10, pady=10)

cuadro2.pack()

# FRAME TERCERO

cuadro3 = tkinter.Frame(ventana, bg='lightblue')

boton_borrar = tkinter.Button(cuadro3, text='Borrar', bg='grey', font=('consolas', 18, 'bold'), width=10)
boton_borrar.pack(side='left', padx=20, pady=20)
boton_convertir = tkinter.Button(cuadro3, text='Convertir', bg='orange', font=('consolas', 18, 'bold'), width=10, command=convertir)
boton_convertir.pack(side='left', padx=20, pady=20)

cuadro3.pack()

ventana.mainloop()
