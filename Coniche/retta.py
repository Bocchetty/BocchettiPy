# La classe retta

class Retta:
    
    #Metodo costruttore
    def __init__(self, eqImplicita, eqEsplicita, coordinate=tuple):
        #Attributi di istanza
        self.__eqImplicita = eqImplicita
        self.__eqEsplicita = eqEsplicita
        self.__coordinate = coordinate
        
        Retta.numeroRette +=1
    
    def equazione_esplicita(self):
        return f'Consegna:\n  Equazione esplicita:\n{self.eqEsplicita}\n Equazione implicita:\n{self.eqImplicita}\n Coordinate:\n{self.Coordinate}'

a = float(input("Il valore x è "))
b = float(input("Il valore y è "))
c = float(input("Il termine noto è "))

#m=float(yb-ya)/(xb-xa)

y = (-a / b) 
z = (-c / b)
eq_1 = "y =" , y ,'x' , '+' , z
eq_2 = a,'x', '+', b,'y', '+' , c , = 0

coordinate_1 = (0,z)
coordinate_2 = (y,(y + z))
coordinate_3 = coordinate_1 , coordinate_2
equazione_uno = Retta(eq_1, eq_2, coordinate_3) 
print(equazione_uno.equazione_esplicita())
print("\nRette totali: ",Retta.numeroRette)