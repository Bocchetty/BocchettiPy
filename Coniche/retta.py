# La classe retta

import Coniche
import math

class retta(Coniche.Coniche):
            
    def __init__subclass__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        
        if(tipo == "param"):
            super().__init__(self, tipo = "punti", p1 = None, p2 = None, p3 = None, p4 = None)
              
        elif(tipo == "punti"):
            super().__init__(self, tipo = "punti", p1 = None, p2 = None, p3 = None, p4 = None) 

        elif(tipo == "coeff"):
            self.__x3 = int(p1)
            self.__y3 = int(p2)
            self.__m1 = int(p3)
            self.__punti = []
            self.__a = self.__m1
            self.__b = -1
            self.__c = (self.__m1 * -self.__x3) + self.__y3
            print("a = ", self.__a,',', "b = ", self.__b,',', "c = ",self.__c)

    def Implicita(self):
        if self.__b == 0:
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__c} = 0"       
        elif self.__a == 0:
            return f"\nForma implicita dell'equazione:\n {self.__b}y + {self.__c} = 0"    
        elif self.__c == 0:
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__b}y = 0"    
        else:   
            return f"\nForma implicita dell'equazione:\n {self.__a}x + {self.__b}y + {self.__c} = 0 "

    def Esplicita(self):
        if self.__b == 0:
            return f"\nForma esplicita dell'equazione: \n L'equazione è impossibile"
        elif self.__a == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__c / self.__b}"
        elif self.__c == 0:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__a / self.__b}"
        else:
            return f"\nForma esplicita dell'equazione: \n y = {-self.__a / self.__b}x + {-self.__c / self.__b}"
    
    def m(self):
        if self.__b == 0:
            return None
        else:
            return -self.__a / self.__b
    
    def trovaY(self, x):
        self.__x = float(x)
        return -self.__a * self.__x / self.__b + (-self.__c / self.__b)

    def punti(self, K, H):
        self.__K = int(K)
        self.__H = int(H)
    
        for self.__K in range (self.__H):
            tupla = (self.x, (-self.__a * self.x) / self.__b + (-self.__c / self.__b))
            self.__x = self.__x + 1
            self.__punti.append(tupla)
        return self.__punti      


    def instersezione(self, a1 , b1 , c1):
        self.__a1 = float(a1)
        self.__b1 = float(b1)
        self.__c1 = float(c1)
        if (-self.__b / self.__a) == (-self.__b1 / self.__a1):
            if self.__c == self.__c1:
                return self.__punti
            else:
                return None
        elif self.__c == self.__c1:
            return (0, self.__c)
        else:
            return ({((-self.__c / self.__b)+(self.__c1 / self.__b1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))}, {((-self.__b / self.__c)+(self.__b1 / self.__c1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))})
    
    def fascio_parallelo(self):
        if self.__b==0:
            return f"x = k"
        else:
            return f"y = {-self.__a / self.__b}x + q"

valori = retta (input('tipo = ' ), input('valore 1 = ' ), input('valore 2 = ' ), input('valore 3 = ' ), input('valore 4 = ' ))
print(valori.Implicita())
print(valori.Esplicita())
print("Coefficiente angolare: ", valori.m())
print("y=",valori.trovaY(input('x = ')))
risposta = input("Vuoi saprete tutti i punti appartenenti alla retta nell'intervallo ?")
if risposta == 'si':
    print("Le coordinate dei punti appartenenti alla retta sono:", valori.punti(input('inizio intervallo = '), input('fine intervallo = ')))
else:
    pass
print("I punti di intersezione delle due rette sono:", valori.instersezione(input('a1 = ' ), input('b1 = ' ), input('c1 = ' )))
print("L'equazione del fascio è:", valori.fascio_parallelo())