from csv import reader
from random import randint as rd

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
print(quinario1)
print(settenario1)
print(quinario2)