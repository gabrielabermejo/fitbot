from tkinter import *
from tkinter.font import BOLD, ITALIC

class Recetaobeso:
    def __init__(self):
        self.ventanita5 = Tk()
        self.ventanita5.title("Recetas Para sobrepeso")

        self.ventanita5.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita5.resizable(False, False)

        self.miFrame5=Frame(self.ventanita5, width=400, height=300)
        self.miFrame5.pack()
        self.miFrame5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="RECETAS FACILES:", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=55, y=20)
        self.miLabel5.config(bg='pink')

        

        