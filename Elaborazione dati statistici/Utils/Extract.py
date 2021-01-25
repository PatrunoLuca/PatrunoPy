from csv import reader as csv_reader

def Extract(filename):
    #Creo un dizionario
    dizionario = {}

    #Apro il file passato come parametro
    with open(filename, "r") as csv_file:
        #Per ogni linea nel file
        for line in csv_reader(csv_file):
            #Se la linea ha la lunghezza giusta
            if len(line) == 7:
                #Aggiungo al dizionario l'età come indice e i 3 dati che mi servono come chiavi 
                dizionario[line[0]] = [float(line[1]), float(line[-1]), round(100 - (float(line[1])+ float(line[-1])), 2)]
                #I 3 dati che prendo sono: quelli che usano il pc, quelli che non lo usano e quelli che si sono astenuti
    #Restituisco la lista dei dati
    return dizionario

#Creo 2 funzioni, ognuna passa al metodo Extract un file e poi restituisce un dizionario in output
def Extract_2018():
    return Extract("Utils/2018.csv")
    
def Extract_2019():
    return Extract("Utils/2019.csv")
