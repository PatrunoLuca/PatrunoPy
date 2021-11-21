class Conica:
    
    NumeroConiche = 0
    
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__punti = []
        Conica.NumeroConiche += 1

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_punti(self):
        return self.__punti

    def risolvi(self, noto=int):
        pass #dipende dalla singola conica

    def coppie(self, start=1, stop=int, step=1):
        return [(x, self.risolvi(x)) for x in range(start, stop, step)] if self.get_simmetria() == "y" else [(self.risolvi(y) ,y) for y in range(start, stop, step)]