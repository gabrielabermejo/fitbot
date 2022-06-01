from tkinter import *
from tkinter.font import BOLD, ITALIC
import webbrowser
class Instru:
    def __init__(self):
        self.ventanita3 = Tk()
        self.ventanita3.title("INSTRUCCIONES")

        self.ventanita3.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita3.resizable(False, False)

        self.miFrame3=Frame(self.ventanita3, width=500, height=500)
        self.miFrame3.pack()
        self.miFrame3.config(bg='white')

        webbrowser.open("https://gabymorenobermejo.wixsite.com/fitbot")







        self.ventanita3.mainloop()

