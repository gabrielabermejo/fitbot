from tkinter import *
from tkinter.font import BOLD, ITALIC

class Sentadilla:
    def __init__(self):
        self.ventanita8 = Tk()
        self.ventanita8.title("SENTADILLAS")

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

        self.miLabel5=Label(self.miFrame5, text="1. Para realizar este ejercicio tendrás que ponerte de pie, con las piernas algo más \n separadas de la línea de tus hombros.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=50)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="2. Ponte la barra detrás de la nuca, agarrándola con fuerza con ambas manos.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=105)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="3. Baja lentamente flexionando las rodillas y manteniendo la espalda recta.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=147)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="4. Luego vuelve a la posición inicial. Haz 2 series de 10 repeticiones.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=185)
        self.miLabel5.config(bg='white')