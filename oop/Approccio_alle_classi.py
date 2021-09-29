#Primo approccio a classi ed oggetti

class auto:

    # Attributi di Classe
    garanzia = 1
    assicurazione = True
    optional = False
    parcoAuto = 0

    #Metodo costruttore
    def __init__(self,proprietario, marca, modello, cilidrata, cavalli, colore):

        # Attributi di Istanza
        self.proprietario = proprietario
        self.marca = marca
        self.modello = modello
        self.cilindrata = cilidrata
        self.cavalli = cavalli
        self.colore = colore
        
        auto.parcoAuto +=1

    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda di "{self.proprietario}"\n Marca: {self.marca}\n Modello: {self.modello}\n Cilindrata: {self.cilindrata}\n Cavalli: {self.cavalli}\n Colore: {self.colore}\n Optional: {self.optional}\n Assicurazione: {self.assicurazione}\n Garanzia: {self.garanzia}'    

giovanni = auto("Giovanni","Ford","Fiesta",1500, 160, "rosso")
marco = auto("Marco","Fiat","Bravo",2500, 200, "verde")
paolo = auto("Paolo", "Fiat", "Panda", 1500, 150, "blu")

giovanni.garanzia += 2
paolo.garanzia += 1
marco.optional +=1

print("Il tipo di variabile costruita è:")
print(giovanni)
print(marco)
print(paolo)

print("\nSchede disponibili:")
print (giovanni.scheda())
print (marco.scheda())
print (paolo.scheda())
print("\nAuto totali: ",auto.parcoAuto)
