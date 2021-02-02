#Per aggiungere altri veicoli basta metterli nei 2 dizionari qui sotto
#Il numero di giorni per cui il veicolo ha un prezzo già stabilito puo anche essere diverso da 0
Veicoli_Prezzati = {"Scooter 50cc": {1: 45, 2: 80, 3: 120, 4: 160}}
Prezzo_Giornaliero_Veicoli = {"Scooter 50cc": 40}


Veicoli = list(Veicoli_Prezzati.keys())
print('''Benvenuto in Noleggia Veicoli!
Di seguito la lista dei veicoli disponibili:\n''')
for oggetto in Veicoli:
    print(f"--{oggetto}")  

while True:
    Veicolo = str(input("\nChe veicolo scegli? "))
    if Veicolo in Veicoli:
        break
    else:
        print('''Mi dispiace, il veicolo scelto non fa parte dei veicoli attualmente disponibili
Di seguito la lista dei veicoli disponibili:\n''')
        for oggetto in Veicoli:
            print(f"--{oggetto}")

while True:
    try:
        N_Giorni = int(input(f"\nPer quanti giorni vuoi noleggiare veicolo? ({Veicolo})  "))
        break
    except Exception:
        print("Valore non valido!")
        print("È possibile inserire solo numeri interi\n")
try:
    Prezzo = (Veicoli_Prezzati[Veicolo])[N_Giorni]
except KeyError or IndexError:
    Prezzo_Ultimo_Giorno = (Veicoli_Prezzati[Veicolo])[len(Veicoli_Prezzati[Veicolo])]
    Max_Giorni = (N_Giorni - len(Veicoli_Prezzati[Veicolo]))
    Prezzo_Giornaliero_Veicolo = (Prezzo_Giornaliero_Veicoli)[Veicolo]
    Prezzo = Prezzo_Ultimo_Giorno + (Max_Giorni * Prezzo_Giornaliero_Veicolo)
except Exception as Errore:
    print("C'è stato un errore")
    raise Exception(f"Errore {Errore}")
print(f"\nIl prezzo per noleggiare il veicolo {Veicolo} per {N_Giorni} giorni è {Prezzo},00 ")
