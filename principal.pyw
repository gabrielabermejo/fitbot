from tkinter import *
from entidades.persona import Personas
from froms.informacion import Info
class Principal:
    def __init__(self):
        self.ventanita = Tk()
        self.ventanita.title("FitBot")

        self.peso=StringVar()
        self.altura=StringVar()
        self.edad=StringVar()

        self.ventanita.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita.resizable(False, False)

        self.miFrame=Frame(self.ventanita, width=500, height=700)
        self.miFrame.pack()
        self.miFrame.config(bg='dark turquoise')
        self.miLabel=Label(self.miFrame, text="Digite sus datos", font=("Courier", 13))
        self.miLabel.place(x=150, y=20)
        self.miLabel.config(bg='dark turquoise')

        pesoLabel=Label(self.miFrame, text="Peso:", padx=-12)
        pesoLabel.place(x=150, y=55)
        cuadroTexto=Entry(self.ventanita, textvariable=self.peso)
        cuadroTexto.place(x=190, y=55)

        alturaLabel=Label(self.miFrame, text="Altura:", padx=-12)
        cmLabel=Label(self.miFrame, text="(cm)")
        cmLabel.place(x=320, y=85)
        alturaLabel.place(x=150, y=85)
        cuadroTexto1=Entry(self.ventanita, textvariable=self.altura)
        cuadroTexto1.place(x=190, y=85)

        edadLabel=Label(self.miFrame, text="Edad:", padx=-12)
        edadLabel.place(x=150, y=115)
        cuadroTexto2=Entry(self.ventanita, textvariable=self.edad)
        cuadroTexto2.place(x=190, y=115)

        def codigoBoton():
            print(self.peso.get())
            print(self.altura.get())
            print(self.edad.get())
            int(self.peso.get())
            int(self.altura.get())
            int(self.edad.get())
            p =  Personas(int(self.peso.get()), int(self.altura.get()), int(self.edad.get()))
            Info(p)
            

        botonEnvio=Button(self.ventanita, text="Enviar", command=codigoBoton)
        botonEnvio.place(x=220, y=145)

        self.ventanita.mainloop()

   

Principal()