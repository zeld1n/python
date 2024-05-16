class RefertoMedico:
    #1,2 09:20

    def __init__(self,nome):
        self.nome=nome
        self.arraydiagnosi=[]
    
    def popola(self):
        self.arraydiagnosi.append(("01/03/2022",323,350,"parametro1"))
        self.arraydiagnosi.append(("04/01/2022",200,240,"parametro2"))
        self.arraydiagnosi.append(("11/08/2023",124,260,"parametro2"))
        self.arraydiagnosi.append(("15/01/2024",100,300,"parametro4"))
        self.arraydiagnosi.append(("10/02/2020",50,200,"parametro5"))
    
    def visualizzaReferto(self):
        for data,rilevato,riferimento,parametro in self.arraydiagnosi:
            print("Data: ",data,"\nParametro: ",parametro,"\nValore rilevato: ",rilevato,"\nValore di riferimento: ",riferimento,"\nScostamento: ",abs(riferimento-rilevato))

    def contaDiagnosi(self):
        print("Diagnosi presenti sono: ",len(self.arraydiagnosi))
        self.visualizzaReferto()

    def mediaRelivazioni(self,parametroInserito):
        cont=0
        somma=0
        for _,rilevato,_,parametro in self.arraydiagnosi:
            print(parametro)
            if(parametro==parametroInserito):
                cont+=1
                somma+=rilevato
        return somma/cont
    
    def rilevazioniMigliore(self,parametroInserito):
        differenza=0
        differenzaMin=self.arraydiagnosi[0][1]
        riferimentoValore=[]
        dataarray=[]
        cont=0
        
        for data,rilevato,riferimento,parametro in self.arraydiagnosi:
            if(parametro==parametroInserito):
                cont+=1
                dataarray.append(data)
                riferimentoValore.append(riferimento)
                differenza=abs(riferimento-rilevato)
                if(differenzaMin>differenza):
                    differenzaMin=differenza
        if(cont>0):
            dizionario={parametroInserito:(min(riferimentoValore),differenzaMin,dataarray)}
            return dizionario
        else:
            print("Parametro inserito non esiste ")
            return 0
        
    def visRilevazioneMigliore(self,parametroIns):
        dizionario=self.rilevazioniMigliore(parametroIns)
        if(dizionario!=0):
            for riferimento,difMin,array in dizionario.values():
                print("Migliori rilevazioni di: ",parametroIns,"\nValore di riferimento: ",riferimento,"\nScostamento minimo registrato: ",difMin,"\nNelle rilevazioni del : ",array) 
    





class ReportReferti:
    def __init__(self):
        self.refertiLista=[]

    def aggiungiReferto(self,referto):
        self.refertiLista.append(referto)

    def rimuoviReferto(self,paziente):
        cont=0
        for arrayDiagnosi in self.refertiLista:
            if(arrayDiagnosi.nome==paziente):
                self.refertiLista.pop(cont)
        cont+=1

    def cercaReferto(self,paziente):
        for i in self.refertiLista:
            if(i.nome==paziente):
                return i
        return -1
        

    def visualizzaReferto(self,paziente):
    
        for i in self.refertiLista:
            if(i.nome==paziente):
                for cont in range(len(i.arraydiagnosi)):
                    vis="Parametro: "+str(i.arraydiagnosi[cont][3])+"\nData: "+str(i.arraydiagnosi[cont][0])+"\nValore rilevato: "+str(i.arraydiagnosi[cont][1])+"\nValore di riferimento: "+str(i.arraydiagnosi[cont][2])+"\n"
                    print(vis)
            return
        print("Non esiste ")
    def __str__(self):
        vis=""
        for i in self.refertiLista:
            vis+="Nome: "+i.nome
            for cont in range(len(i.arraydiagnosi)):
                vis+="\nParametro: "+str(i.arraydiagnosi[cont][3])+"\nData: "+str(i.arraydiagnosi[cont][0])+"\nValore rilevato: "+str(i.arraydiagnosi[cont][1])+"\nValore di riferimento: "+str(i.arraydiagnosi[cont][2])+"\n"
        return vis




if __name__=='__main__':

    referiti=ReportReferti()
    nome=input("Inserisci nome di paziente: ")
    paziente = RefertoMedico(nome)
    paziente.popola()
    referiti.aggiungiReferto(paziente)
while True:
  scelta=int(input("""   
1.Visualizza
2.Contaggio diagnosi
3.Media rilevazioni
4.Rilevazione Miglore
5.Rimuove il referto
6.Cerca il Referto
7.Visualizza il referto
8.Visualizza
0.USCIRE
"""))
  if(scelta==1):
        paziente.visualizzaReferto()
  if(scelta==2):
        paziente.contaDiagnosi()
  if(scelta==3):
       parametro=input("Inserisci parametro: ")
       print(paziente.mediaRelivazioni(parametro))
  if(scelta==4):
       parametro=input("Inserisci parametro: ")
       paziente.visRilevazioneMigliore(parametro)
  if(scelta==5):
      nomePaziente=input("Inserisci nome: ")
      referiti.rimuoviReferto(nomePaziente)    
  if(scelta==6):
      nomePaziente=input("Inserisci nome: ")
      if(referiti.cercaReferto(nomePaziente)!=-1):
          print("Trovato")    
      else:
          print("Non esiste")
  if(scelta==7):
      nomePaziente=input("Inserisci nome: ")
      referiti.visualizzaReferto(nomePaziente)
  if(scelta==8):
      print(referiti)    
  if(scelta==0):
      break
      

  

