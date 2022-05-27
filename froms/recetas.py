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

        self.miFrame4=Frame(self.ventanita4, width=200, height=200)
        self.miFrame4.pack()
        self.miFrame4.config(bg='plum')

        self.miLabel4=Label(self.miFrame4, text="1. Sobrepeso", font=("Arial", 15, BOLD, ITALIC))
        self.miLabel4.place(x=25, y=20)
        self.miLabel4.config(bg='plum')

        self.miLabel4=Label(self.miFrame4, text=" 2. Bajo de peso ", font=("Arial", 15, BOLD, ITALIC))
        self.miLabel4.place(x=25, y=55)
        self.miLabel4.config(bg='plum')

        def codigoBoton3():
            self.ventanita4.destroy()
            Recetaobeso()
       

        botonInstru=Button(self.ventanita4, text="1", command=codigoBoton3, bg='pink')
        botonInstru.place(x=65, y=120)

        def codigoBoton4():
            self.ventanita4.destroy()
            Recetadelgado()
       

        botonInstru=Button(self.ventanita4, text="2", command=codigoBoton4, bg='pink')
        botonInstru.place(x=115, y=120)

