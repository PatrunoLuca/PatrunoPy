from pandas import DataFrame, read_csv
from rich.console import Console
from rich.table import Table
from pyfiglet import figlet_format
from math import sin, radians

def media(lista=list):
    return sum(lista) / len(lista)

def get_data(degree=str):
    with open(f"{degree}.csv", "r") as csvfile:
        df = read_csv(csvfile)
    return  {
        "Linear Acceleration x (m/s^2)" : df["Linear Acceleration x (m/s^2)"].tolist(),
        "Linear Acceleration z (m/s^2)" : df["Linear Acceleration z (m/s^2)"].tolist(),
        "Time (s)" : df["Time (s)"].tolist()
    }

def extract(dizionario, intervallo1, intervallo2, spazio, angolo):
    asse_x = dizionario["Linear Acceleration x (m/s^2)"]
    asse_z = dizionario["Linear Acceleration z (m/s^2)"]
    tempo = dizionario["Time (s)"]
    return {
        "X" : {
            "accelerazione_media": media(asse_x[intervallo1:intervallo2+1]),
            "velocita_iniziale" :  (spazio/100) / tempo[intervallo1]
            },
        "Z" : {
            "accelerazione_media": media(asse_z[intervallo1:intervallo2+1]),
            "velocita_iniziale" : 0 if angolo == "0" else (spazio/100) * radians(sin(int(angolo)))
            },
        "Absolute" : {
            "accelerazione_media": media(asse_x[intervallo1:intervallo2+1]) + media(asse_z[intervallo1:intervallo2+1]),
            "velocita_iniziale" : ((spazio/100) / tempo[intervallo1]) if angolo == "0" else (spazio/100) / tempo[intervallo1] + ((spazio/100) * radians(sin(int(angolo))))
            }
    }

def print_dict(dizionario=dict, angolo=str):
    table = Table()
    console.print(figlet_format(f"Angolo di {angolo}°"), style="purple" )
    table.add_column("Asse", justify="left", style="red", no_wrap=True)
    table.add_column("Velocità iniziale (m/s)", justify="left", style="bold green", no_wrap=True)
    table.add_column("Acelerazione (m/s2)", justify="left", style="bold blue", no_wrap=True) 
    for i in dizionario:        
        lista = dizionario[i]
        table.add_row(i,str(lista["velocita_iniziale"]), str(lista["accelerazione_media"]))
    console.print(table)

if __name__ == '__main__':
    console = Console()
    Angle0 = get_data("0")
    Angle32 = get_data("32")
    print_dict(extract(Angle0, 24, 27, 30, "0"), "0")
    print_dict(extract(Angle32, 46, 50, 22, "32"), "32")