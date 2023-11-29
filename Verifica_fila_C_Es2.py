tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
    ("SquadraC", "SquadraD", 1, 2),
)

def mediagol(tupla):
    media=0
    cont=0
    for sq1,sq2,gol1,gol2 in tupla:
        media+=gol1+gol2
        cont+=2
    return media/cont

def mediagolSquadre(tupla):
    nomesquadra=input("Inserisci nome della squadra :")
    media=0
    cont=0

    for sq1,sq2,gol1,gol2 in tupla:
        if(nomesquadra==sq1):
            media+=gol1
            cont+=1
        if(nomesquadra==sq2):
            media+=gol2
            cont+=1
    return media/cont,nomesquadra

def partitaconpiugol(tupla):
    maxVal=0
    partitaMax=""
    for sq1,sq2,gol1,gol2 in tupla:
        if(maxVal<gol1+gol2):
            maxVal=gol1+gol2
            partitaMax=sq1+" "+sq2
    return partitaMax,maxVal


def partitaconmenogol(tupla):
    minVal=tupla[0][2]+tupla[0][3]
    partitaMin=""
    for sq1,sq2,gol1,gol2 in tupla:
        if(minVal>gol1+gol2):
            minVal=gol1+gol2
            partitaMin=sq1+" "+sq2
    return partitaMin,minVal

def percentuale(tupla):
    sqIns=input("Inserisci squadra: ")
    disputate=0
    vinte=0
    for sq1,sq2,gol1,gol2 in tupla:
        if(sqIns==sq1 or sqIns==sq2):
            disputate+=1
            if(sq1==sqIns and gol1>gol2):
                vinte+=1
            if(sq2==sqIns and gol2>gol1):
                vinte+=1
    return vinte/disputate*100,sqIns







while True:
    print("\n1. media dei gol segnati in tutte le partite")
    print("2. la media dei gol segnati dalla squadra in tutte le partite in cui ha partecipato")
    print("3. la partita con il maggior numero di gol segnati e i relativi puntegg")
    print("4. la partita con il minor numero di gol segnati e i relativi puntegg")
    print("5. la percentuale di partite vinte dalla squadra rispetto al totale delle partite disputate")
    scelta=int(input("\n"))

    if(scelta==1):
        media,nomesquadra=mediagolSquadre(tupla_partite)
        print(f"Media gol {media} di squadra {nomesquadra}")
    if(scelta==2):
        print("Media gol di tutte partite è: ",mediagol(tupla_partite))
    if(scelta==3):
        Maxpartita,maxgol=partitaconpiugol(tupla_partite)
        print(f"Partita tra {Maxpartita} con il maggior numero di gol: ",maxgol)
    if(scelta==4):
        Minpartita,mingol=partitaconmenogol(tupla_partite)
        print(f"Partita tra {Minpartita} con il minor numero di gol: ",mingol)
    if(scelta==5):
        perc,squadraIns=percentuale(tupla_partite)
        print(f"La percentuale {perc} di partite vinte dalla squadra {squadraIns}")
    if(scelta==0):
        break