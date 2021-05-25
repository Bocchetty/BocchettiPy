import tkinter as tk
from tkinter import*
from tkinter import Menu
from tkinter import messagebox
from csv import reader
from random import randint as rd
from tkinter.filedialog import asksaveasfile

#Interfaccia e layout interno
root= Tk()
finestra= tk.Canvas(root, width = 600, height = 300, bg="#00ffa2")
root.configure(background="#00ffa2")
root.resizable(False, False)
root.title("GENERATORE DI HAIKU AUTOMATICO")
finestra.pack(side= BOTTOM)

finestra2= tk.Canvas(root, width = 400, height = 120, bg="#00ffa2")
finestra2.pack()
finestra.create_window(300,140, window=finestra2)

quinario= finestra2.create_text(200,30, font= ("georgia", 20))
settenario= finestra2.create_text(200,60, font= ("georgia", 20))
quinario2= finestra2.create_text(200,90, font= ("georgia", 20))

#Lettore del file
with open('Haiku_coding.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = reader(csv_file)
    colonne = list(csv_reader)
lista1= []
lista2= []
lista3= []

for i in colonne:
    lista1.append(i[0])
    lista2.append(i[1])
    lista3.append(i[2]) 

l1= (len(lista1)-1)
l2= (len(lista2)-1)
l3= (len(lista3)-1)

#Funzioni
def istruzioni():
 messagebox.showinfo('Istruzioni','Cliccare il bottone in basso per generare automaticamente l Haiku. Per rigenerare interamente l Haiku ricliccare il bottone. Per rigenerare solamente un verso dell Haiku, cliccare il bottone alla sua sinistra.')

def autori():
 messagebox.showinfo('Autori','Arcione Vittoria, Biasi Luca, Bocchetti Francesco, Catalano Giovanni')

def copia():
    files = [('File di testo', '*.txt'),
             ('Pdf', '*.pdf')]
    file = asksaveasfile(filetypes = files, defaultextension = files)

def generatore0(side=BOTTOM):
    
    verso1=lista1[rd(0, l1)]
    verso2=lista2[rd(0, l2)]
    verso3=lista3[rd(0, l3)]
    
    finestra2.itemconfig(quinario, text=str(verso1))
    finestra2.itemconfig(settenario, text=str(verso2))
    finestra2.itemconfig(quinario2, text=str(verso3))
    
def generatore1(side=BOTTOM):
    verso1 = lista1[rd(0,l1)]
    finestra2.itemconfig(quinario, text=str(verso1))

def generatore2(side=BOTTOM):
    verso2 = lista2[rd(0,l2)]
    finestra2.itemconfig(settenario, text=str(verso2))

def generatore3(side=BOTTOM):
    verso3 = lista3[rd(0,l3)]
    finestra2.itemconfig(quinario2, text=str(verso3))

#Label e bottoni
lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", fg='#004466', font=("times new roman", 20), background="#00ffa2")

tasto=Button(root,text="Clicca qui per generare un Haiku", fg= '#004466', font=("georgia", 15), background="#00ffa2", command=generatore0)
finestra.create_window(300, 50, window=tasto)

tasto1= tk.Button(root, text="Cambia", command=generatore1, font= ("georgia", 10), background="#00ffa2")
finestra.create_window(50, 110, window=tasto1)

tasto2= tk.Button(root, text="Cambia", command=generatore2, font= ("georgia", 10), background="#00ffa2")
finestra.create_window(50, 140, window=tasto2)

tasto3= tk.Button(root, text="Cambia", command=generatore3, font= ("georgia", 10), background="#00ffa2")
finestra.create_window(50, 170, window=tasto3)

#Menu
menubar= Menu(root)

filemenu= Menu(menubar)
filemenu.add_command(label="Istruzioni", command=istruzioni)
filemenu.add_command(label="Autori", command=autori)
filemenu.add_command(label="Copia", command=copia)
filemenu.add_command(label="Chiudi", command=root.quit)

menubar.add_cascade(label="Impostazioni", menu=filemenu)

root.config(menu=menubar)

lbl.pack()
tasto.pack()

root.mainloop()