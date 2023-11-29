tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Novara", [
        ("febrraio", ("elettrico", 320)),
        ("febrraio", ("gas", 170)),
        ("febbraio", ("elettrico", 270)),
        ("febbraio", ("gas", 110)),
        # Aggiungi altri mesi e consumi
    ]) 
)
def analizza_consumi_energetici(tupla):
    medio=0
    cont=0
    meseMax=""
    valoreMax=0
    cittaIns=(input("Inserisci città: "))
    risorsaIns=(input("Inserisci risorsa: "))
    
    for citta,altro in tupla:
        if(citta == cittaIns):
            for mese, (risorsa, valore) in altro:
                if risorsa == risorsaIns: 
                    medio+=valore
                    cont+=1
                    if(valoreMax<valore):
                        valoreMax=valore
                        meseMax=mese
       
            return (medio/cont,(valoreMax,meseMax))  
   
        
       
       
                
            





medio,(risorsaMax,meseMax)=analizza_consumi_energetici(tupla_consumi_energetici)
print("Medio valore é: ",medio," Max risorsa: ",risorsaMax," Max mese",meseMax)

