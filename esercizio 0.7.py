from os import startfile
from guizero import *
from random import *
import numpy as np
import matplotlib.pyplot as plt
import string


app = App(title="Esecutore di file", width=500, height=300, bg="#f4d742")

file = Text(app, text="Inserisci il nome del file:")
filename = TextBox (app, width=50)

def tasto1():
    output= s= str(filename)
    output= l= list (s)
    output= g= l[28:44]
    output= f= ''.join(g)
    output= startfile(f)

output = TextBox (app, width=80, height=10, multiline= True)
p1 = PushButton(app,text='Esegui file',command=tasto1)


p1.bg = "#41f465"

output.bg = "#ccc222"

app.display()
