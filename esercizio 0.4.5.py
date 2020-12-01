print ("questo programma data una stringa determina il carattere che compare più spesso e il numero di ripetizioni ")
frase= input("scrivi una frase: ")
Carattere= {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
Conteggio = 0
for Carattere in frase:
  if Carattere == 'Carattere':
    Conteggio = Conteggio + 1
Carattere= Conteggio
print ("Il carattere che compare più spesso è",(max(Carattere)) , "e si ripete", (max(Conteggio)), "volte")