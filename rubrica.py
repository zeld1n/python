import pprint
pp=pprint.PrettyPrinter(indent=4)

contacts={'b'+' '+'a':['3290057330','Bareggio','marcoespinoza@gmail.com']}
                                                    

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
      print(dict[cognome+' '+nome]) ## Починити вивод !
      break
        
    
        


def mostra_tutti(dict):
  pp.pprint(dict)

def modifica(dict):          
    nome=input("Nome: ")
    cognome=input("Cognome: ")
    for i in dict.keys():
      if(i==cognome+' '+nome):
          print("Dati del contatto :",cognome,nome)
          print(dict[cognome+' '+nome])
          print("Aggiorna i dati (lascia in bianco i campi che non vuoi modificare): ")
          telefono=input("Telefono (9 cifre): ")
    while len(telefono)!=9  or not telefono.isnumeric():
        if(telefono==""):
          telefono=dict[cognome+' '+nome][0]
          break
        else: 
          telefono=input("Telefono (9 cifre): ")
    indirizzo=input("Inserisci indirizzo: ")
    mail = input("Email (@ richiesta): ")
    while "@" not in mail or not '':
       if(mail==""):
          mail=dict[cognome+' '+nome][2]
          break
       else: 
          mail = input("Email (@ richiesta): ")
    dict[cognome+' '+nome]=[telefono,indirizzo,mail]

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