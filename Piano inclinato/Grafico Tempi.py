from math import radians, sin, sqrt

import matplotlib.pyplot as plt
from pandas import DataFrame
from pandas import read_csv as csv
from rich.console import Console
from rich.table import Table
from pyfiglet import figlet_format as pyfiglet

def average(lista=list):
    #ritorna la media di una lista approssimato a 3 cifre decimali
    return round(sum(lista) / len(lista), 3)


def extract(space=float, nomefile=str):
    with open(nomefile, "r") as outfile:
        #estrae i dati e li trasforma in un DataFrame
        df = csv(outfile)

    return DataFrame(
        #crea un DataFrame calcolando i dati dal DataFrame del csv
        [
            {
                "angle": row[0],
                "acceleration": average(
                    [(space / time) / time for time in row[1:]]),
                "time": average(row[1:]),
                "velocity": average([space / time for time in row[1:]])
                } for index, row in df.iterrows()#iterazion per ogni elemento nel DataFrame
            ]
        ) #ritorna il DataFrame


def calculate_data(space=float):
    dict_list = []
    for angle in [30, 45, 60]: #per ogni angolo calcola i dati
        acceleration = 9.81 * round(sin(radians(angle)), 1)
        time = sqrt( space / acceleration)
        velocity = space / time
        dict_list.append(
            # aggiunge i dati come dizionario alla lista
            dict(
                zip(#comprime 2 liste in un dizionario
                    ["angle", "acceleration", "time", "velocity"],
                    [round(i, 3) for i in [
                        angle, acceleration, time, velocity]]
                    )
                )
            )
    return DataFrame(dict_list) # ritorna la lista come DataFrame


def panda_to_table(df=DataFrame, color=0):
    table = Table()
    for title, data in df.items():
        #per ogni titolo in DataFrame lo aggiunge come colonna  della tabella
        table.add_column(title, justify="left", style=f"color({color})")
        color += 1 #aumenta la variabile colore di 1 per variare il colore
    for index, rows in df.iterrows():
        #aggiunge la riga del DataFrame come riga della tabella
        table.add_row(*tuple([str(i) for i in rows]))
    return table #Ritorna la tabella


if __name__ == "__main__":
    console = Console()
    data = extract(0.5, "misure.csv")
    true_data = calculate_data(0.5)
    #estrae i dati in due variabile
    console.print(pyfiglet("Esperimento"), style="green")
    console.print(panda_to_table(data, color=1))
    console.print(pyfiglet("Formule"), style="red")
    console.print(panda_to_table(true_data, color=1))
    #stampa a schermo prima un testo in ascii art che identifica la tabella
    # e la tabella stessa dai DataFrame delle due variabili
    plt.plot(data["angle"], data["time"], label='Esperimento')
    plt.plot(true_data["angle"], true_data["time"], label='Formule')
    #Crea un grafico con 2 linee che hanno come asse y gli angoli e come asse x
    # il tempo impiegato per percorrere un piano inclinato di 50 cm con
    #quell'inclinazione specifica
    plt.xlabel("angolo")
    plt.ylabel("tempo")
    plt.title("Grafico tempi")
    plt.legend()
    plt.show()
