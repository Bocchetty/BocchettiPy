import tkinter as tk
from tkinter import*
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
import csv
from random import randint as rd

root= Tk()
finestra= tk.Canvas(root, width = 600, height = 300, bg="#00ffa2")
root.configure(background="#00ffa2")
root.title("GENERATORE DI HAIKU AUTOMATICO")
finestra.pack(side= BOTTOM)

finestra2= tk.Canvas(root, width = 200, height = 120, bg="#00ffa2")
finestra2.pack()
finestra.create_window(300,140, window=finestra2)

quinario= finestra2.create_text(100,30, font= ("georgia", 20))
settenario= finestra2.create_text(100,60, font= ("georgia", 20))
quinario2= finestra2.create_text(100,90, font= ("georgia", 20))

a = open("Haiku_coding.csv")
line = csv.reader(a)
v1 = list(line)

b = open("Haiku_coding.csv")
line = csv.reader(b)
v2 = list(line)

c = open("Haiku_coding.csv")
line = csv.reader(c)
v3 = list(line)


def istruzioni():
 messagebox.showinfo('istruzioni','cliccare il bottone in basso per generare automaticamente l Haiku')

def autori():
 messagebox.showinfo('Autori','Arcione Vittoria, Biasi Luca, Bocchetti Francesco, Catalano Giovanni')
 
def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Pdf",".pdf"),("txt",".txt"))))

def generatore(side=BOTTOM):
    
    verso1=v1[rd(0, 9)]
    verso2=v2[rd(0, 9)]
    verso3=v3[rd(0, 9)]
    
    finestra2.itemconfig(quinario, text=str(verso1))
    finestra2.itemconfig(settenario, text=str(verso2))
    finestra2.itemconfig(quinario2, text=str(verso3))



lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", fg='#004466', font=("times new roman", 20), background="#00ffa2")

tasto=Button(root,text="Clicca qui per generare un Haiku", fg= '#004466', font=("georgia", 15), background="#00ffa2", command=generatore)
finestra.create_window(300, 50, window=tasto)


menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="Istruzioni", command=istruzioni)
filemenu.add_command(label="Copia", command=onSave)
filemenu.add_command(label="Autori", command=autori)
filemenu.add_command(label="Chiudi", command=root.quit)


menubar.add_cascade(label="Impostazioni", menu=filemenu)

root.config(menu=menubar)

lbl.pack()
tasto.pack()

root.mainloop()

#creare 3 file txt.     verso1=l1(rd(0,len(i)) for i in a),verso2=l2(rd(0,len(i)) for i in b),verso3=l3(rd(0,len(i)) for i in c)