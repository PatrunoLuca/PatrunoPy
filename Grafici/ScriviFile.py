from random import randint
#Importo la libreria
def randCoord(start,stop,vartype=None):
    #Start ---- Valore di inizio
    #Stop ----- Valore di fine
    #VarType -- Tipo di dato da dare in output, se none ritorna una stringa
    X = str(randint(start, stop))
    Y = str(randint(start, stop))
    #Do come valora un numero casuale da 1 a 100
    if vartype == 'tupla':
        return (X,Y)
    elif vartype == 'dizionario':
        return {X:Y}
    elif vartype == 'lista':
        return [X,Y]
    elif vartype == 'stringa':
        return f"{X},{Y}"
    else:
        return f"{X},{Y}"
    #Restituisco i valori in base al tipo richiesto

if __name__ == "__main__":
    #Apro il file in modalità w
    #Se esiste lo cancello e lo ricreo, se non esiste lo apro
    with open("desktop/dati.txt", 'w') as f:
        #Ripeto 100 volte 
        for i in range(1,101): 
            coord = randCoord(1,101)
            #Aggiungo X e Y al file e li scrivo
            f.write(randCoord(1,101) + "\n")
            print(f"La coppia numero {i} è {coord}")