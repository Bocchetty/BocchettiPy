#Superclasse coniche

import math

class Coniche:
    
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo=="param"):   
            self.__a = p1  
            self.__b = p2
            self.__c = p3
            self.__punti = []
        
        elif(tipo == "punti"):
            self.__x1 = int(p1)
            self.__x2 = int(p2)
            self.__y1 = int(p3)
            self.__y2 = int(p4)
            self.__punti = []
            x_d = (self.__x2 - self.__x1)
            y_d = (self.__y2 - self.__y1)
            MCD = math.gcd(x_d, y_d)
            mcm = (x_d * y_d) / MCD
            self.__a = mcm / x_d
            self.__b = mcm / y_d
            self.__c = (mcm / x_d * -self.__x2) + (mcm / y_d * self.__y2)
            print("a = ", self.__a,',', "b = ", self.__b,',', "c = ",self.__c)
    
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    #def punti(self, K, H):
        self.__K = int(K)
        self.__H = int(H)
    
        for self.__K in range (self.__H):
            tupla = (self.x, (-self.__a * self.x) / self.__b + (-self.__c / self.__b))
            self.__x = self.__x + 1
            self.__punti.append(tupla)
        return self.__punti
        
valori = Coniche (input('tipo = ' ), input('valore 1 = ' ), input('valore 2 = ' ), input('valore 3 = ' ), input('valore 4 = ' ))
#print(valori.punti(input('Inizio intervallo = '), input('Fine intervallo = ')))