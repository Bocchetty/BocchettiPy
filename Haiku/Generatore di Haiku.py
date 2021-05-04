import os
import random
import tkinter

os.chdir('BocchettiPy\Haiku')

with open('Versi da 5.txt') as f1, open('Versi da 7.txt') as f2:
    for line1, line2, line3 in zip(f1, f2):
        print(line1+line2+line3)

def istruzioni():
 messagebox.showinfo('istruzioni','cliccare il bottone in basso per generare automaticamente l Haiku?')
root=Tk()
root.geometry('600x600')
root.title("GENERATORE DI HAIKU AUTOMATICO")
lbl=Label(root,text="Benvenuto nel generatore automatico di Haiku!", font=(20))
lbl.pack()
b=Button(root, text="Cliccami per le istruzioni d'uso", command=istruzioni)
b.pack()
root.mainloop()
