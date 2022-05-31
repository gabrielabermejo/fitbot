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
        self.miFrame5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=10)
        self.miFrame3.place(x=0,y=0)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="===================Pasos a seguir: ===================", font=("Arial", 13, BOLD, ITALIC))
        self.miLabel5.place(x=0, y=10)
        self.miLabel5.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="1. Para empezar, lavar bien los tomates. Yo me aseguro de eliminar cualquier residuo, \n remojándolos con agua y un chorro de vinagre (blanco) después de lavarlos. ", font=("Arial", 9))
        self.miLabel5.place(x=6, y=35)
        self.miLabel5.config(bg='white')

        self.miLabel2=Label(self.miFrame5, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=65)
        self.miLabel2.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="2. Picar los tomates en rueda delgadas y acomodarlos en un bol o plato grande. \n Hay quienes prefieren pelarlos antes de picar, pero para mi gusto la piel les deja \n más sabor, nutrientes y fibra.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=95)
        self.miLabel5.config(bg='white')

        self.miLabel2=Label(self.miFrame5, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=140)
        self.miLabel2.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="3. Pelar el ajo, y luego triturarlo o picarlo en cubo muy pequeños.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=186)
        self.miLabel5.config(bg='white')

        self.miLabel2=Label(self.miFrame5, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=204)
        self.miLabel2.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="4. Esparcir el ajo sobre las ruedas de tomate. Hay que cuidar que los trozos sean real- \n mente pequeños para que el gusto quede uniforme y nadie termine con un bocado \n sorpresa de ajo tamaño irregular.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=245)
        self.miLabel5.config(bg='white')

        self.miLabel2=Label(self.miFrame5, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=295)
        self.miLabel2.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="5. Espolvorear la ensalada con sal y pimienta al gusto.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=337)
        self.miLabel5.config(bg='white')

        self.miLabel2=Label(self.miFrame5, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=360)
        self.miLabel2.config(bg='white')

        self.miLabel5=Label(self.miFrame5, text="6. Cubrir con un hilo de aceite de oliva, más o menos grueso según el gusto personal, \n y si se ha decidido utilizar vinagre balsámico, otro de hilo de este último. \n En caso de añadir más ingredientes a la receta básica de ensalada de tomates, se \n recomienda moderar la adición de vinagre, para evitar la competencia de sabores.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=405)
        self.miLabel5.config(bg='white')
