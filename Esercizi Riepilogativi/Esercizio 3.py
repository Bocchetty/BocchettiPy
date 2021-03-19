from numpy import*
Mario= {"Matematica": 6, "Italiano": 6, "Scienze": 7, "Inglese": 4}
Giovanni= {"Matematica": 4, "Italiano": 6, "Scienze": 5, "Inglese": 7}
Paola= {"Matematica": 9, "Italiano": 6, "Scienze": 8, "Inglese": 8}
M= list(Mario.values())
G= list(Giovanni.values())
P= list(Paola.values())
print ("Media voti Mario", mean(M))
print ("Media voti Giovanni", mean(G))
print ("Media voti Paola", mean(P))