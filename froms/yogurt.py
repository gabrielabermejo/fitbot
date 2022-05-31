from tkinter import *
from tkinter.font import BOLD, ITALIC

class Yogurt:
    def __init__(self):
        self.ventanita10 = Tk()
        self.ventanita10.title("YOGURT")

        self.ventanita10.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita10.resizable(False, False)

        self.miFrame5=Frame(self.ventanita10, width=500, height=500)
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

        self.miLabel5=Label(self.miFrame5, text="1. Pela el mango y extrae la pulpa de su interior para añadirla a la licuadora.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=60)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=100)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="2. Luego debes añadir al vaso de la batidora un plátano pelado y cortado en varios trozos.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=105)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=143)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="3. Por último, añade a la mezcla media taza de yogur y otro medio \n vaso de leche de vaca, ya sea entera o desnatada.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=147)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=180)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="4. Bate toda la mezcla en la licuadora hasta conseguir un batido cremoso.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=185)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=208)
        self.miFrame3.config(bg='paleturquoise')

        self.miLabel5=Label(self.miFrame5, text="5. Si quieres endulzar un poco más esta bebida, puedes añadirle una cucharadita de \n miel en lugar de azúcar, ya que se trata de utilizar ingredientes saludables.", font=("Arial", 9))
        self.miLabel5.place(x=6, y=213)
        self.miLabel5.config(bg='white')

        self.miFrame3=Frame(self.miFrame5, width=500, height=2)
        self.miFrame3.place(x=0,y=248)
        self.miFrame3.config(bg='paleturquoise')