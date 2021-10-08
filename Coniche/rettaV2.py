# La classe retta


class retta:
    

    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__punti = []


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
            return f"\nCoefficiente angolare: \n Il coefficiente angolare non è definito; la retta è parallela all'asse y"
        else:
            return f"\nCoefficiente angolare: \n m = {-self.__b / self.__a}"
    
    def trovaY(self, x):
        return f"\n Y: \n y = {-self.__a * x / self.__b + (-self.__c / self.__b)}"


    def punti(self, N, M, x):
        self.N = N
        self.M = M
    
        for self.N in range (self.M):
            tupla = (x, (-self.__a * x) / self.__b + (-self.__c / self.__b))
            x = x + 1
            self.__punti.append(tupla)
        return f"\n Le coordinate dei punti appartenenti alla retta sono: \n {self.__punti}"         


    def instersezione(self, a1 , b1 , c1):
        self.__a1 = float(a1)
        self.__b1 = float(b1)
        self.__c1 = float(c1)
        if (-self.__b / self.__a) == (-self.__b1 / self.__a1):
            if self.__c == self.__c1:
                return f"\nLe rette sono coincidenti \n {self.__punti}"
            else:
                return f"Null"
        elif self.__c == self.__c1:
            return f"\nIl putnto di incontro delle due rette è: {self.__c}y" 
        else:
            return f"\nLe rette sono incidenti e le coordinate del punto d'incidenza sono: ({((-self.__c / self.__b)+(self.__c1 / self.__b1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))}, {((-self.__b / self.__c)+(self.__b1 / self.__c1))/((-self.__b / self.__a)+(self.__b1 / self.__a1))})"

valori = retta(2, 3, 4)
print(valori.Implicita())
print(valori.Esplicita())
print(valori.m())
print(valori.trovaY(2))
print(valori.punti(0, 600, -300))
print(valori.instersezione(1, 2, 5))