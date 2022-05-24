from entidades.persona import Personas
from tkinter import *

class Info:
    def __init__(self,persona):
        self.ventanita2 = Tk()
        self.ventanita2.title("INFORMACION")

        self.ventanita2.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita2.resizable(False, False)

        self.miFrame2=Frame(self.ventanita2, width=500, height=500)
        self.miFrame2.pack()
        self.miFrame2.config(bg='pink2')
        self.miLabel2=Label(self.miFrame2, text="Resultados", font=("The Monotype Corporation", 13))
        self.miLabel2.place(x=150, y=20)
        self.miLabel2.config(bg='pink2')

        pesoLabel2=Label(self.miFrame2, text="Peso: "+str(persona.peso), padx=-12)
        pesoLabel2.place(x=150, y=55)
        
        pesoLabel2=Label(self.miFrame2, text="Altura: "+str(persona.altura), padx=-12)
        pesoLabel2.place(x=150, y=85)

        pesoLabel2=Label(self.miFrame2, text="Edad: "+str(persona.edad), padx=-12)
        pesoLabel2.place(x=150, y=115)

        self.miLabel3=Label(self.miFrame2, text="Su IMC: ", font=("The Monotype Corporation", 13))
        self.miLabel3.place(x=150, y=150)
        self.miLabel3.config(bg='pink2')

        IMC = persona.peso/((persona.altura*0.01)**2)

        Mensaje= StringVar()
        recomendacion= StringVar()
        if IMC<=18.5 and IMC>=0:
            Mensaje.set('bajo de peso')
            recomendacion.set('')
        elif IMC>=18.5 and IMC<=24.9:
            Mensaje.set('normal')
            recomendacion.set('')
        elif IMC>=25 and IMC<=29.9:
            Mensaje.set('sobre peso')
            recomendacion.set('')
        else:
            Mensaje.set('obeso')
            recomendacion.set("Visite por favor un nutricionista \n e intente mejorar su actividad física diaria")
    
        print(Mensaje.get())
        print(str(IMC))

        IMCLabel2=Label(self.miFrame2, text="Su IMC es de: "+str(IMC), padx=-12)
        IMCLabel2.place(x=150, y=200)

        estadoLabel2=Label(self.miFrame2, text="Estado: "+Mensaje.get(), padx=-12)
        estadoLabel2.place(x=150, y=225)

        recomendacionesLabel2=Label(self.miFrame2, text="Recomendaciones: "+recomendacion.get(), padx=-12)
        recomendacionesLabel2.place(x=150, y=250)

        self.ventanita2.mainloop()
