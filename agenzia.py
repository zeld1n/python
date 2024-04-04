import pprint
pp=pprint.PrettyPrinter(indent=4)

def popola():
    n=int(input("Inserisci numero appartamenti: "))
    for _ in range(n):
        codice=int(input("Inserisci codice: "))
        for c in appartmaneti.keys():
            while(codice==c):
                print("Appartamento già presente")
                codice=int(input("Inserisci codice: "))

        indirizzo=input("Inserisci indrizzo: ")
        posti=int(input("Inserisci numero di posti: "))
        prezzo=float(input("Inserisci prezzo: "))
        notti=int(input("Inserisci numero dei notti: "))
        totale=prezzo*notti
        appartmaneti[codice]=[indirizzo,posti,prezzo,notti,totale]
       

def aggiungi_Un_appartamento():
    codice=int(input("Inserisci codice: "))
    for c in appartmaneti.keys():
        while(codice==c):
            print("Appartamento già presente")
            codice=int(input("Inserisci codice: "))

    indirizzo=input("Inserisci indrizzo: ")
    posti=int(input("Inserisci numero di posti: "))
    prezzo=float(input("Inserisci prezzo: "))
    notti=int(input("Inserisci numero dei notti: "))
    totale=prezzo*notti
    appartmaneti[codice]=[indirizzo,posti,prezzo,notti,totale]

def elimina_un_appartamento():
    codice=int(input("Inserisci codice: "))
    for c in appartmaneti.keys():
        if(codice==c):
            del appartmaneti[codice]
            return appartmaneti
    print("Codice non esiste ")
    
def mostra_dati_appartamento():
    codice=int(input("Inserisci codice: "))
    for c in appartmaneti.keys():
        if(codice==c):
            print(appartmaneti[codice])
            return appartmaneti
    print("Codice non esiste ")

def mostra_dati_tuttiAppartamenti():
    pp.pprint(appartmaneti)

def modifica_dati():
    codice=int(input("Inserisci codice: "))
    for c in appartmaneti.keys():
        if(codice==c):
            indirizzo=input("Inserisci indrizzo: ")
            posti=int(input("Inserisci numero di posti: "))
            prezzo=float(input("Inserisci prezzo: "))
            notti=int(input("Inserisci numero dei notti: "))
            totale=prezzo*notti
            appartmaneti[codice]=[indirizzo,posti,prezzo,notti,totale]
            return appartmaneti
    print("Codice non esiste: ")


def calcola_totale():
    prezzoMassimo=0
    prezzototale=0
    #posizione
    for k,(indirizzo,posti,prezzo,notti,totale) in appartmaneti.items():
        prezzototale+=totale
        if(prezzoMassimo<totale):
            prezzoMassimo=totale
            posizione=k
    print("Totale degli incassi: ",prezzototale,"\nl'incasso massimo: ",appartmaneti[posizione])        




appartmaneti={1:["Via rossi 23",3,55,2,110],
              2:["Via Verdi 32",4,65,4,260],
              3:["Via Bianchi 19",5,75,2,150],
              }



while(True):
    print("\n0.Esci"
        "\n1.Popola"
        "\n2.Aggiungi"
        "\n3.Elimina"
        "\n4.Cerca"
        "\n5.Mostra tutti"
        "\n6.Modifica"
        "\n7.Calcolo totale e massimo")

    scelta=int(input())
    if(scelta==1):
        popola()
    elif(scelta==2):
        aggiungi_Un_appartamento()
    elif(scelta==3):
        elimina_un_appartamento()
    elif(scelta==4):
        mostra_dati_appartamento()
    elif(scelta==5):
        mostra_dati_tuttiAppartamenti()
    elif(scelta==6):
        modifica_dati()
    elif(scelta==7):
        calcola_totale()
    elif(scelta==0):
        break
    






