  
from random import randint as rd
import os
import csv
import tkinter as tk
import csv
from tkinter import *
from tkinter import font 

a = open("Haiku_coding.csv")
line = csv.reader(a)
v1 = list(line)

b = open("Haiku_coding.csv")
line = csv.reader(b)
v2 = list(line)

c = open("Haiku_coding.csv")
line = csv.reader(c)
v3 = list(line)


root = Tk()
riquadro = tk.Canvas(root, width = 600, height = 300, bg="dark sea green")
root.title("GENERATORE DI HAIKU")
riquadro.pack()

riquadro2 = tk.Canvas(root, width = 200, height = 120, bg="dark sea green")
riquadro2.pack()
riquadro.create_window(300,140, window=riquadro2)

scritta1 = riquadro2.create_text(100,30, font= ("times", 14, "italic"))
scritta2 = riquadro2.create_text(100,60, font= ("times", 14, "italic"))
scritta3 = riquadro2.create_text(100,90, font= ("times", 14, "italic"))

def genera_haiku(Side=BOTTOM):
    
    verso1 = v1[rd(0,len)]
    verso2 = v2[rd(0,len)]
    verso3 = v3[rd(0,len)]


    riquadro2.itemconfig(scritta1, text=str(*verso1))
    riquadro2.itemconfig(scritta2, text=str(*verso2))
    riquadro2.itemconfig(scritta3, text=str(*verso3))


    #riquadro.place(x=70, y=55)

def cambia_rigo1():
    verso1 = v1[rd(0,len)]
    riquadro2.itemconfig(scritta1, text=str(*verso1))
    

def cambia_rigo2():
    verso2 = v2[rd(0,len)]
    riquadro2.itemconfig(scritta2, text=str(*verso2))
    

def cambia_rigo3():
    verso3 = v3[rd(0,len)]
    riquadro2.itemconfig(scritta3, text=str(*verso3))
    

button1 = tk.Button(root, text="chiudi scheda", command=root.destroy, bg="NavajoWhite2")
riquadro.create_window(560, 15, window=button1)

button2 = tk.Button(root, text="Genera Haiku", command=genera_haiku, font= ("monospace", 12, "bold"), bg= "NavajoWhite2")
riquadro.create_window(300, 50, window=button2)


buttonr1 = tk.Button(root, text="cambia", command=cambia_rigo1, font= ("NavajoWhite2", 7), bg="NavajoWhite2")
riquadro.create_window(185, 110, window=buttonr1)

buttonr2 = tk.Button(root, text="cambia", command=cambia_rigo2, font= ("NavajoWhite2", 7), bg="NavajoWhite2")
riquadro.create_window(185, 140, window=buttonr2)

buttonr3 = tk.Button(root, text="cambia", command=cambia_rigo3, font= ("NavajoWhite2", 7), bg="NavajoWhite2")
riquadro.create_window(185, 170, window=buttonr3)



root.mainloop()