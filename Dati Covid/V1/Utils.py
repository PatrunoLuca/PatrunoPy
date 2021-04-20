import requests
from datetime import datetime, date

def lista_regioni():
    return [
        "Abruzzo",
        "Basilicata",
        "Calabria",
        "Campania",
        "Emilia-Romagna",
        "Friuli-Venezia Giulia",
        "Lazio",
        "Liguria",
        "Lombardia",
        "Marche",
        "Molise",
        "Piemonte",
        "Puglia",
        'Provincia Autonoma Bolzano / Bozen',
        'Provincia Autonoma Trento',
        "Sardegna",
        "Sicilia",
        "Toscana",
        "Umbria",
        "Valle d'Aosta / Vallée d'Aoste",
        "Veneto"
        ]

def scrape_list(base_list, element, region):
    nuova_lista = {}
    for i in base_list:
        if i["Nome Area"].lower() == region.lower():
            if i["Data"] not in nuova_lista.keys():
                nuova_lista[i["Data"]] = i[element]
            else:
                nuova_lista[i["Data"]] += i[element]
    return nuova_lista

def extract(url):
    dati_json = requests.get(url).json()
    return sorted([
        {
            "Data" : datetime.strptime(i["data_somministrazione"], "%Y-%m-%dT%H:%M:%S.000Z").date(),
            "Fascia Anagrafica" : i["fascia_anagrafica"],
            "Prima Dose" : i["prima_dose"],
            "Seconda Dose" : i["seconda_dose"],
            "Nome Area": i["nome_area"]
            } for i in dati_json[
                        list(dati_json.keys())[1]
                    ]
        ], key=lambda k: k['Data'])


def region_corrector(regione):
    if regione.lower() == 'provincia autonoma trento':
        return 'Trento'
    elif regione.lower() == 'provincia autonoma bolzano / bozen':
        return 'Bolzano'
    elif regione.lower() == "valle d'aosta / vallée d'aoste":
        return "Valle d'Aosta"
    else:
        return regione