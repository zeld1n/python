


pagella = {
    "studente1": [
        ("Matematica", (7, 2), (8, 1)),
        ("Italiano", (6, 3), (7, 2)),
        ("Inglese", (8, 1), (9, 0)),
    ],
    "studente2": [
        ("Matematica", (5, 5), (5, 2)),
        ("Italiano", (3, 3), (6, 2)),
        ("Inglese", (7, 5), (10, 2)),
    ],

}
def stampaStudentePrimoQuad(pagella):
    nome=input("Inserisci nome del studente :" )
    
    for vettore in pagella.keys():
        if(nome==vettore):
            for vet in pagella[vettore]:
                if(vet[0]=="Matematica"):
                    return vet[1]

def stampaStudenteSecondoQuad(pagella):
    nome=input("Inserisci nome del studente :" )
    materia=input("Inserisci materia:" )
    for keys in pagella.keys():
        if(nome==keys):
            for vet in pagella[keys]:
                if(vet[0]==materia):
                    return vet[1]
                
def stampaMateriaAssenze(pagella):
    materiaMax=" "
    assenzeMax=0

    nome=input("Inserisci nome del studente : ")
    for keys in pagella.keys():
        if(nome==keys):
            for materia,(votoPrimo,assPrimo),(votoSecondo,assSecondo) in pagella[nome]:
                if(assPrimo>assenzeMax):
                    assenzeMax=assPrimo
                    materiaMax=materia
                if(assSecondo>assenzeMax):
                    assenzeMax=assSecondo
                    materiaMax=materia
                
            return assenzeMax,materiaMax
        
def votoMinimoMateria(pagella):
    minimoVoto=10
    materiaMinimo=""
    nome=input("Inserisci nome del studente : ")
    for keys in pagella.keys():
        if(nome==keys):
            for materia,(votoPrimo,assPrimo),(votoSecondo,assSecondo) in pagella[nome]:
                if(minimoVoto>votoSecondo):
                    minimoVoto=votoSecondo
                    materiaMinimo=materia
            return minimoVoto,materiaMinimo
        
def stampaVotoMaximo(pagella):
    materiaMax=" "
    votoMax=0

    nome=input("Inserisci nome del studente : ")
    for keys in pagella.keys():
        if(nome==keys):
            for materia,(votoPrimo,assPrimo),(votoSecondo,assSecondo) in pagella[nome]:
                if(votoPrimo>votoMax):
                    votoMax=votoPrimo
                    materiaMax=materia
                if(votoSecondo>votoMax):
                    votoMax=votoSecondo
                    materiaMax=materia
                
            return votoMax,materiaMax


                    


voti=pagella["studente1"]
voti.append(("Fisica",(10,0),(10,0)))



pagella["Albert Einstein"]=[("Matematica",(10,0),(10,0)),
                            ("Italiano", (10, 0), (10, 0)),
                            ("Inglese", (10, 0), (10, 0)),]
voti=pagella["Albert Einstein"]
voti.append(("Fisica",(10,0),(10,0)))

print(pagella)

#print(stampaStudentePrimoQuad(pagella))

#print(stampaStudenteSecondoQuad(pagella))

#print(stampaMateriaAssenze(pagella))

#print(votoMinimoMateria(pagella))

print(stampaVotoMaximo(pagella))#зробити в еррей

    

