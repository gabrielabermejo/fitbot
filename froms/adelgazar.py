from tkinter import *
from tkinter.font import BOLD, ITALIC
from froms.sentadilla import Sentadilla
from froms.press import Press

class EjerciciosA:
    def __init__(self):
        self.ventanita9 = Tk()
        self.ventanita9.title("RUTINAS ADELGAZAR")

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

        self.miLabel5=Label(self.miFrame5, text="========RUTINA PARA BAJAR PESO========", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=0, y=10)
        self.miLabel5.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="1. Sentadillas con barra")
        self.miLabel5.place(x=15, y=45)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="Las sentadillas acompañadas con una barra de peso son un ejercicio \n muy eficaz para aumentar nuestra masa muscular, especialmente en \n las piernas, glúteos y abdomen. ")
        self.miLabel5.place(x=15, y=65)
        self.miLabel5.config(bg='white')

        def codigoBoton4():
            self.ventanita9.destroy()
            Sentadilla()
            
        botonInstru=Button(self.ventanita9, text="Mostrar pasos", command=codigoBoton4)
        botonInstru.place(x=60, y=118)
        botonInstru.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="2. Press de banca")
        self.miLabel5.place(x=15, y=145)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="El press de banca es el levantamiento de peso tumbado en un banco, \n otro ejercicio con el que conseguirás desarrollar poco a poco tus \n  músculos, especialmente el torso y los brazos. ")
        self.miLabel5.place(x=15, y=165)
        self.miLabel5.config(bg='white')

        def codigoBoton5():
            self.ventanita9.destroy()
            Press()
            
        botonInstru=Button(self.ventanita9, text="Mostrar pasos", command=codigoBoton5)
        botonInstru.place(x=60, y=220)
        botonInstru.config(bg='paleturquoise')