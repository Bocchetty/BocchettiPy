from tkinter import*
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
from csv import reader
from random import randint as rd

root= Tk()
root.geometry('600x600')
root.title("GENERATORE DI HAIKU AUTOMATICO")
root.configure(background="#00ffa2")
root.resizable(False, False)

T = Text(root, height = 4, width = 15, relief= SUNKEN, state= DISABLED)

frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

with open('Haiku_coding.csv', 'r') as csv_file:
     csv_reader = reader(csv_file)
     colonne = list(csv_reader)

lista1= []
lista2= []
lista3= []

for i in colonne:
    lista1.append(i[0])
    lista2.append(i[1])
    lista3.append(i[2]) 

quinario1=lista1[rd(0,9)]
settenario1=lista2[rd(0,9)]
quinario2=lista3[rd(0,9)]


def istruzioni():
 messagebox.showinfo('istruzioni','cliccare il bottone in basso per generare automaticamente l Haiku')
 
def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))

def testo():
    l= Label(T, text= quinario1)
    m= Label(T, text= settenario1)
    n= Label(T, text= quinario2)
    l.pack()
    m.pack()
    n.pack()

lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", fg='#004466', font=("times new roman", 20), background="#00ffa2")
tasto1=Button(root,text="Clicca qui per le istruzioni d'uso", fg= '#004466', command=istruzioni, font=("georgia", 15), background="#00ffa2")
tasto2=Button(bottomframe,text="Clicca qui per generare un Haiku", fg= '#004466', font=("georgia", 15), background="#00ffa2", command=testo)

menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="Istruzioni", command= istruzioni)
filemenu.add_command(label="Salva", command=onSave)
filemenu.add_command(label="Chiudi", command=root.quit)

menubar.add_cascade(label="Impostazioni", menu=filemenu)

root.config(menu=menubar)

lbl.pack()
T.pack()
tasto1.pack()
tasto2.pack()

root.mainloop()