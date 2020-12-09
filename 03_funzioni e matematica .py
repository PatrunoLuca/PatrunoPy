def _zerominuscorrect(x):
    if x == -0 or -0.0:
        return 0.0
    else: 
        return x

def _swap(a,b):
    return b,a

def _equazione(a,b):
    return _zerominuscorrect(-b / a)  

def _massimo(lista):
    lista = list(lista)
    maggiore = 0
    for elemento in lista:
        if elemento > maggiore:
            maggiore = elemento
    return maggiore

if __name__ == "__main__":
    while True:
        print("Ciao, benvenuto nel mio programma!")
        x = 0
        while True:
            try:
                a = float(input("Quanto vale a? -> "))
                if a == 0:
                    raise IndexError
                b = float(input("Quanto vale b? -> "))
                break
            except ValueError:
                print("Numero non valido\nÈ possibile inserire solo numeri \n")
            except IndexError:
                print("Nell'equazione ax-b=0 la variabile a non può avere valore 0\n")
        x = _equazione(a,b)
        print(f"\nIl valore di 'a' è {a} mentre quello di 'b' è {b}.")
        print(f"Nell'equazione ax+b=0 , la variabile x è uguale a {x}")
        print(f"Il numero piu grande tra {a}, {b} e {x} è {_massimo([a,b,x])}")
        a,b = _swap(a,b)
        print("\nHo appena invertito le 2 variabili (a e b)")
        print(f"Adesso il nuovo valore di 'a' é {a} ed  il nuovo valore di 'b' é {b}")
        input("\nPremi 'ctrl' + 'c' per chiudere il programma o 'enter' per riutilizzarlo")

