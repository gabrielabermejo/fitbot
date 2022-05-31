from tkinter import *
from tkinter.font import BOLD, ITALIC

class Panq:
    def __init__(self):
        self.ventanita8 = Tk()
        self.ventanita8.title("PANQUEQUES DE BANANO")

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

        self.miLabel5=Label(self.miFrame5, text="1. Con un tenedor aplasta la banana hasta reducirla a una consistencia pastosa. \n Pero no abuses, no la hagas puré.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=50)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=90)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="2. En un bowl mezcla las harinas con la leche y la banana aplastada..", font=("Arial", 9))
        self.miLabel5.place(x=6, y=95)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=123)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="3. Si no estás en una onda dietética siéntete libre de agregarle un poquito de azúcar.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=127)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=151)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="4. Recuerda que puedes sustituir los tipos de harina dependiendo de tu \n gusto/necesidad.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=155)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=194)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="5. Calienta una sartén de teflón, ponle media cucharadita de aceite y agrega, con una \n cuchara sopera de las pequeñas, una cantidad de mezcla de panqueques que \n cubra toda la superficie del sartén sin excesos.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=197)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=250)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="6. Cuando empiece a hacérsele pequeños agujeros a la mezcla es que está lista para \n voltear, dales la vuelta con una paleta, dejar cocinar por el otro lado un par de \n minutos y sirve en un plato.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=257)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=313)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="7. Repite este procedimiento con toda la mezcla de panqueques hasta que se termine", font=("Arial", 9))
        self.miLabel5.place(x=6, y=315)
        self.miLabel5.config(bg='white')

        






       
