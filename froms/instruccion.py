from tkinter import *
from tkinter.font import BOLD, ITALIC
class Instru:
    def __init__(self):
        self.ventanita3 = Tk()
        self.ventanita3.title("INSTRUCCIONES")

        self.ventanita3.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita3.resizable(False, False)

        self.miFrame3=Frame(self.ventanita3, width=500, height=500)
        self.miFrame3.pack()
        self.miFrame3.config(bg='pink')

        self.miLabel3=Label(self.miFrame3, text="¿Cómo usar el FitBot?", font=("Arial", 21, BOLD, ITALIC))
        self.miLabel3.place(x=135, y=20)
        self.miLabel3.config(bg='pink')

        self.miLabel4=Label(self.miFrame3, text="INSTRUCCIONES: ", font=("The Monotype Corporation", 13))
        self.miLabel4.place(x=135, y=65)
        self.miLabel4.config(bg='pink')

        instruLabel2=Label(self.miFrame3, text="Primer paso: ", padx=-12)
        instruLabel2.place(x=135, y=105)

        instruLabel2=Label(self.miFrame3, text="Ingrese por favor sus datos CORRECTAMENTE \n según las instrucciones, recordando que son, \n peso, altura y edad en este mismo orden ", padx=-12)
        instruLabel2.place(x=135, y=125)

        instruLabel2=Label(self.miFrame3, text="Segundo paso: ", padx=-12)
        instruLabel2.place(x=135, y=200)

        instruLabel2=Label(self.miFrame3, text="Haga click en el botón de enviar, en este  \n momento lo dirigira a otra pestaña en la que  \n le mostrara sus resultados", padx=-12)
        instruLabel2.place(x=135, y=220)

        instruLabel2=Label(self.miFrame3, text="Tercer paso:", padx=-12)
        instruLabel2.place(x=135, y=265)

        instruLabel2=Label(self.miFrame3, text="Si desea más información, en esta \n nueva pestaña abierta encontrará un \n boton el cual le enseñará recetas que usted \n puede tomar en cuenta segun sus recomendacione.", padx=-12)
        instruLabel2.place(x=135, y=285)

        instruLabel2=Label(self.miFrame3, text="Cuarto paso:", padx=-12)
        instruLabel2.place(x=135, y=400)











        self.ventanita3.mainloop()

