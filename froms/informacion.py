from entidades.persona import Personas
from tkinter import *
from froms.recetas import Recetas
from froms.ejercicios import Ejercicios
from tkinter.font import BOLD, ITALIC
#from colorama import Fore, init
#init()
class Info:
    def __init__(self,persona):
        self.ventanita2 = Tk()
        self.ventanita2.title("INFORMACION")

        self.ventanita2.iconbitmap("froms\imagenes\icono.ico")

        self.ventanita2.resizable(False, False)

        self.miFrame2=Frame(self.ventanita2, width=500, height=500)
        self.miFrame2.pack()
        self.miFrame2.config(bg='white')
        self.miLabel2=Label(self.miFrame2, text="===============RESULTADOS===============", font=("The Monotype Corporation", 16), fg='black')
        self.miLabel2.place(x=1, y=14)
        self.miLabel2.config(bg='white')

        self.miFrame3=Frame(self.miFrame2, width=500, height=15)
        self.miFrame3.place(x=0,y=0)
        self.miFrame3.config(bg='paleturquoise')

        self.miFrame4=Frame(self.miFrame2, width=500, height=15)
        self.miFrame4.place(x=0,y=40)
        self.miFrame4.config(bg='paleturquoise')

        self.miLabel2=Label(self.miFrame2, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=86)
        self.miLabel2.config(bg='white')

        pesoLabel2=Label(self.miFrame2, text="Peso: "+str(persona.peso),font=9, padx=-12,fg='black', bg='white')
        pesoLabel2.place(x=220, y=80)

        self.miLabel2=Label(self.miFrame2, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=120)
        self.miLabel2.config(bg='white')
        
        alturaLabel2=Label(self.miFrame2, text="Altura: "+str(persona.altura),font=9, padx=-12, fg='black', bg='white')
        alturaLabel2.place(x=220, y=115)

        self.miLabel2=Label(self.miFrame2, text="___________________________________________", font=("The Monotype Corporation", 16), fg='paleturquoise')
        self.miLabel2.place(x=1, y=155)
        self.miLabel2.config(bg='white')

        edadLabel2=Label(self.miFrame2, text="Edad: "+str(persona.edad), font=9,padx=-12, bg='white', fg='black')
        edadLabel2.place(x=220, y=150)


        IMC = persona.peso/((persona.altura*0.01)**2)

        Mensaje= StringVar()
        recomendacion= StringVar()
        if IMC<=18.5 and IMC>=0:
            Mensaje.set('bajo de peso')
            recomendacion.set('Visite por favor un nutricionista \n e intente mejorar su actividad f??sica diaria \n si desea, tambien puede agregar \n nuevas dietas a su diario vivir')
        elif IMC<0 and persona.peso<0:
            Mensaje.set('Debe digitar un valor valido')
            recomendacion.set('Por favor, ingrese de nuevo')
            #estadoLabel2=Label(self.miFrame2, text="Estado: "+Mensaje.get(), padx=-12)
            #estadoLabel2.place(x=150, y=225)
            #recomendacionesLabel2=Label(self.miFrame2, text="Por favor: "+recomendacion.get(), padx=-12)
            #recomendacionesLabel2.place(x=150, y=250)
        elif IMC>=18.5 and IMC<=24.9:
            Mensaje.set('normal')
            recomendacion.set('FELICITACIONES, \n su estado esta acorde a usted')
        elif IMC>=25 and IMC<=29.9:
            Mensaje.set('sobre peso')
            recomendacion.set('Intente por favor mejorar su actividad diaria')
        else:
            Mensaje.set('obeso')
            recomendacion.set("Visite por favor un nutricionista \n e intente mejorar su actividad f??sica diaria")
    
        print(Mensaje.get())
        print(str(IMC))

        IMCLabel2=Label(self.miFrame2, text="Su IMC es de: "+str(IMC), padx=-12, fg='black', bg='white', font=("Arial", 13))
        IMCLabel2.place(x=135, y=200)

        estadoLabel2=Label(self.miFrame2, text="Estado: "+Mensaje.get(), padx=-12, fg='black', bg='white', font=("Arial", 13))
        estadoLabel2.place(x=135, y=235)


        recomendacionesLabel2=Label(self.miFrame2, text="Recomendaciones: "+recomendacion.get(), padx=-12, bg='white', fg='black', font=("Arial", 10))
        recomendacionesLabel2.place(x=135, y=265)


        def codigoBoton2():
    
            Recetas()

        botonInstru=Button(self.ventanita2, text="RECETAS", command=codigoBoton2, bg='paleturquoise', fg='black')
        botonInstru.place(x=55, y=380)

        g=persona.altura-100

        if g==persona.peso:
            Mensaje.set('Usted se encuentra en buen estado')
        else:
            Mensaje.set('Su peso ideal es de: '+str(g))
            
        gLabel2=Label(self.miFrame2, text="Acerca de su peso ideal: "+Mensaje.get(),  font=("Arial", 11, BOLD, ITALIC), fg='black', bg='white')
        gLabel2.place(x=45, y=350)

        def codigoBoton3():
        
            Ejercicios()

        botonInstru=Button(self.ventanita2, text="RUTINAS", command=codigoBoton3, bg='paleturquoise', fg='black')
        botonInstru.place(x=55, y=420)


        self.ventanita2.mainloop()
