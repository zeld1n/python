def mediavoti(dizionario):
    media=0
    cont=0
    for value in dizionario:
        media+=dizionario[value]
        cont+=1
    return media/cont

dizionario={}

nome=input("Inserisci nome dello studente: ")
while nome=="":
    nome=input("Inserisci nome dello studente: ")

while True:
    materia=input("Inserisci il nome della materia (o 'fine' per terminare): ")
    while materia=="":
        materia=input("Inserisci il nome della materia (o 'fine' per terminare): ")
    if(materia=="fine"):
        break
    voto=int(input(f"Inserisci il voto di {materia}: "))
    dizionario[materia]=voto
    
print(f"Voti di {nome}: ")
for key,value in dizionario.items():
    print("-",key,value)
print(f"Media voti è {mediavoti(dizionario)}")

