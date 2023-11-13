prezzi_prodotti=(
    ("Mela",("Lunedi",1.0),("Martedi",1.2),("Mercoledi",1.1),("Giovedi",5.0),("Venerdi",1.2),("Sabato",1.1),("Domenica",1.4)),
    ("Banana",("Lunedi",0.8),("Martedi",0.9),("Mercoledi",0.7),("Giovedi",3.0),("Venerdi",1.0),("Sabato",2),("Domenica",1.0)),
    ("Fragola",("Lunedi",0.3),("Martedi",0.9),("Mercoledi",0.7),("Giovedi",3.0),("Venerdi",12.0),("Sabato",2),("Domenica",12.0))

)



def medioinserito(tupla,nome):
    prezzo_media=0
    cont=0
    for prodotto,*altro in tupla:
        if(prodotto==nome):
            for giorno,prezzo in altro:
                prezzo_media+=prezzo
                cont+=1
    return prezzo_media/cont


def prezzoMedioTot(tupla):
    prezzo_media=0
    cont=0
    for prodotto,*altro in tupla:
            for giorno,prezzo in altro:
                prezzo_media+=prezzo
                cont+=1
    return prezzo_media/cont


def prezzoMax(tupla,nome):
    prezzoMassimo=0
    giornoMax=""
    for prodotto,*altro in tupla:
        if(prodotto==nome):
            for giorno,prezzo in altro:
               if(prezzoMassimo<prezzo):
                    prezzoMassimo=prezzo
                    giornoMax=giorno
    return (prezzoMassimo,giornoMax)




def prezzoMin(tupla):
    prezzoMinTot=5
    giornoMin=""
    prodottoMin=""
    array=[]
    for prodotto,*altro in tupla:
        for giorno,prezzo in altro:
            if(prezzoMinTot>prezzo):
                prezzoMinTot=prezzo
                giornoMin=giorno
                prodottoMin=prodotto
                ritorn=(prodottoMin,prezzoMinTot,giornoMin)
                array.append(ritorn)
    return array


nome=(input("Inserisci prodotto: "))

nomeprodottomax=(input("Inserisci prodotto per vedere massimo prezzo e in quale giorno: "))


print("Prezzo medio :",nome," ",medioinserito(prezzi_prodotti,nome))

print("Prezzo medio totale: ",prezzoMedioTot(prezzi_prodotti))

prezzoM,g=prezzoMax(prezzi_prodotti,nomeprodottomax)
print("Prezzo massimo di ",nomeprodottomax,": ",prezzoM," giorno: ",g)
print("Prezzo minimo: ",prezzoMin(prezzi_prodotti))












