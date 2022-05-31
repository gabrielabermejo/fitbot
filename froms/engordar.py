from tkinter import *
from tkinter.font import BOLD, ITALIC

class Engordar:
    def __init__(self):
        self.ventanita9 = Tk()
        self.ventanita9.title("RUTINAS SUBIR DE PESO")

        self.ventanita9.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita9.resizable(False, False)

        self.miFrame5=Frame(self.ventanita9, width=400, height=600)
        self.miFrame5.pack()
        self.miFrame5.config(bg='white')

        self.miFrame=Frame(self.miFrame5, width=10, height=600)
        self.miFrame.place(x=0,y=0)
        self.miFrame.config(bg='paleturquoise')

        self.miFrame=Frame(self.miFrame5, width=400, height=10)
        self.miFrame.place(x=0,y=590)
        self.miFrame.config(bg='paleturquoise')

        self.miFrame=Frame(self.miFrame5, width=400, height=10)
        self.miFrame.place(x=0,y=0)
        self.miFrame.config(bg='paleturquoise')

        self.miFrame=Frame(self.miFrame5, width=10, height=600)
        self.miFrame.place(x=390,y=0)
        self.miFrame.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="========RUTINA AUMENTAR PESO========", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=0, y=10)
        self.miLabel5.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="1. Flexiones (20 segundos)")
        self.miLabel5.place(x=15, y=45)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="2. Zancadas con peso (20 segundos)")
        self.miLabel5.place(x=15, y=75)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="3. Remo con peso (20 segundos)")
        self.miLabel5.place(x=15, y=105)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="4. Rodillas arriba (20 segundos)")
        self.miLabel5.place(x=15, y=135)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="5. Sentadillas (20 segundos)")
        self.miLabel5.place(x=15, y=165)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="6. Jumping jacks (20 segundos)")
        self.miLabel5.place(x=15, y=195)
        self.miLabel5.config(bg='white')