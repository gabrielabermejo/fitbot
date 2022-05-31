from tkinter import *
from tkinter.font import BOLD, ITALIC

class Recetadelgado:
    def __init__(self):
        self.ventanita9 = Tk()
        self.ventanita9.title("Recetas Para Bajos de peso")

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

        self.miLabel5=Label(self.miFrame5, text="============RECETAS FACILES:============", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=0, y=10)
        self.miLabel5.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="1. Yogurt griego con cereales y frutos secos")
        self.miLabel5.place(x=55, y=45)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="Ingredientes: ")
        self.miLabel5.place(x=55, y=65)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 250 ml de yogur griego (puede ser blanco o con frutas)")
        self.miLabel5.place(x=55, y=90)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 100 grs de copos de avena")
        self.miLabel5.place(x=55, y=110)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 1 cucharadita de miel")
        self.miLabel5.place(x=55, y=130)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 10 porciones de frutos secos (puedes combinar nueces, \n almendras, avellanas)")
        self.miLabel5.place(x=55, y=150)
        self.miLabel5.config(bg='white')

        def codigoBoton4():
            self.ventanita9.destroy()
            pass
            
        botonInstru=Button(self.ventanita9, text="Mostrar pasos", command=codigoBoton4)
        botonInstru.place(x=60, y=200)
        botonInstru.config(bg='paleturquoise')


        
