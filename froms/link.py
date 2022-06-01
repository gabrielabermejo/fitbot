from tkinter import *
from tkinter.font import BOLD, ITALIC
import webbrowser

class Link:
    def __init__(self):
        self.ventanita8 = Tk()
        self.ventanita8.title("SENTADILLAS")

        self.ventanita8.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita8.resizable(False, False)

        self.miFrame5=Frame(self.ventanita8, width=500, height=500)
        self.miFrame5.pack()
        self.miFrame5.config(bg='white')

        webbrowser.open("https://www.comedera.com/recetas-para-adelgazar/")
        