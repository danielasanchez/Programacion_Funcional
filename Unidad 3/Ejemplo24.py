# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""

from tkinter import *

def obtener():
    print(opcion.get())
    opcion.set(None)
    etiqueta2.set("atributo hijo")

def update():
    clase = opcion.get()
    if clase==1:
        etiqueta2.set("Padecimientos")
    elif clase == 2:
        etiqueta2.set("Especialidad")
    
    
principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")

#variable de control String, Int, Double, Boolean
opcion=IntVar() 
#se le establece una opcion por default
opcion.set(4)
etiqueta1 = StringVar()
etiqueta1.set("Nombre")
etiqueta2 = StringVar()
etiqueta2.set("atributo hijo")

label1 = Label(principal,  font=("Arial",16,"bold"),text="Respuesta:")
label1.pack()
label1.config(width=10,bg="gray",pady=20)

opcion1 = Radiobutton(principal,text="Paciente",
                      font=("Arial",16,"bold"),
                      bg="gray",variable=opcion,value=1,
                      command=update).pack()
opcion2 = Radiobutton(principal,text="Medico",
                      font=("Arial",16,"bold"),
                      bg="gray",variable=opcion,value=2,
                      command=update).pack()



label2 = Label(principal, textvariable=etiqueta1)
label2.pack()
label2.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))

label3 = Label(principal, textvariable=etiqueta2)
label3.pack()
label3.config(width=20,bg="gray",pady=5, font=("Arial",16,"bold"))


boton1 = Button(principal, text="Obtener", bg="gray",
                command=obtener,
                activebackground="yellow",
                activeforeground="red",
                font=("Arial",16,"bold"),
                #state=DISABLED
                )

boton1.pack()
boton1.config(pady=10,width=10)




principal.mainloop()

