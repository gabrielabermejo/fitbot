from tkinter import *
from tkinter.font import BOLD, ITALIC
from froms.ensaladat import Ensalada
from froms.panque import Panq
from froms.caldo import Caldo


class Recetaobeso:
    def __init__(self):
        self.ventanita5 = Tk()
        self.ventanita5.title("Recetas Para sobrepeso")

        self.ventanita5.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita5.resizable(False, False)

        self.miFrame5=Frame(self.ventanita5, width=400, height=600)
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

        self.miLabel5=Label(self.miFrame5, text="1. Ensalada de tomate")
        self.miLabel5.place(x=55, y=45)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="Ingredientes: ")
        self.miLabel5.place(x=55, y=65)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 2 tomates grandes o tres medianos: ")
        self.miLabel5.place(x=55, y=90)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 1 diente de ajo grande ")
        self.miLabel5.place(x=55, y=110)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 2 cucharadas de orégano albahaca ú \n otra hierba de tu preferencia ")
        self.miLabel5.place(x=55, y=130)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- Aceite de oliva virgen extra")
        self.miLabel5.place(x=55, y=160)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- Una pizca de sal y pimienta negra \n recién molida")
        self.miLabel5.place(x=55, y=180)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- Vinagre balsámico o de jerez opcional.")
        self.miLabel5.place(x=55, y=200)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="2. Panqueques de banana.")
        self.miLabel5.place(x=55, y=260)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="Ingredientes: ")
        self.miLabel5.place(x=55, y=280)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 1 banana mediana ligeramente madura")
        self.miLabel5.place(x=55, y=300)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 50 gramos de harina de trigo todo uso")
        self.miLabel5.place(x=55, y=320)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 50 gramos de harina de quinoa ó de arroz")
        self.miLabel5.place(x=55, y=340)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 250 mililitros de leche desnatada")
        self.miLabel5.place(x=55, y=360)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="2. Caldo de verduras")
        self.miLabel5.place(x=55, y=415)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="Ingredientes: ")
        self.miLabel5.place(x=55, y=435)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 1 Kg de cebolla")
        self.miLabel5.place(x=55, y=455)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 1 Kg apio con sus hojas")
        self.miLabel5.place(x=55, y=475)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- 1/2  Kg de zanahorias")
        self.miLabel5.place(x=55, y=495)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="Otros opcionales: ")
        self.miLabel5.place(x=195, y=435)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- Dientes de ajo: ")
        self.miLabel5.place(x=195, y=455)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- Unas pocas ramas de cilantro")
        self.miLabel5.place(x=195, y=475)
        self.miLabel5.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="- Hojas de laurel")
        self.miLabel5.place(x=195, y=495)
        self.miLabel5.config(bg='white')


        def codigoBoton4():
            self.ventanita5.destroy()
            Ensalada()

        def codigoBoton5():
            self.ventanita5.destroy()
            Panq()

        def codigoBoton6():
            self.ventanita5.destroy()
            Caldo()
       

        botonInstru=Button(self.ventanita5, text="Mostrar pasos", command=codigoBoton4)
        botonInstru.place(x=60, y=225)
        botonInstru.config(bg='paleturquoise')

        botonInstru=Button(self.ventanita5, text="Mostrar pasos", command=codigoBoton5)
        botonInstru.place(x=60, y=385)
        botonInstru.config(bg='paleturquoise')

        botonInstru=Button(self.ventanita5, text="Mostrar pasos", command=codigoBoton6)
        botonInstru.place(x=60, y=520)
        botonInstru.config(bg='paleturquoise')

        

        