from conica import Conica

class Retta(Conica):


    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__punti = []
        
        super().__init__(a,b,c)
        
        if (self.__a, self.__b) == (0.0, 0.0):
            raise Exception(f"{self.eq_implicita()} non è una retta")
        if b == 0.0:
            self.__asse_di_simmetria = "x"
            self.__m = 0.0
        else:
            self.__asse_di_simmetria = "y"
            self.__m = - self.__a / self.__b

    def get_simmetria(self):
        return self.__asse_di_simmetria

    def get_m(self):
        return self.__m

    def risolvi(self, noto=int):
        soluzione = int((self.__m * noto) + self.__c)
        if self.__asse_di_simmetria == "y":
            self.__punti.append((noto, soluzione))
        else:
            self.__punti.append(( soluzione, noto))
        return soluzione

    def eq_implicita(self):
        segno_x = "" if self.__a >= 0 else "- "
        segno_y = "+" if self.__b >= 0 else "-"
        segno_c = "+" if self.__c >= 0 else "-"
        
        x = f"{segno_x}{self.__a}X" if self.__a != 1.0 else f"{segno_x}X"
        y = f"{segno_y} {abs(self.__b)}Y" if abs(self.__b) != 1.0 else f"{segno_y} Y"
        c = f"{segno_c} {abs(self.__c)}"
        return f"{segno_x}{x} {y} {c} = 0"

    def eq_esplicita(self):
        x_y = "Y" if self.__asse_di_simmetria == "y" else "X"
        m = f"{self.__m}X " if self.__asse_di_simmetria == "y" else f"{self.__m}Y "
        
        if self.__m == 0.0:
            segno = "" if self.__c >= 0 else "- "
            return f"{x_y} = {segno}{self.__c}"
        elif self.__c != 0.0:
            segno = "+" if self.__c >= 0 else "-"
            return f"{x_y} = {m} {segno} {abs(self.__c)}" 
        else:
            return f"{x_y} = 0"

    
    @classmethod
    def intersezione(cls, r1, r2):
        if type(r1) != Retta or type(r2) != Retta:
            raise Exception
        elif (r1.get_a(), r1.get_b(), r1.get_c()) == (r2.get_a(), r2.get_b(), r2.get_c()):
            return "Coincidenti"
        elif r1.get_m() == r2.get_m():
            return None
        else:
            det = (r1.get_a() * r2.get_b()) - (r2.get_a() * r1.get_b())
            det_x = (r1.get_c() * r2.get_b()) - (r2.get_c() * r1.get_b())
            det_y = (r1.get_a() * r2.get_c()) - (r2.get_a() * r1.get_c())
            return (det_x / det, det_y / det)

    @classmethod
    def from_points(cls, punto1, punto2):
        assert len(punto1) == 2 
        assert len(punto2) == 2
        assert type(punto1) == tuple 
        assert type(punto2) == tuple
        
        x = (punto2[0] - punto1[0])
        y = (punto2[1] - punto1[1])
        m = y/x 
        q = punto1[-1] - (m * punto1[0])
        return cls(m, -1, q)
    
    @classmethod
    def from_coeff(cls, m, punto):
        assert len(punto) == 2
        assert type(punto) == tuple
        assert type(m) == float
        
        q = punto[-1] - (m * punto[0])
        return cls(m, -1, q)

    @classmethod
    def from_intercepts(cls, q, punto):
        assert len(punto) == 2
        assert type(punto) == tuple
        assert type(q) == float
        
        m = (punto[-1] - q) / punto[0]
        return cls(m, -1, q) 

if __name__ == "__main__":
    m = float(input("Inserisci valore di 'm' nella prima retta:    "))
    x = float(input("Inserisci valore di 'x' del punto nella prima retta:    "))
    y = float(input("Inserisci valore di 'y' del punto nella prima retta:    "))
    x1 = float(input("\nInserisci valore di 'x1' nella seconda retta:  "))
    y1 = float(input("Inserisci valore di 'y1' nella seconda retta:  "))
    x2 = float(input("Inserisci valore di 'x2' nella seconda retta:  "))
    y2 = float(input("Inserisci valore di 'y2' nella seconda retta:  "))

    retta1 = Retta.from_coeff(m, (x, y))
    retta2 = Retta.from_points((x1, y1), (x2, y2))

    retta1.coppie(1, 20)
    retta2.coppie(1, 20)
    print(f"\n\nRetta 1:\n  Implicita: {retta1.eq_implicita()}\n  Esplicita: {retta1.eq_esplicita()}\n  Punti: {retta1.coppie(1,10)}")
    print(f"\n\nRetta 2:\n  Implicita: {retta2.eq_implicita()}\n  Esplicita: {retta2.eq_esplicita()}\n  Punti: {retta2.coppie(1,10)}")
    print(f"\n\nIl punto in cui le due rette si incontrano è il punto: {Retta.intersezione(retta1, retta2)}")