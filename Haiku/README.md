# Progetto haiku

## Descrizione

**Nota: Inserire descrizione**

## Immagini

![Interfaccia](https://github.com/PatrunoLuca/PatrunoPY/blob/main/Haiku/interfaccia.png)

## Codice

``` python
from json import load
from random import choice

def extract(filename):
    with open("%s.json" % filename, "r") as outfile:
        return load(outfile)

def generate(json):
    return "\n".join(
        [
            str(choice(json["verso %s" % str(i)]))
            for i in range(1, len(json.items()) + 1)
            ]
        )

if __name__ == "__main__":
    json = extract("haiku")
    haiku = generate(json)
    print(haiku)
```

## File json

``` json
{
    "verso 1" : [
        "La mela dolce",
        "Stagione fredda",
        "Nel buio pesto",
        "Vola l'uccello",
        "candida neve"
    ],
    "verso 2" : [
        "l'altissima montagna",
        "la foglia scura cade ",
        "una luce improvvisa",
        "oltre l'albero spoglio",
        "discendi dal cielo blu"
    ],
    "verso 3" : [
        "calda estate",
        "il cielo grigio",
        "lumeggia tutto",
        "e giunge al nido",
        "imbianca l'erba"
    ]
}
```

## Divisione ruoli

Barile Luigi ➡  Creazione file json

Patruno Luca ➡ Creazione del codice

Ripoli Luca ➡ Cura delle grafice

Senese Walter ➡  Raccolta haiku
