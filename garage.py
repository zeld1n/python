class Garage:
    def __init__(self):
        self.macchine = []

    def push(self, macchina):
        self.macchine.append(macchina)

    def pop(self):
        if self.macchine:
            return self.macchine.pop()
        else:
            print("Il garage è vuoto.")
            return None

    def remove(self, targa):
        for macchina in self.macchine:
            if macchina["targa"] == targa:
                self.macchine.remove(macchina)
                print("Macchina con targa", targa, "rimossa.")
                return
        print("Macchina con targa", targa, "non trovata.")

    def cercaMacchina(self, targa):
        for macchina in self.macchine:
            if macchina["targa"] == targa:
                print("Macchina con targa", targa, "trovata.")
                return
        print("Macchina con targa", targa, "non trovata.")

    def __str__(self):
        result = "Contenuto del garage:\n"
        if self.macchine:
            for index, macchina in enumerate(self.macchine, start=1):
                result += f"{index}. Marca: {macchina['marca']}, Modello: {macchina['modello']}, Targa: {macchina['targa']}\n"
        else:
            result += "Il garage è vuoto."
        return result


# Test della classe Garage
garage = Garage()

# Inserimento di macchine nel garage
garage.push({"marca": "Fiat", "modello": "500", "targa": "AB123CD"})
garage.push({"marca": "Ford", "modello": "Focus", "targa": "EF456GH"})

# Test delle funzioni
print(garage)  # Stampa il contenuto del garage
garage.remove("AB123CD")  # Rimuove una macchina
print(garage)  # Stampa di nuovo il contenuto del garage
garage.cercaMacchina("EF456GH")  # Cerca una macchina
macchina_estratta = garage.pop()  # Estrae una macchina
print("Macchina estratta:", macchina_estratta)