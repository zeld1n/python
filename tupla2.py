prenotazioni=[]
scelta=""


def aggiungi_prenotazione():
    nome=input("Nome: ")
    data=input("Data di prenotazione: ")
    numeroPersone=int(input("Inserisci numero di persone: "))
    numeroTavolo=int(input("Inserisci numero di tavolo: "))
    tupla=(nome,data,numeroPersone,numeroTavolo)

    return tupla

def rimuovi_prenotazione(array):
    nome=(input("Inserisci nome della prenotazione: "))
    data=(input("Inserisci la data: "))

    for i in range (array):
        if (array[i][0]==nome and array[i][1]== data):
            array.pop(i)
    return array


def tavoli_disponibili(array):
    cont=0
    disponibili=[0,1,2,3,4,5,6,7,8,9,10]
    data=(input("Inserisci giorno per sapere tavoli disponibili: "))
    for i in range (len(array)):
        if(data==array[i][1]):
            disponibili[array[i][3]]=0
            #disponibili.pop(array[i][3])
    return (data,disponibili)


def prenotazioni_cliente(array):
    listaPrenot=[]
    nome=(input("Inserisci nome di un cliente : "))
    for i in range (len(array)):
        if(nome==array[i][0]):
            listaPrenot.append(array[i])
    return (nome,listaPrenot)    

def conto_totale(array):
    giorno=(input("Inserisci giorno che ti interessa : "))
    person=20 #Valore medio di quanto spende una persona 
    tot=0
    final=0

    for nome,data,persone,tavolo in array:
        if(giorno==data):
            tot+=persone
            final=tot*person
    return (giorno,final)
    





while scelta!="no":
    prenotazioni.append(aggiungi_prenotazione())
    scelta=input("Vuoi aggingere? (si/no): ")

scelta=""

while scelta!="no":
    scelta=input("Vuoi rimuovere tavolo? (si/no): ")
    if(scelta=="si"):
        rimuovi_prenotazione(prenotazioni)
data,dispon=tavoli_disponibili(prenotazioni)
print(f"Tavoli disponibili per il {data}",dispon)

nomePrenot,listaPrenot=prenotazioni_cliente(prenotazioni)
print(f"Prenotazioni di {nomePrenot}: ",listaPrenot)

giornoConto,contoFinale=conto_totale(prenotazioni)
print(f"Conto totale per il {giornoConto}: ",contoFinale)


