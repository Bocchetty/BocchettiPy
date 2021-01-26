from os import startfile
from guizero import *
from random import *
import matplotlib.pyplot as plt

app = App(title="Esecutore di file", width=500, height=600, bg="#f4d742")

file = Text(app, text="Inserisci il nome del file:")
filename = TextBox (app, width=50)

def tasto1():
    output= f= filename.value
    output= startfile(f, "hide")


p1 = PushButton(app,text='Esegui file',command=tasto1)


grafico1= Picture(app, image= "grafico.png")

p1.bg = "#41f465"

app.display()