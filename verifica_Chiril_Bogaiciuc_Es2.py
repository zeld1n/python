tupla_pluviometrica = (
                      (("Vittuone","Milano"),(2022, ("gennaio",20))),
                      (("Vittuone","Milano"),(2023, ("marzo",80))),
                      (("Vittuone","Milano"),(2023, ("aprile",60))),
                      (("Vittuone","Milano"),(2023, ("maggio",80))),
                      (("Vittuone","Milano"),(2023, ("luglio",30))),
                      (("Arluno","Milano"),(2023, ("luglio",60))),
                      (("Vittuone","Milano"),(2023, ("agosto","N/D"))),
                      (("Varenna","Lecco"),(2023, ("luglio",150))),
                      (("Morbegno","Sondrio"),(2023, ("luglio",165)))
                      )#645


def media_globale(tupla):
    cont=0
    media=0
    for provincia,(anno,(mese,gradi)) in tupla:
        if(gradi=="N/D"):
            cont=cont
        else:
            media+=gradi
            cont+=1
    return media/cont


def media(tupla):
    media=0
    cont=0
    prov=input("Inserisci provincia: ")
    meseRif=input("Inserisci mese: ")
    for (citta,provincia),(anno,(mese,gradi)) in tupla:
        if(prov==provincia and mese==meseRif):
            media+=gradi
            cont+=1
    return media/cont,prov,meseRif

def pioggiaMax(tupla):
    maxGradi=0
    maxCitta=""
    maxmese=""
    for (citta,provincia),(anno,(mese,gradi)) in tupla:
        if(gradi=="N/D"):
            maxGradi=maxGradi
        else:
            if(gradi>maxGradi):
                maxGradi=gradi
                maxCitta=citta
                maxmese=mese
    return maxGradi,maxCitta,maxmese   

def pioggiaMin(tupla):
    minGradi=tupla[1][1][1][1]
    minCitta=""
    minmese=""
    for (citta,provincia),(anno,(mese,gradi)) in tupla:
        if(gradi=="N/D"):
            minGradi=minGradi
        else:
            if(provincia=="Milano"):
                if(minGradi>gradi):
                    minGradi=gradi
                    minCitta=citta
                    minmese=mese

    return minGradi,minCitta,minmese   


def provinciaPer(tupla):
    provPer=0
    percentuale=0
    tot=0
    provinciaIns=(input("Inserisci provincia :"))
    for (citta,provincia),(anno,(mese,gradi)) in tupla:
        if(gradi=="N/D"):
           tot=tot
        else:
            tot+=gradi
    if(provinciaIns==provincia):
        if(gradi=="N/D"):
            gradi=gradi
        else:
            provPer+=gradi
        
    percentuale=(provPer/tot)*100
    return percentuale
         
            


        





scelta=0

while(True):
    print("1) Media Globale")
    print("2) Media")
    print("3) Pioggia max")
    print("4) Pioggia min")
    print("5) Provincia Per")
    print("0) Esce")
    scelta=int(input(""))
    if(scelta==1):
        print("Medio di pioggia nell'anno : ",media_globale(tupla_pluviometrica))
    elif(scelta==2):
        mediaPio,prov,meseRif=media(tupla_pluviometrica)
        print("Media pluviometricha di provincia : ",prov,": ",mediaPio," Mese: ",meseRif)
    elif(scelta==3):
        maxGradi,maxcitta,maxmese=pioggiaMax(tupla_pluviometrica)
        print("Citta: ",maxcitta," Max gradi: ",maxGradi," Mese: ",maxmese)
    elif(scelta==4):  
        minGradi,mincitta,minmese=pioggiaMin(tupla_pluviometrica)
        print("Citta: ",mincitta," Min gradi: ",minGradi," Mese: ",minmese)
    elif(scelta==5):
       print( "Percentuale: ",provinciaPer(tupla_pluviometrica))
    elif(scelta==0):
        break

