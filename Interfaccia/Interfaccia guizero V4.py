from os import chdir, remove, startfile
from guizero import *
from random import *
import matplotlib.pyplot as plt


app = App(title="Esecutore di file", width=600, height=600, bg="#f4d742")

file = Text(app, text="Inserisci il nome del file:")
filename = TextBox (app, width=50)

def tasto1():
    output= f= filename.value
    output= startfile(f)


def tasto2():
    output=grafico1= Picture(app, image= "grafico.png")

p1 = PushButton(app,text='Esegui file',command=tasto1)

p2 = PushButton(app,text='Mostra Grafico',command=tasto2)

p1.bg = "#41f465"
p2.bg = "#41f465"

app.display()