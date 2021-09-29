def Cerca_Massimo(stringa, Lista_Lettere):
    Maggiori = []
    for Lettera in Lista_Lettere:
        if stringa.count(Lettera) > 0:
            Maggiori.append(stringa.count(Lettera))
    return max(Maggiori)


def Più_Ricorrenti(stringa, Lista_Lettere, Massimo):
    Maggiori = []
    for Lettera in Lista_Lettere:
        if stringa.count(Lettera) == Massimo:
            Maggiori.append(Lettera)
    return Maggiori


def Crea_Lista_Lettere(Stringa):
    Lista_Lettere = []
    for Lettera in Stringa:
        if Lettera not in Lista_Lettere:
            Lista_Lettere.append(Lettera)
    return(Lista_Lettere)
  
  
if __name__ == "__main__":
    while True:
        print('''Benvenuto! 
Se mi scrivi una parola ti dirò la lettera con il maggior numero di occorrenze in una lista''')
        Stringa = input("Scrivi una parola --> ")
        Stringa = list(Stringa.upper())
        Stringa.sort()
        Lista_Lettere = Crea_Lista_Lettere(Stringa)
        Massimo = Cerca_Massimo(Stringa, Lista_Lettere)
        Maggiori = Più_Ricorrenti(Stringa, Lista_Lettere, Massimo)
        if Massimo == 1:
            finale = "a"
        else:
            finale = "e"
        if len(Maggiori) > 1:
            Intermedio = " "
            print(f"Le lettere che compaiono più volte sono {Intermedio.join(Maggiori)}, e compaiono {Massimo} volt{finale}.")
        else: 
            print(f"La lettera che compare più volte è la  {Maggiori[0]}, e compare {Massimo} volt{finale}.")
        input("\n-Premi invio per riutilizzare il programma o premi ctrl + c per terminarne l'esecuzione  ")