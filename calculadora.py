from tkinter import *

raiz = Tk()

raiz.iconbitmap("bichi.ico")

miFrame = Frame(raiz)

miFrame.pack()

operacion = ""
resultado = 0


#----------------Pantalla--------------------------------------#

numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#------------pulsaciones teclado----------------------------------

def numeroPulsado(Num):
    global operacion

    if operacion != "":
        numeroPantalla.set(Num)
        operacion = ""

    else:
        numeroPantalla.set(numeroPantalla.get() + Num)



#--------------------funcion suma___________________________________

def suma(num):
    global operacion
    global resultado

    resultado += int(num)

    operacion = "suma"

    numeroPantalla.set(resultado)



#-------------------funcion el_resultado_______________________________

def el_resultado():
    global resultado

    numeroPantalla.set(resultado + int(numeroPantalla.get()))
    resultado = 0

#------------Fila 1---------------------------------------------------#

boton_ = Button(miFrame, text=" ", width=3)
boton_.grid(row=2, column=1)

botonper = Button(miFrame, text="%", width=3)
botonper.grid(row=2, column=2)

erase = Button(miFrame, text="del", width=3)
erase.grid(row=2, column=3)

botondiv = Button(miFrame, text="/", width=3)
botondiv.grid(row=2, column=4)



#------------Fila 2---------------------------------------------------#

boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=3, column=1)

boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=3, column=2)

boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=3, column=3)

botonMult = Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)


#------------Fila 2---------------------------------------------------#

boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=4, column=1)

boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=4, column=2)

boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=4, column=3)

botonMenos = Button(miFrame, text="-", width=3)
botonMenos.grid(row=4, column=4)

#---------------------Fila 3 -----------------------



boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=5, column=1)

boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=5, column=2)

boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=5, column=3)

botonMas = Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
botonMas.grid(row=5, column=4)

#--------------------Fila 4-----------------------------

boton00 = Button(miFrame, text="00", width=3, command=lambda: numeroPulsado("00"))
boton00.grid(row=6, column=1)

boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=6, column=2)

botonpunto = Button(miFrame, text=".", width=3, command=lambda: numeroPulsado("."))
botonpunto.grid(row=6, column=3)

botonIgual = Button(miFrame, text="=", width=3, command=lambda : el_resultado())
botonIgual.grid(row=6, column=4)

raiz.mainloop()

