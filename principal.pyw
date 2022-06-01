from tkinter import *
from tkinter.font import BOLD, ITALIC
from entidades.persona import Personas
from froms.informacion import Info
from froms.instruccion import Instru

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
        self.miFrame.config(bg='paleturquoise')
        self.miLabel=Label(self.miFrame, text="Digite sus datos", font=("Arial", 21, BOLD, ITALIC))
        self.miLabel.place(x=150, y=25)
        self.miLabel.config(bg='paleturquoise')

        self.miFrame3=Frame(self.miFrame, width=500, height=400)
        self.miFrame3.place(x=0,y=70)
        self.miFrame3.config(bg='white')

        pesoLabel=Label(self.miFrame, text="Peso:", padx=-12)
        pesoLabel.place(x=150, y=90)
        pesoLabel.config(bg='white')
        kgLabel=Label(self.miFrame, text="(Kg)")
        kgLabel.config(bg='white')
        kgLabel.place(x=320, y=90)
        cuadroTexto=Entry(self.ventanita, textvariable=self.peso)
        cuadroTexto.place(x=190, y=90)

        alturaLabel=Label(self.miFrame, text="Altura:", padx=-12)
        alturaLabel.config(bg='white')
        cmLabel=Label(self.miFrame, text="(cm)")
        cmLabel.config(bg='white')
        cmLabel.place(x=320, y=120)
        alturaLabel.place(x=150, y=120)
        cuadroTexto1=Entry(self.ventanita, textvariable=self.altura)
        cuadroTexto1.place(x=190, y=120)

        edadLabel=Label(self.miFrame, text="Edad:", padx=-12)
        edadLabel.config(bg='white')
        edadLabel.place(x=150, y=150)
        cuadroTexto2=Entry(self.ventanita, textvariable=self.edad)
        cuadroTexto2.place(x=190, y=150)

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

        def codigoBoton1():

            Instru()

        botonEnvio=Button(self.ventanita, text="Enviar", command=codigoBoton, bg='paleturquoise')
        botonEnvio.place(x=220, y=210)

        botonInstru=Button(self.ventanita, text="?", command=codigoBoton1, bg='paleturquoise')
        botonInstru.place(x=15, y=350)

        self.ventanita.mainloop()


Principal()