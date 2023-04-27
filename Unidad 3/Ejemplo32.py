# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 00:48:54 2023

@author: Daniela
"""
#grid

from tkinter import *


principal = Tk()
principal.title("Mi primer ventana")
principal.geometry("380x280+400+200")
principal.config(bg="gray")


label1 = Label(principal, text="Soy una etiqueta")
# relx, rely = eslaca del 0 al 1
label1.grid(row=0,column=0)

label2 = Label(principal, text="Soy otra etiqueta")
label2.grid(row=1,column=1)


label3 = Label(principal, text="Soy otra etiqueta")
label3.grid(row=2,column=2)


principal.mainloop()

