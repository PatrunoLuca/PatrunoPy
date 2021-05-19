from matplotlib import pyplot as plt
from pandas import DataFrame, read_csv
from rich.console import Console
from rich.table import Table
from pyfiglet import figlet_format

def media(lista=list):
    return sum(lista) / len(lista)

def get_data(csv_file=str):
    with open("0.csv", "r") as csvfile:
        df = read_csv(csvfile)
    return  {
        "Linear Acceleration x (m/s^2)" : df["Linear Acceleration x (m/s^2)"].tolist()[24:],
        "Linear Acceleration z (m/s^2)" : df["Linear Acceleration z (m/s^2)"].tolist()[24:],
        "Time (s)" : df["Time (s)"].tolist()[24:]
    }

def extract(dizionario=dict):
    asse_x = media(dizionario["Linear Acceleration x (m/s^2)"])
    asse_z = media(dizionario["Linear Acceleration z (m/s^2)"])
    tempo = (dizionario["Time (s)"][-1] - dizionario["Time (s)"][0])
    return {
        "X" : {
            "accelerazione_media": asse_x,
            "velocita_iniziale" : asse_x / tempo
            },
        "Z" : {
            "accelerazione_media": asse_z,
            "velocita_iniziale" : asse_z / tempo
            },
        "Absolute" : {
            "accelerazione_media": asse_x + asse_z,
            "velocita_iniziale" : (asse_x / tempo) + (asse_z / tempo)
            }
    }

def print_dict(dizionario=dict, angolo=str):
    table = Table()
    console.print(figlet_format(f"Angolo di {angolo}°"), style="purple" )
    table.add_column("Asse", justify="left", style="red", no_wrap=True)
    table.add_column("Acelerazione", justify="left", style="bold blue", no_wrap=True)
    table.add_column("Velocità", justify="left", style="bold green", no_wrap=True) 
    for i in dizionario:        
        lista = dizionario[i]
        table.add_row(i,str(lista["accelerazione_media"]),str(lista["velocita_iniziale"]))
    console.print(table)

if __name__ == '__main__':
    console = Console()
    Angle0 = get_data("0.csv")
    Angle32 = get_data("32.csv")
    print_dict(extract(Angle0), '0')
    print_dict(extract(Angle32), '32')