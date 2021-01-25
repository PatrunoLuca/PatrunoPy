import numpy as np
import matplotlib.pyplot as plt
from Utils import Extract_2018, Extract_2019, Merge_Graph
#Importo le librerie necessarie
    
def Grafico(dizionario, anno):
    #Creo una lista per ogni dato che mi serve
    titles = [i for i in dizionario ]
    use = [dizionario[i][0] for i in dizionario ]
    dont_use = [dizionario[i][1] for i in dizionario ]
    error = [dizionario[i][-1] for i in dizionario ]

    w = 0.2

    bar1 = np.arange(len(titles))
    bar2 = [i+w for i in bar1]
    bar3 = [i+w for i in bar2]
    
    #Creo le tre barre 
    plt.bar(bar1, use, w, label="Usano il PC", color="green")
    plt.bar(bar2, dont_use, w, label="Non usano il PC", color="orange")
    plt.bar(bar3, error, w, label="Astenuti", color="red")
    #Imposto tutti i parametri del grafico
    plt.xlabel("Fascia d'età")
    plt.ylabel("Uso del PC")
    plt.title(f"Grafico {anno}")
    plt.xticks(bar1,titles)
    plt.legend(loc='upper center')
    #Imposto il grafico a schermo intero
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    #Salvo la foto
    plt.savefig(f"Utils/{anno}.png")
    #Mostro il grafico
    plt.show()


if __name__ == "__main__":
    #Definisco i due dizionario
    Dizionario_2018 = Extract_2018()
    Dizionario_2019 = Extract_2019()
    
    #Generò i due grafici
    Grafico(Dizionario_2018, "2018")
    Grafico(Dizionario_2019, "2019")
    #Fondo i due grafici in una sola immagine
    Merge_Graph("Utils/2018","Utils/2019","png")