from tkinter import*
from tkinter import messagebox
from os import close, startfile

root= Tk()
root.geometry('600x600')
root.title("GENERATORE DI HAIKU AUTOMATICO")
root.configure(background="#00ffa2")
root.resizable(False, False)

frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

def istruzioni():
 messagebox.showinfo('istruzioni','cliccare il bottone in basso per generare automaticamente l Haiku')
 
lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", fg='#004466', font=("times new roman", 20), background="#00ffa2")
tasto1=Button(root,text="Clicca qui per le istruzioni d'uso", fg= '#004466', command=istruzioni, font=("georgia", 15), background="#00ffa2")
tasto2=Button(root,text="Clicca qui per generare un Haiku", fg= '#004466', font=("georgia", 15), background="#00ffa2", command=startfile("Generatore_di_Haiku.py"))

lbl.pack()
tasto1.pack()
tasto2.pack()

root.mainloop()