Lista_Prezzi = {1: 45, 2: 80, 3: 120, 4: 160}
while True:
    try:
        N_Giorni = int(input("Per quanti giorni vuoi noleggiare lo scooter? "))
        break
    except Exception:
        print("Valore non valido!")
        print("È possibile inserire solo numeri interi")
try:
    Prezzo = str(Lista_Prezzi[N_Giorni])
except IndexError or KeyError:
    Prezzo = str(160 + ((N_Giorni - 4) * 40))
except Exception as Errore:
    print("C'è stato un errore")
    raise Exception(f"Errore {Errore}")
print(f"Il prezzo per noleggiare lo scooter per {N_Giorni}gg è {Prezzo},00")
