tupla=(

    ("repartoA",[("Gennaio",1000),("Febbraio" ,10000),("Marzo",2000),("Aprile",4000),("Maggio","N/D"),("Giugno",0)]),
    ("repartoB",[("Gennaio",4000),("Febbraio" ,16000),("Marzo",1700),("Aprile",3000),("Maggio",4000),("Giugno",500)]),
    ("repartoC",[("Gennaio",3000),("Febbraio" ,12000),("Marzo",2500),("Aprile",2323),("Maggio",1000),("Giugno",900)])
)


def medioVen(tupla):
    if(tupla==""):
        return ("Tupla vuota ")
    cont=0
    valMin=tupla[1][1][1][1]
    valMax=0
    meseMin=""
    meseMax=""
    impMedio=0
    insReparto=input("Inserisci reparto : ")

    for reparto,altro in tupla:
        if(insReparto==reparto):
            for mese,valore in altro:
                if(valore=="N/D"):
                    cont=cont
                else:
                    cont+=1
                    impMedio+=valore
    
                    if(valMax<valore):
                        valMax=valore
                        meseMax=mese
                    if(valMin>valore):
                        valMin=valore
                        meseMin=mese
        
            return (impMedio/cont,(valMax,meseMax),(valMin,meseMin))
    return ("Tupla non è stata trovata")

              

        
medio,(valmax,mesemax),(valmin,mesemin)=medioVen(tupla)  

print("Valore medio : ",medio)
print("Valore min: ",valmin, " Mese: ",mesemin)
print("Valore max: ",valmax, " Mese: ",mesemax)