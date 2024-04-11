import pprint
pp=pprint.PrettyPrinter(indent=4)
#1 09.35
campionati={
    "Giuseppe Gullo":[("Corsa campestre",(40,21,0),"Juniores mas"),("Corsa 100mt",(0,12,0),"Juniores mas"),("Corsa 200mt",(0,29,19),"Juniores mas")],
    "Antonia Barbera":[("Corsa campestre",(0,39,11),"Juniores fem"),("Corsa 100mt",(0,18,0),"Juniores fem"),("Corsa 200mt",(0,0,0),"Juniores fem")],
    "Nicola Esposito":[("Corsa campestre",(0,43,22),"Juniores mas"),("Corsa 100mt",(0,14,0),"Juniores mas"),("Corsa 200mt",(0,36,19),"Juniores mas")]

}
#2,3,4 09,57
#5,6,7 10,23


#punto2
def AggiungereMioNome():
    nominativo="Chiril Bogaiciuc"
    campionati[nominativo]=[("Corsa campestre",(10,1,0),"Juniores mas"),("Corsa 100mt",(2,1,10),"Juniores mas"),("Corsa 200mt",(1,1,0),"Juniores mas")]

#punto3
def aggiungereDisciplina():
    for nominativi,valori in campionati.items():
        minuti=int(input("Inserisci minuti per corsa ad ostacoli 400mt per "+nominativi))
        secondi=int(input("Inserisci secondi per corsa ad ostacoli 400mt per "+nominativi))
        centesimi=int(input("Inserisci centesimi per corsa ad ostacoli 400mt per "+nominativi))
        categoria=input("Inserisci categoria: ")
        if(nominativi=="Chiril Bogaiciuc"):
             campionati[nominativi].append(("Corsa ad ostacoli 400mt",(minuti,1,centesimi),categoria))
        else:
            campionati[nominativi].append(("Corsa ad ostacoli 400mt",(minuti,secondi,centesimi),categoria))
       


def stampatuplaGiuseppe():
    pp.pprint(campionati["Giuseppe Gullo"])

def stampla200MtNicola():
    for corsa,(minuti,secondi,centesimi),categoria in campionati["Nicola Esposito"]:
        if(corsa=="Corsa 200mt"):
            print(corsa+"\nMinuti: ",minuti,"\nSecondi: ",secondi,"\nCentesimi: ",centesimi,"\nCategoria: "+categoria)

def tempo100MtAntonio():
     for corsa,(minuti,secondi,centesimi),categoria in campionati["Antonia Barbera"]:
        if(corsa=="Corsa 100mt"):
            print("\nMinuti: ",minuti,"\nSecondi: ",secondi,"\nCentesimi: ",centesimi)

def tempoMassimo():
    tempi=[]
    for i in campionati.keys(): 
        for corsa,tupla,categoria in campionati[i]:
            if(corsa=="Corsa 200mt"):
                tempi.append(tupla)
                
    max_tempo = max(tempi)
    print("Tempo massimo è: ",max_tempo)


def tempoMinimo():
    tempi=[]
    studente=[]
    for i in campionati.keys(): 
        for corsa,tupla,categoria in campionati[i]:
            if(corsa=="Corsa 100mt"):
                tempi.append(tupla)
                studente.append(i)

    min_tempo = min(tempi)

    for i in campionati.keys(): 
        for corsa,tupla,categoria in campionati[i]:
            if(corsa=="Corsa 100mt"):
                if(tupla==min_tempo):
                    studenteM=i

    print("Tempo minimo è: ",min_tempo,"\nStudente: ",studenteM)
 

def mediatempiCorsaJuniores():
    totale_minuti = 0
    totale_secondi = 0
    totale_centesimi = 0 
    totale_tempi=0


    for i in campionati.keys(): 
        for corsa,(minuti,secondi,centesimi),categoria in campionati[i]:
            if(categoria=="Juniores mas"):
                totale_minuti+=minuti
                totale_secondi+=secondi
                totale_centesimi+=centesimi
                totale_tempi+=1

    media_minuti = totale_minuti / totale_tempi
    media_secondi = totale_secondi / totale_tempi
    media_centesimi = totale_centesimi / totale_tempi

    print(f"Tempo medio di gara: {media_minuti:2f}:{media_secondi:2f}.{media_centesimi:02f}")

def aggiungereaaDizionario():
    nome=input("Insersici nome: ")
    for i in campionati.keys():
        if(nome==i):
            print("Nome già esiste")
            return
        

    for corsa,(minuti,secondi,centesimi),categoria in campionati["Antonia Barbera"]:
        minutiIns=int(input(f"Inserisci minuti di {corsa} : "))
        secondiIns=int(input(f"Inserisci minuti di {corsa} : "))
        centesimiIns=int(input(f"Inserisci minuti di {corsa} : "))
        categoriaIns=input("Inserisci categoria: ")
        campionati[nome]=((corsa,(minutiIns,secondiIns,centesimiIns),categoriaIns))
    
    





AggiungereMioNome()


while(True):
    scelta=int(input(
"""
1.Aggiungi la 4 disciplina sportiva 'corsa ad ostacoli 400 mt' 
2.Stampa la tupla con le informazioni sulla disciplina sportiva corsa campestre per l'atleta Giuseppe Gullo
3.Stampa i singoli valori della tupla con le informazioni sulla disciplina corsa 200 mt. per Nicola Esposito
4.Stampa il tempo di Antonia Barbera nella corsa 100 mt separando min,sec,cent.
5.Stampa il tempo massimo riportato nella corsa 200mt della categoria Juniores mas
6.Stampa il tempo minimo riportato nella corsa 100mt. della categoria Juniores mas. e lo studente che lo ha realizzato 
7.Stampa la media dei tempi nella corsa campestre della categoria Juniores mas 
8.Realizzare le opportune funzioni per aggiungere al dizionario i dati validi relativi alle 4 gare per un nuovo atleta
9.Visualizzare tutto dizionario
"""))
    print("\n")
    if(scelta==1):
        aggiungereDisciplina()
    elif(scelta==2):
        stampatuplaGiuseppe()
    elif(scelta==3):
        stampla200MtNicola()
    elif(scelta==4):
        tempo100MtAntonio()
    elif(scelta==5):
        tempoMassimo()
    elif(scelta==6):
        tempoMinimo()
    elif(scelta==7):
        mediatempiCorsaJuniores()
    elif(scelta==8):
        aggiungereaaDizionario()
    elif(scelta==9):
        pp.pprint(campionati)






