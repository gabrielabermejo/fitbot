from distutils.log import info
from tkinter import *
from tkinter.font import BOLD, ITALIC
from froms.recobeso import Recetaobeso
from froms.recdelgado import Recetadelgado


class Recetas:
    def __init__(self):
        self.ventanita4 = Tk()
        self.ventanita4.title("RECETAS")

        self.ventanita4.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita4.resizable(False, False)

        self.miFrame4=Frame(self.ventanita4, width=200, height=160)
        self.miFrame4.pack()
        self.miFrame4.config(bg='teal')

        self.miFrame5=Frame(self.miFrame4, width=500, height=15)
        self.miFrame5.place(x=0,y=0)
        self.miFrame5.config(bg='paleturquoise')

        self.miFrame5=Frame(self.miFrame4, width=500, height=15)
        self.miFrame5.place(x=0,y=145)
        self.miFrame5.config(bg='paleturquoise')

        
        def codigoBoton3():
            self.ventanita4.destroy()
            Recetaobeso()
       

        botonInstru=Button(self.ventanita4, text="   Sobrepeso  ", command=codigoBoton3)
        botonInstru.place(x=45, y=35)
        botonInstru.config(bg='paleturquoise')

        def codigoBoton4():
            self.ventanita4.destroy()
            Recetadelgado()
       

        botonInstru=Button(self.ventanita4, text=" Bajo de peso ", command=codigoBoton4)
        botonInstru.place(x=45, y=70)
        botonInstru.config(bg='paleturquoise')


        
       



