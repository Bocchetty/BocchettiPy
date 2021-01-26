#Phyton module equazione
print ("questo programma restituisce il risultato dell'equazione ax+b=0")
a= input("Inserisci un valore da assegnare ad a:")
b= input("inserisci un valore da assegnare ad b:")
def equazione (a, b):
    return -a/b
print ("x=",equazione)


#Phyton module numero maggiore
print ("questo programma restituisce il numero maggiore tra quelli inseriti")
numero= (input("inserisci un numero:"))
numero2= (input("inserisci un numero:"))
numero3= (input("inserisci un numero:"))
list=[numero,numero2,numero3]
print ("Il numero massimo è "+(max(list)))


#Phyton module scambio
print ("questo programma inverte il valore di due variabili")
numero4= (input("inserisci un numero:"))
numero5= (input("inserisci un numero:"))
def swap (numero4, numero5):
    return