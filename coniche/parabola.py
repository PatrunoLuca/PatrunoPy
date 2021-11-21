from conica import Conica
from retta import Retta

class Parabola(Conica):


    def __init__(self, a, b, c, asse_di_simmetria):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__punti = []
        super().__init__(a,b,c)
        
        assert asse_di_simmetria.lower() in ["x", "y"] 
        self.__asse_di_simmetria = asse_di_simmetria.lower()
        
        self.__delta = pow(self.__b, 2) - (4 * self.__a * self.__c)
        
        fuoco_x = - (self.__b / (2 * self.__a))
        fuoco_y = (1 - self.__delta) / (4 * self.__a)
        self.__fuoco = (fuoco_x, fuoco_y) if self.__asse_di_simmetria == "y" else (fuoco_y, fuoco_x)

        vertice_x = fuoco_x
        vertice_y =  - (self.__delta / (4 * self.__a))
        self.__vertice = (vertice_x, vertice_y) if self.__asse_di_simmetria == "y" else (vertice_y, vertice_x)

        coeff_direttrice = - ((1 + self.__delta) / (4 * self.__a))
        self.__direttrice = Retta(coeff_direttrice, 1, 0) if self.__asse_di_simmetria == "y" else Retta(1, coeff_direttrice, 0)

    def get_fuoco(self):
        return self.__fuoco
    
    def get_vertice(self):
        return self.__vertice
    
    def get_direttrice(self):
        return self.__direttrice

    def risolvi(self, noto=int):
        soluzione = (self.__a * pow(noto, 2)) + (self.__b * noto) + self.__c
        if self.__asse_di_simmetria == "y":
            self.__punti.append((noto, soluzione))
        else:
            self.__punti.append(( soluzione, noto))
        return soluzione

    #WIP
    @classmethod
    def from_fuoco_direttrice(fuoco, direttrice):
        pass
    
    #WIP
    @classmethod
    def intersezione(parabola, altro):
        pass