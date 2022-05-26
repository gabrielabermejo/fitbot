from tkinter import *
from tkinter.font import BOLD, ITALIC

class Recetas:
    def __init__(self):
        self.ventanita4 = Tk()
        self.ventanita4.title("RECETAS")

        self.ventanita4.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita4.resizable(False, False)

        self.miFrame4=Frame(self.ventanita4, width=500, height=500)
        self.miFrame4.pack()
        self.miFrame4.config(bg='pink')

        self.miLabel4=Label(self.miFrame4, text="1. Sobrepeso", font=("Arial", 18, BOLD, ITALIC))
        self.miLabel4.place(x=135, y=20)
        self.miLabel4.config(bg='pink')

        self.miLabel4=Label(self.miFrame4, text=" 2. Bajo de peso ", font=("Arial", 18, BOLD, ITALIC))
        self.miLabel4.place(x=135, y=55)
        self.miLabel4.config(bg='pink')
        


