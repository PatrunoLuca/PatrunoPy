#https://github.com/italia/covid19-opendata-vaccini
#data somministrazione(2), fascia anagrafica, prima dose, seconda dose, nome area
from datetime import datetime, date
import matplotlib.pyplot as plt
from random import randint
from Utils import *

def graph(prima_dose, seconda_dose, regione, save=True):
    plt.plot(prima_dose.keys(),  prima_dose.values(), label = "Prima Dose") 
    plt.plot(seconda_dose.keys(),  seconda_dose.values(), label = "Seconda Dose") 
    plt.xlabel('Date') 
    plt.ylabel('Numero vaccini') 
    plt.title(regione)
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.legend(loc='upper left') 
    if save is True:
        plt.savefig(f"Grafici/{regione}.png") 
    plt.show()

if __name__ == '__main__':
    plt.ion()
    lista = extract("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.json")
 
    for regione in lista_regioni(): 
        prima_dose = scrape_list(lista, "Prima Dose", regione)
        seconda_dose = scrape_list(lista, "Seconda Dose", regione)
        graph(prima_dose, seconda_dose, region_corrector(regione))
        plt.clf()
