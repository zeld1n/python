def mediovoti(dizionario):
    media=0
    cont=0
    nome=input("Inserisci il nome dello studente di cui vuoi calcolare la media: ")
    while nome=="":
        nome=input("Inserisci il nome dello studente di cui vuoi calcolare la media: ")
        
    for key in dizionario.keys():
        if(nome==key):
            for vet in dizionario[key]:
                media+=vet
                cont+=1
            return media/cont,nome
        else:
            print("Studente non presente: ")
            return mediovoti(dizionario)
            #quit()
    

numeroStud=int(input("Numero di studenti: "))
if(numeroStud<=0):
    print("Hai inserito numero non valido :) ")
    quit()
voti={}
for _ in range(numeroStud):
    nomeStud=input("Inserisci nome dello studente: ")
    while nomeStud=="": 
        nomeStud=input("Inserisci nome dello studente: ")
        
    mate=int(input("Inserisci il voto in Matematica: "))
    fisica=int(input("Inserisci il voto in fisica: "))
    chimica=int(input("Inserisci il voto in chimica: "))
    voti[nomeStud]=[mate,fisica,chimica]

media,nome=mediovoti(voti)
print("La media dei voti di: ",nome," è: ",media )  