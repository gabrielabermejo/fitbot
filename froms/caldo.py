from tkinter import *
from tkinter.font import BOLD, ITALIC

class Caldo:
    def __init__(self):
        self.ventanita9 = Tk()
        self.ventanita9.title("PANQUEQUES DE BANANO")

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