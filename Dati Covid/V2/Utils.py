import requests
from datetime import datetime, date
import pandas as pd

def extract(url):
    dati_json = requests.get(url).json()
    return pd.DataFrame(sorted([
        {
            "Data" : datetime.strptime(i["data_somministrazione"], "%Y-%m-%dT%H:%M:%S.000Z").date(),
            "Fascia Anagrafica" : i["fascia_anagrafica"],
            "Fornitore" : i["fornitore"],
            "Prima Dose" : i["prima_dose"],
            "Seconda Dose" : i["seconda_dose"],
            "Nome Area": i["nome_area"]
            } for i in dati_json[
                        list(dati_json.keys())[1]
                    ]
        ], key=lambda k: k['Data']))

def region_corrector(regione):
    if regione.lower() == 'provincia autonoma trento':
        return 'Trento'
    elif regione.lower() == 'provincia autonoma bolzano / bozen':
        return 'Bolzano'
    elif regione.lower() == "valle d'aosta / vallée d'aoste":
        return "Valle d'Aosta"
    else:
        return regione

def scrape_list(df, element, region):
    nuova_lista = {}
    for index, rows in df.iterrows():
        if rows["Nome Area"].lower() == region.lower(): #and rows["Fornitore"].lower() == foritore.lower():
            if rows["Data"] not in nuova_lista.keys():
                nuova_lista[rows["Data"]] = rows[element]
            else:
                nuova_lista[rows["Data"]] += rows[element]
    return nuova_lista
