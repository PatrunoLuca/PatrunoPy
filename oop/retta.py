class Retta:
    
    NumeroRette = 0
    
    def __init__(self, coeff_X=int, coeff_Y=int, noto=int):
        if coeff_X == 0 or coeff_Y == 0:
            raise ZeroDivisionError
        self.coeff_X = coeff_X
        self.coeff_Y = coeff_Y
        self.noto = noto
        self.punti = []
        Retta.NumeroRette += 1

    def trova_y(self, x=int):
        y = int(((self.coeff_X * x) + self.noto) / self.coeff_Y)
        self.punti.append((x, y))
        return y

    def trova_x(self, y=int):
        x = int(((self.coeff_Y * y) - self.noto) / self.coeff_X)
        self.punti.append((x, y))
        return x

    def lista(self):
        return self.punti

    def coppie(self, start=1, stop=int, step=1):
        return [(x, self.trova_y(x)) for x in range(start, stop, step)]

    def __str__(self):
        x = f"{self.coeff_X}X" if self.coeff_X != 1.0 else "X"
        y = f"{self.coeff_Y}Y" if self.coeff_Y != 1.0 else "Y"
        segno = "+" if self.noto > 0 else "-"
        noto = f"{segno} {self.noto}" if self.noto != 0.0 else "" 
        return f"{y} = {x} {noto}"

    def __repr__(self):
        return f"Retta({self.coeff_X}X, {self.coeff_Y}Y, {self.noto})"

if __name__ == "__main__":
    retta1 = Retta(1, 1, -4)
    retta1.trova_x(5)
    retta1.trova_y(8)
    print(retta1)
    print(retta1.lista())
    print(repr(retta1))
    print(retta1.coppie(8))