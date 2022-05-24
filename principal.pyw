from tkinter import *
from tkinter.font import BOLD, ITALIC
from entidades.persona import Personas
from froms.informacion import Info

class Principal:
    def destruir(self):
        self.ventanita.destroy()
        Info()

    def __init__(self):
        self.ventanita = Tk()
        self.ventanita.title("FitBot")

        self.peso=StringVar()
        self.altura=StringVar()
        self.edad=StringVar()

        self.ventanita.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita.resizable(False, False)

        self.miFrame=Frame(self.ventanita, width=500, height=400)
        self.miFrame.pack()
        self.miFrame.config(bg='pink')
        self.miLabel=Label(self.miFrame, text="Digite sus datos", font=("Arial", 21, BOLD, ITALIC))
        self.miLabel.place(x=155, y=15)
        self.miLabel.config(bg='pink')

        self.miFrame3=Frame(self.miFrame, width=500, height=400)
        self.miFrame3.place(x=0,y=55)
        self.miFrame3.config(bg='pink2')

        pesoLabel=Label(self.miFrame, text="Peso:", padx=-12)
        pesoLabel.place(x=150, y=60)
        pesoLabel.config(bg='pink2')
        kgLabel=Label(self.miFrame, text="(Kg)")
        kgLabel.config(bg='pink2')
        kgLabel.place(x=320, y=60)
        cuadroTexto=Entry(self.ventanita, textvariable=self.peso)
        cuadroTexto.place(x=190, y=60)

        alturaLabel=Label(self.miFrame, text="Altura:", padx=-12)
        alturaLabel.config(bg='pink2')
        cmLabel=Label(self.miFrame, text="(cm)")
        cmLabel.config(bg='pink2')
        cmLabel.place(x=320, y=90)
        alturaLabel.place(x=150, y=90)
        cuadroTexto1=Entry(self.ventanita, textvariable=self.altura)
        cuadroTexto1.place(x=190, y=90)

        edadLabel=Label(self.miFrame, text="Edad:", padx=-12)
        edadLabel.config(bg='pink2')
        edadLabel.place(x=150, y=120)
        cuadroTexto2=Entry(self.ventanita, textvariable=self.edad)
        cuadroTexto2.place(x=190, y=120)

        def codigoBoton():

            if len(self.peso.get())==0:
                return
            if len(self.altura.get())==0:
                return
            if len(self.edad.get())==0:
                return
            p =  Personas(int(self.peso.get()), int(self.altura.get()), int(self.edad.get()))
            
            self.peso.set('')
            self.altura.set('')
            self.edad.set('')


            self.ventanita.destroy()
            Info(p)

        botonEnvio=Button(self.ventanita, text="Enviar", command=codigoBoton, bg='light pink')
        botonEnvio.place(x=220, y=145)

        self.ventanita.mainloop()

   

Principal()