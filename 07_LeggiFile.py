import matplotlib.pyplot as plt

ListX = []
ListY = []
#Creo due liste globali

def Coord(line):
    valori = line.strip("\n").split(",")
    #Scompongo la linea in 2
    ListX.append(int(valori[0]))
    ListY.append(int(valori[1]))
    #Aggiungo le coordinate X e Y alle liste
    return line.strip("\n")
    #Restituisce le coordinate del punto
    
    
if __name__ == "__main__":
    with open("desktop/dati.txt", 'r') as f:
    #Apro il file in lettura
        for line in f:
        #Creo un ciclo che controlla tutte le righe del file
            print(Coord(line))

    plt.scatter(ListX,ListY)
    #Creo il grafico a dispersione
    plt.show()