import pprint
pp=pprint.PrettyPrinter(indent=4)

contacts={'Espinoza'+' '+'Marco':['3290057330','Bareggio','marcoespinoza@gmail.com']}

def leggiDati():
  nome=input("Inserisci il nome =")
  while len(nome)==0:
    nome=input("Inserisci il nome =")
  cognome=input("Inserisci il cognome =")
  while len(nome)==0:
    cognome=input("Inserisci il cognome =")
  
  


  
  return [nome,cognome,telefono,indirizzo,email]
                                                    
def leggiChiave(): # зрозуміти навіщо ці 2 функциї |
  #...da completare
  #...
  return [nome,cognome]



def aggiungi(dict):
  print('Codice della funzione aggiungi')
  quantita=int(input("Quanti contatti vuoi inserire ?"))
  for i in range (quantita):
    print(f"Inserimento {i+1} contatto ")
    nome=input("Nome: ")
    cognome=input("Cognome: ")
    telefono=input("Telefono (9 cifre): ")
    while len(telefono)!=9  or not telefono.isnumeric():
        telefono=input("Telefono (9 cifre): ")
    indirizzo=input("Inserisci indirizzo: ")
    mail = input("Email (@ richiesta): ")
    while "@" not in mail:
      mail = input("Email (@ richiesta): ")
    dict[cognome+' '+nome]=[telefono,indirizzo,mail]
      

def elimina(dict):
    print("Cancellazione di un contatto")
    nome=input("Nome: ")
    cognome=input("Cognome: ")
    tut=cognome+' '+nome
    for i in dict:
        print(i)
        if(tut == i):
           del dict[tut]
           print("Eliminato")
           break
           

def cerca(dict):
   print("Mostra dati di un contatto:")
   nome=input("Nome: ")
   cognome=input("Cognome: ")
   for i in dict.keys():
    if(i==cognome+' '+nome):
      print(dict[cognome+' '+nome].values()) ## Починити вивод !
      break
        
    
        


def mostra_tutti(dict):
  print(dict)

def modifica(dict):             # Провірити функцию
    nome=input("Nome: ")
    cognome=input("Cognome: ")
    if(dict.keys()==cognome+nome):
        print("Dati del contatto :",cognome,nome)
        print(dict[cognome,nome].values())
        print("Aggiorna i dati (lascia in bianco i campi che non vuoi modificare): ")
        telefono=int(input("Telefono (9 cifre): "))
    while telefono!=9 or not telefono.isnumeric() :
      telefono=int(input("Telefono (9 cifre): "))
    indirizzo=input("Inserisci indirizzo: ")
    mail = input("Email (@ richiesta): ")
    while "@" not in mail:
      mail = input("Email (@ richiesta): ")
      dict[cognome,nome]=[telefono,indirizzo,mail]


while True:
  print('0) Esci')
  print('1) Aggiungi')
  print('2) Elimina')
  print('3) Cerca')
  print('4) Mostra tutti')
  print('5) Modifica')
  scelta=int(input('Scegli :'))
  if scelta==0:
    break
  elif scelta==1:
    aggiungi(contacts)
    
  elif scelta==2:
    elimina(contacts)
  elif scelta==3:
    cerca(contacts)
  elif scelta==4:
    mostra_tutti(contacts)
  elif scelta==5:
    modifica(contacts)