# Dizionario che rappresenta la scacchiera con 9 posizioni, inizialmente libere
# mentre la partita si svolge il valore associato sarà o X oppure O 
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
  cont=0
  for values in board.values():
    print('|'+values+'|',end="")
    cont+=1
    if(cont==3):
      print()
      print("---------") 
      cont=0
    
def controllaPosizione(board,posizione):
  if(posizione in board.keys()):
    if(board[posizione]==' '):
      return True
    else:
      print("Posizione è occupata ")
  else:
    print("Posizione non esiste ")


def controllaVittoria(board):
  if(board['top-L']==board['top-M']==board['top-R'] and board['top-L']!=' '):
    return True
  if(board['top-L']==board['mid-M']==board['low-R'] and board['top-L']!=' '):
    return True
  if(board['top-L']==board['mid-L']==board['low-L'] and board['top-L']!=' '):
    return True
  if(board['top-M']==board['mid-M']==board['low-M'] and board['top-M']!=' '):
    return True
  if(board['top-R']==board['mid-R']==board['low-R'] and board['top-R']!=' '):
    return True
  if(board['top-R']==board['mid-M']==board['low-L'] and board['top-R']!=' '):
    return True
  if(board['low-L']==board['low-M']==board['low-R'] and board['low-L']!=' '):
    return True
  if(board['mid-L']==board['mid-M']==board['mid-R'] and board['mid-L']!=' '):
    return True
  

  
def boardInizio():
  print("Scelta disponibili:\ntop-L|top-M|top-R\n-+-+-\nmid-L|mid-M|mid-R\n-+-+-\nlow-L|low-M|low-R\n-----------------")
#stabilisce il turno iniziale 
turn = 'X'
boardInizio()


#ciclo per gestire le 9 mosse
for i in range(9):
    print("Turno: ",turn)
    printBoard(theBoard)
    posizione=input("Inserisci posizione: ")
    while not controllaPosizione(theBoard,posizione):
      posizione=input("Inserisci posizione: ")
    theBoard[posizione]=turn
    if(controllaVittoria(theBoard)):
        print("Vinto: ",turn)
        printBoard(theBoard)
        exit()
    if(i%2):
      turn='X'
    else:
      turn='O'
    
print("PAREGGIO")
      
    
    