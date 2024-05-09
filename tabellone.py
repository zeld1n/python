class Pagella:
    def __init__(self, nome_studente):
        self.nome_studente = nome_studente
        self.pagella = []
    def popola_pagella(self):
        self.pagella.append(("ITALIANO",8,5))
        self.pagella.append(("STORIA",8,4))
        self.pagella.append(("MATEMATICA",10,3))
        self.pagella.append(("LINGUA INGLESE",9,0))
        self.pagella.append(("TELECOMUNICAZIONI",10,7))
        self.pagella.append(("INFORMATICA",5,0))
        self.pagella.append(("SISTEMI E RETI",5,0))
        self.pagella.append(("TECN. PROG. SIST. I.",4,0))
        self.pagella.append(("SCIENZE MOTORIE E SP",6,0))

class Tabellone:
  def __init__(self):
    self.tabella=[]
  def push(self,pagella):
    self.tabella.append(pagella)
  def pop(self,studente):
    self.tabella.pop(studente)
  def cercaPagella(self,studente):
    for i in self.tabella:
        if(i.nome_studente==studente):
           return i
    return -1
    
  def __repr__(self):
    vis=""
    for i in self.tabella:
        for cont in range(len(i.pagella)):
            vis+="Pagella di "+str(i.nome_studente)+": "+"Materia: "+str(i.pagella[cont][0])+"="+str(i.pagella[cont][1])+" Ore di assenza: "+str(i.pagella[cont][2])+"\n\n"
    return vis

scelta=0
tabellone=Tabellone()
while True:
  scelta=int(input("""
1.Inserisci una pagella di uno studente     
2.Estrae la pagella di uno studente
3.Verifica se la pagella di uno studente è presente
4.Visualizza
0.USCIRE
                    """))
  if(scelta==1):
    nome=input("Inserisci nome: ")
    pagella1=Pagella(nome)
    pagella1.popola_pagella()
    tabellone.push(pagella1)
  if(scelta==2):
    nome=input("Inserisci nome: ")
    tabellone.pop(nome)
  if(scelta==3):
    nome=input("Inserisci nome: ")
    if(tabellone.cercaPagella(nome)!=-1):
       print("Trovato")
    else:
       print("Non è trovato")
  if(scelta==4):
    print(tabellone)
  if(scelta==0):
     break
    





