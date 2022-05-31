from tkinter import *
from tkinter.font import BOLD, ITALIC
from froms.ensaladat import Ensalada


class Recetaobeso:
    def __init__(self):
        self.ventanita5 = Tk()
        self.ventanita5.title("Recetas Para sobrepeso")

        self.ventanita5.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita5.resizable(False, False)

        self.miFrame5=Frame(self.ventanita5, width=400, height=400)
        self.miFrame5.pack()
        self.miFrame5.config(bg='pink')


        self.miLabel5=Label(self.miFrame5, text="RECETAS FACILES:", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=55, y=20)
        self.miLabel5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="Ensalada de tomate")
        self.miLabel5.place(x=55, y=45)
        self.miLabel5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="Ingredientes: ")
        self.miLabel5.place(x=55, y=65)
        self.miLabel5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="- 2 tomates grandes o tres medianos: ")
        self.miLabel5.place(x=55, y=90)
        self.miLabel5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="- 1 diente de ajo grande ")
        self.miLabel5.place(x=55, y=110)
        self.miLabel5.config(bg='pink')

        self.miLabel5=Label(self.miFrame5, text="- 2 cucharadas de orégano albahaca ú \n otra hierba de tu preferencia ")
        self.miLabel5.place(x=55, y=130)
        self.miLabel5.config(bg='pink')

        def codigoBoton4():
            self.ventanita5.destroy()
            Ensalada()
       

        botonInstru=Button(self.ventanita5, text="Mostrar pasos", command=codigoBoton4)
        botonInstru.place(x=45, y=350)
        botonInstru.config(bg='pink2')

        

        