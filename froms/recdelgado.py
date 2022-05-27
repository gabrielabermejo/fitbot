from tkinter import *
from tkinter.font import BOLD, ITALIC

class Recetadelgado:
    def __init__(self):
        self.ventanita6 = Tk()
        self.ventanita6.title("Recetas Para Bajos de peso")

        self.ventanita6.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita6.resizable(False, False)

        self.miFrame5=Frame(self.ventanita6, width=400, height=300)
        self.miFrame5.pack()
        self.miFrame5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="RECETAS FACILES:", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=55, y=20)
        self.miLabel5.config(bg='pink')

        