from tkinter import *
class Info:
    def __init__(self,persona):
        self.ventanita2 = Tk()
        self.ventanita2.title("INFORMACION")

        self.ventanita2.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita2.resizable(False, False)

        self.miFrame2=Frame(self.ventanita2, width=500, height=700)
        self.miFrame2.pack()
        self.miFrame2.config(bg='dark turquoise')
        self.miLabel2=Label(self.miFrame2, text="Resiltados", font=("Courier", 13))
        self.miLabel2.place(x=150, y=20)
        self.miLabel2.config(bg='dark turquoise')

        pesoLabel2=Label(self.miFrame2, text="Peso: "+"50", padx=-12)
        pesoLabel2.place(x=150, y=55)
        
        pesoLabel2=Label(self.miFrame2, text="Altura: "+"50", padx=-12)
        pesoLabel2.place(x=150, y=85)

        pesoLabel2=Label(self.miFrame2, text="Edad: "+"50", padx=-12)
        pesoLabel2.place(x=150, y=115)

        self.miLabel3=Label(self.miFrame2, text="Recomendaciones: ", font=("Courier", 13))
        self.miLabel3.place(x=150, y=150)
        self.miLabel3.config(bg='dark turquoise')

        
        self.ventanita2.mainloop()
