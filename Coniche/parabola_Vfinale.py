#La classe parabola

import Coniche

class parabola(Coniche.Coniche):
    
    def __init__(self, tipo, p1, p2, p3, p4):

        if(tipo == "param"):
            super().__init__(tipo, p1, p2, p3, p4)
            self.__a = int(p1)
            self.__b = int(p2)
            self.__c = int(p3)
            self.__punti = []

        elif(tipo == "fuocoDiret"):
            #p1= coordinata x di f
            self.__p1 = int(p1)
            #p2= coordinata y di f
            self.__p2 = int(p2)
            #p3= direttrice
            self.__p3 = int(p3)
            self.__punti = []
            self.__a = 1/(2*self.__p2 - 2*self.__p3)
            self.__b = -2*self.__a * self.__p1
            self.__c = (4*self.__a*self.__p2 + self.__b*self.__b - 1)/(4*self.__a)
        
    def fuoco(self, asse_simmetria = "x"):
     if (asse_simmetria == "x"):
        y = -((self.__b)/((self.__a)*2))
        x = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
        return x,y
        
     elif (asse_simmetria == "y"):
            x =-((self.__b)/((self.__a)*2))
            y = (1-(pow(self.__b,2)-4*self.__a*self.__c))/4*self.__a
            return x,y
    
    def direttrice(self, asse_simmetria = "x"):
     if (asse_simmetria == "x"):
        x= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
        return x
     
     elif (asse_simmetria == "y"):
        y= -1-(pow(self.__b,2)-4*self.__a*self.__c)/4*self.__a
        return y
    
valori = parabola(input('tipo = ' ), input('valore 1 = ' ), input('valore 2 = ' ), input('valore 3 = ' ), input('valore 4 = ' ))
print(valori.fuoco(input('Asse simmetria parallelo a ' )))
print(valori.direttrice(input('Asse simmetria parallelo a ' )))