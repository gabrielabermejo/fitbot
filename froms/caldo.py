from tkinter import *
from tkinter.font import BOLD, ITALIC

class Caldo:
    def __init__(self):
        self.ventanita9 = Tk()
        self.ventanita9.title("CALDO")

        self.ventanita9.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita9.resizable(False, False)

        self.miFrame5=Frame(self.ventanita9, width=500, height=500)
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

        self.miLabel5=Label(self.miFrame5, text="1. Limpia y corta las verduras en trozos medianos, cubos, trozos irregulares, \n tiras, como quieras, no hay regla aquí.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=50)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=90)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="2.Coloca todos los ingredientes en una olla con 3 litros de agua y pon la temperatura al \n máximo. Cuando comience a hervir pon el fuego a la mitad y cocina hasta que el líquido \n  reduzca a la mitad. Calcula aproximadamente 45 minutos, dependiendo de tu cocina.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=95)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=145)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="3.Transcurrido este tiempo cuela bien el caldo, déjalo enfriar y guárdalo en recipientes \n plásticos con tapa..", font=("Arial", 9))
        self.miLabel5.place(x=6, y=150)
        self.miLabel5.config(bg='white')