from Utils import *
from matplotlib import pyplot as plt

def graph(prima_dose0, seconda_dose0, regione0, prima_dose1, seconda_dose1, regione1, save=True):
    fig, ax = plt.subplots(1, 2, figsize=(50,20))
    ax[0].plot(prima_dose0.keys(), prima_dose0.values(), label = "Prima Dose") 
    ax[0].plot(seconda_dose0.keys(), seconda_dose0.values(), label = "Seconda Dose") 
    ax[1].plot(prima_dose1.keys(), prima_dose1.values(), label = "Prima Dose") 
    ax[1].plot(seconda_dose1.keys(), seconda_dose1.values(), label = "Seconda Dose")
    '''
    ax.xlabel('Date')
    ax.ylabel('Numero vaccini')
    ax.title(f"{regione0} -- {regione1}")
    '''
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.legend(loc='upper left') 
    if save is True:
        plt.savefig(f"{regione0} -- {regione1}.png") 
    plt.show()
   
df = extract("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.json")
regione0 = input("Regione0 --> ")
regione1 = input("Regione1 --> ")
graph(scrape_list(df, "Prima Dose", regione0), scrape_list(df, "Seconda Dose", regione0), regione0, scrape_list(df, "Prima Dose", regione1), scrape_list(df, "Seconda Dose", regione1), regione1)

#Grandezza grafici
#label e title
#tutti hanno lo stesso minimo e lo stesso massimo
#interfaccia grafica