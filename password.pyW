from tkinter import *
import random
import string
import clipboard


raiz = Tk()
raiz.title("PasswordsCreatorG57")
raiz.resizable(0, 0) 

def Copy(contraseña):
    clipboard.copy(contraseña)


def CrearPassword():

    charactersforPassword = 18
    contraseña = ''
    caracteres = list(string.printable)
    caracteresDisponibles = caracteres[:-6]

    for i in range(charactersforPassword):
        contraseña += random.choice(caracteresDisponibles)

    textoV.set(f"Tu contraseña es: {contraseña}")


    botonCopy = Button(miFrame, text = "Copy", fg = "white", bg = "green", font = ("System-UI", 10,  "bold"), command = Copy(contraseña)) 
    botonCopy.grid(row = 3, column = 0, pady = 10, padx = 10)





miFrame = Frame(raiz, width = 500, height = 400)
miFrame.pack()


titulo = Label(miFrame, text = "PasswordsGenerator", font = ("System-UI", 20),)
titulo.grid(row = 0, column = 0, pady = 10, padx = 10)

botonCrear = Button(miFrame, text = "Create Password", fg = "white", bg = "green", font = ("System-UI", 10,  "bold"), command = CrearPassword) 
botonCrear.grid(row = 1, column = 0, pady = 10)


textoV = StringVar()


nombre = Label(miFrame, text = "", font = ("System-UI", 10, "bold"), textvariable=textoV)
nombre.grid(row = 2, column = 0, sticky = "", padx = 5, pady = 5)


raiz.mainloop()