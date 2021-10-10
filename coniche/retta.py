class Retta:
    
    NumeroRette = 0
    
    def __init__(self, a, b, c):
        if b == 0:
            raise ZeroDivisionError
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)
        self._punti = []
        self._m = - self._a / self._b
        Retta.NumeroRette += 1

    def trova_y(self, x=int):
        y = int((self._m * x) + self._c)
        self._punti.append((x, y))
        return y


    def lista(self):
        return self._punti

    def coppie(self, start=1, stop=int, step=1):
        return [(x, self.trova_y(x)) for x in range(start, stop, step)]

    def eq_implicita(self):
        x = f"{self._a}X" if self._a != 1.0 else "X"
        y = f"{self._b}Y" if self._b != 1.0 else "Y"
        segno = "+" if self._c > 0 else "-"
        c = f"{segno} {abs(self._c)}" if self._c != 0.0 else "" 
        return f"{x} + {y}{c} = 0"

    def eq_esplicita(self):
        segno = "+" if self._c > 0 else "-"
        c = f"{segno} {abs(self._c)}" if self._c != 0.0 else "" 
        x = f" {self._m}X " if self._m != 0.0 else ""
        return f"Y ={self._m} {c}"
    
    @classmethod
    def intersezione(cls, r1, r2):
        if type(r1) != Retta or type(r2) != Retta:
            raise Exception
        elif (r1._a, r1._b, r1._c) == (r2._a, r2._b, r2._c):
            return "Coincidenti"
        elif r1._m == r2._m:
            return "Paralleli"
        elif r1._m == (1/ r2._m):
            return "Perpendicolari"
        else:
            return "Incidenti"
 

if __name__ == "__main__":
    a1 = float(input("Inserisci valore di 'A' nella prima retta:    "))
    b1 = float(input("Inserisci valore di 'B' nella prima retta:    "))
    c1 = float(input("Inserisci valore di 'C' nella prima retta:    "))
    a2 = float(input("\nInserisci valore di 'A' nella seconda retta:  "))
    b2 = float(input("Inserisci valore di 'B' nella seconda retta:  "))
    c2 = float(input("Inserisci valore di 'C' nella seconda retta:  "))
    retta1 = Retta(a1, b1, c1)
    retta2 = Retta(a2, b2, c2)
    retta1.coppie(1, 20)
    retta2.coppie(1, 20)
    print(f"\n\nRetta 1:\n  Implicita: {retta1.eq_implicita()}\n  Esplicita: {retta1.eq_esplicita()}\n  Punti: {retta1.coppie(1,10)}")
    print(f"\n\nRetta 2:\n  Implicita: {retta2.eq_implicita()}\n  Esplicita: {retta2.eq_esplicita()}\n  Punti: {retta2.coppie(1,10)}")
    print(f"\n\nLe due rette sono: {Retta.intersezione(retta1, retta2)}")