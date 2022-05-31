from tkinter import *
from tkinter.font import BOLD, ITALIC

class Ensalada:
    def __init__(self):
        self.ventanita7 = Tk()
        self.ventanita7.title("ENSALADA DE TOMATE")

        self.ventanita7.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita7.resizable(False, False)

        self.miFrame5=Frame(self.ventanita7, width=500, height=500)
        self.miFrame5.pack()
        self.miFrame5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="Pasos a seguir: ", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=55, y=20)
        self.miLabel5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="1. Para empezar, lavar bien los tomates. \n Yo me aseguro de eliminar cualquier residuo, \n remojándolos con agua y un chorro de vinagre \n (blanco) después de lavarlos. ", font=("Arial", 10))
        self.miLabel5.place(x=55, y=20)
        self.miLabel5.config(bg='pink')
