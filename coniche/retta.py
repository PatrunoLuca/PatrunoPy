class Retta:
    
    NumeroRette = 0
    
    def __init__(self, a, b, c):
        self._a = float(a)
        self._b = float(b)
        self._c = float(c)
        if (self._a, self._b) == (0.0, 0.0):
            raise Exception(f"{self.eq_implicita()} non è una retta")
        self._punti = []
        if b != 0:
            self._m = - self._a / self._b
        else:
            self._m = None
        Retta.NumeroRette += 1

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def get_m(self):
        return self._m

    def get_punti(self):
        return self._punti

    def trova_y(self, x=int):
        y = int((self._m * x) + self._c)
        self._punti.append((x, y))
        return y

    def coppie(self, start=1, stop=int, step=1):
        return [(x, self.trova_y(x)) for x in range(start, stop, step)]

    def eq_implicita(self):
        x = f"{self._a}X" if self._a != 1.0 else "X"
        y = f"{self._b}Y" if self._b != 1.0 else "Y"
        segno = "+" if self._c >= 0 else "-"
        c = f"{segno} {abs(self._c)}"
        return f"{x} + {y} {c} = 0"

    def eq_esplicita(self):
        segno = "+" if self._c > 0 else "-"
        c = f"{segno} {abs(self._c)}"
        x = f"{self._m}X "
        if (c, x) != ("+ 0.0","0.0X"):
            return f"Y = {self._m} {c}" 
        else:
            return "Y = 0"
    
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

    #WIP funzione che crea un oggetto retta a partire da una lista di punti
    @classmethod
    def from_punti(cls, punti):
        assert len(punti) == 2
        assert type(punti) == list
        a,b,c= [1, 2, 3]
        return cls(a, b, c)
    
    #WIP funzione che crea un oggetto retta a partire dal coefficiente angolare ed un punto
    @classmethod
    def from_coeff(cls, m, punto):
        assert len(punto) == 2
        assert type(punto) == tuple
        a,b,c= [1, 2, 3]
        return cls(a, b, c)
 

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