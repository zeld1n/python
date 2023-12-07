

diz={"Giuseppe Gullo":[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
     "Antonio Barbera":[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
     "Nicola Spina":[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)],
     }

def materiMategiuseppe(diz):
    nome="Giuseppe Gullo"
    materia="Matematica"
    for keys in diz.keys():
        if(keys==nome):
            for vet in diz[keys]:
                if(vet[0]==materia):
                    return nome,vet[0],vet[1],vet[2]
                
def materiNicola(diz):
    nome="Nicola Spina"
    materia="Inglese"
    for keys in diz.keys():
        if(keys==nome):
            for vet in diz[keys]:
                if(vet[0]==materia):
                    return nome,vet[0],vet[1],vet[2]

def votoAntonio(diz):
    nome="Antonio Barbera"
    materia="Geografia"
    for keys in diz.keys():
        if(keys==nome):
            for vet in diz[keys]:
                if(vet[0]==materia):
                    return nome,vet[0],vet[1],vet[2]
 
def mediaNicola(diz):
    nome="Nicola Spina"
    media=0
    cont=0
    for keys in diz.keys():
        if(keys==nome):
            for vet in diz[keys]:
                media+=vet[1]
                cont+=1    
            return nome,(media/cont)
    
def mediaTutti(diz):
    media=0
    cont=0
    for keys in diz.keys():
        for vet in diz[keys]:
            media+=vet[1]
            cont+=1    
    return (media/cont)
    
def assenzeNicola(diz):
    nome="Nicola Spina"
    maxAss=0
    maxMat=""
    for keys in diz.keys():
        if(keys==nome):
            for vet in diz[keys]:
                if(maxAss<vet[2]):
                    maxAss=vet[2]
                    maxMat=vet[0]
            return nome,maxAss,maxMat

                    

diz["Albert Einstein"]=[("Matematica",10,0),("Italiano",10,0),("Inglese",10,0),("Storia",10,0),("Geografia",10,0),("Fisica",10,0)]
voti=diz["Giuseppe Gullo"] 
voti.append((("Fisica",9.5,0)))
voti=diz["Antonio Barbera"] 
voti.append((("Fisica",8,1)))
voti=diz["Nicola Spina"] 
voti.append((("Fisica",8,3)))

nome,materia,voto,assenze=materiMategiuseppe(diz)
print("Nome: ",nome,"Materia: ",materia," Voto: ",voto," Assenze: ",assenze)
nomeN,materiaN,votoN,assenzeN=materiNicola(diz)
print("Nome: ",nomeN,"Materia: ",materiaN," Voto: ",votoN," Assenze: ",assenzeN)

nomeA,materiaA,votoA,assenzeA=votoAntonio(diz)
print("Nome: ",nomeA,"Materia: ",materiaA," Voto: ",votoA)

nomeMedia,media=mediaNicola(diz)
print("Media di ",nome,": ",media)

print("Media tutti: ",mediaTutti(diz))

nomeAssenze,ass,mat=assenzeNicola(diz)
print("Nome: ",nomeAssenze," Assenze: ",ass," Materia: ",mat)


