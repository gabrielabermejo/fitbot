from tkinter import *
from tkinter.font import BOLD, ITALIC

class Batido:
    def __init__(self):
        self.ventanita8 = Tk()
        self.ventanita8.title("BATIDO")

        self.ventanita8.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita8.resizable(False, False)

        self.miFrame5=Frame(self.ventanita8, width=500, height=500)
        self.miFrame5.pack()
        self.miFrame5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=10)
        self.miFrame3.place(x=0,y=0)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="===================Pasos a seguir: ===================", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=0, y=10)
        self.miLabel5.config(bg='paleturquoise')

        self.miFrame3=Frame(self.miFrame5, width=500, height=10)
        self.miFrame3.place(x=0,y=35)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="1. Para preparar este desayuno solo necesitas mezclar todos los ingredientes  \n en un bol de desayuno. Si lo deseas, puedes trocear los frutos secos para \n que se mezclen mejor con el yogur.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=50)
        self.miLabel5.config(bg='white')