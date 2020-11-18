def _Conta(stringa):
    Dict_Letters = {}
    for i in stringa:
        if i not in Dict_Letters:
            Dict_Letters[i] = 1
        else:
            Dict_Letters[i] += 1
    return Dict_Letters

def Cerca_Massimo(Dict_Letters,Massimo):
    Maggiori = []
    for Key in Dict_Letters:
        if Dict_Letters[Key] == Massimo:
            Maggiori.append(Key)
    return Maggiori
                
                
if __name__ == "__main__":
    while True:
        print('''Benvenuto! 
Se mi scrivi una parola ti dirò la lettera con il maggior numero di occorrenze in una lista''')
        Stringa = sorted((input("Scrivi una parola --> ")).upper())
        Dict_Letters = _Conta(Stringa)
        Massimo = max(Dict_Letters.values())

        Maggiori = Cerca_Massimo(Dict_Letters,Massimo)
        Intermedio = " "
        if Massimo == 1:
            Finale = "a"
        else:
            Finale = "e"
        if len(Maggiori) > 1:
            print(f"Le lettere che compaiono più volte sono {Intermedio.join(Maggiori)}, e compaiono {Massimo} volt{Finale}.")
        else: 
            print(f"La lettera che compare più volte è la  {Maggiori[0]}, e compare {Massimo} volt{Finale}.")
        
        input("\n-Premi invio per riutilizzare il programma o premi ctrl + c per terminarne l'esecuzione  ")
