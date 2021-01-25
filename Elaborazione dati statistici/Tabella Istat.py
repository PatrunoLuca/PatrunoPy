from rich.console import Console
from rich.table import Table
from Utils import Extract_2018, Extract_2019 
from pyfiglet import figlet_format
#Importo le librerie necessarie

def Printer(table, dizionario, anno):
    #Stampo a schermo l'anno del grafico in questione
    console.print(figlet_format(anno), style="purple" )
    #Aggiungo le 4 colonne della tabella
    table.add_column("Età", justify="left", style="bold blue", no_wrap=True)
    table.add_column("Lo Usano", justify="left", style="bold green", no_wrap=True)
    table.add_column("Non lo Usano", justify="left", style="yellow", no_wrap=True)
    table.add_column("Astenuti", justify="left", style="red", no_wrap=True)
    #Per ogni elemento del dizionario aggiungo i dati alla tabella 
    for i in dizionario:        
        lista = dizionario[i]
        table.add_row(i,str(lista[0]),str(lista[1]), str(lista[2]))
    #Stampo a schermo la tabella
    console.print(table)


if __name__ == "__main__":
    #Definisco i due dizionario
    Dizionario_2018 = Extract_2018()
    Dizionario_2019 = Extract_2019()
    #Definisco la console e le 2 tabelle
    console = Console()
    table_2018 = Table()
    table_2019 = Table()
    #Genero le due tabelle
    Printer(table_2018, Dizionario_2018, "2018")
    Printer(table_2019, Dizionario_2019, "2019")