prezzi_prodotti=(
    ("Mela","Lunedi",1.0),
    ("Mela","Martedi",1.2),
    ("Mela","Mercoledi",1.1),
    ("Banana","Lunedi",0.8),
    ("Banana","Martedi",0.9),
    ("Banana","Mercoledi",0.7),
    ("Mela","Lunedi",5.0),
    ("Mela","Martedi",1.2),
    ("Mela","Mercoledi",1.1),

)

def prezzo_medio(tupla,giorno,nome):
    price=0
    cont=0
    for prodotto,day,prezzo in tupla:
        if(nome==prodotto and giorno==day):
            price+=prezzo
            cont+=1
    return price/cont
        





nome=input("Nome del prodotto : ")
giorno=input("Giorno della settimana: ")
print(prezzo_medio(prezzi_prodotti,giorno,nome))

