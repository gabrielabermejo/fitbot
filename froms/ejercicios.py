from distutils.log import info
from tkinter import *
from tkinter.font import BOLD, ITALIC
from froms.adelgazar import EjerciciosA

class Ejercicios:
    def __init__(self):
        self.ventanita11 = Tk()
        self.ventanita11.title("EJERCICIOS")

        self.ventanita11.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita11.resizable(False, False)

        self.miFrame4=Frame(self.ventanita11, width=200, height=160)
        self.miFrame4.pack()
        self.miFrame4.config(bg='teal')

        self.miFrame5=Frame(self.miFrame4, width=500, height=15)
        self.miFrame5.place(x=0,y=0)
        self.miFrame5.config(bg='paleturquoise')

        self.miFrame5=Frame(self.miFrame4, width=500, height=15)
        self.miFrame5.place(x=0,y=145)
        self.miFrame5.config(bg='paleturquoise')

        def codigoBoton3():
            self.ventanita11.destroy()
            EjerciciosA()
       

        botonInstru=Button(self.ventanita11, text="   Adelgazar  ", command=codigoBoton3)
        botonInstru.place(x=45, y=35)
        botonInstru.config(bg='paleturquoise')


