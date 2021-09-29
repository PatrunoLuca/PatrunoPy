from datetime import datetime

class Videogame:
    
    def __init__(self, name=str, company=str, pegi=int, platform=tuple, release_date=datetime, genre=tuple, theme=str):
        self.name = name
        self.company = company
        self.pegi = pegi
        self.platform = platform
        self.release_date = release_date.date()
        self.genre = genre
        self.theme = theme
    
    def is_out(self):
        if self.release_date > datetime.now().date():
            return False
        return True

    def change_data(self, new_date=datetime):
        self.release_date = new_date.date()

    def __str__(self):
        return f"{self.name}:\n" + "\n".join([f"\t{i} : {self.__dict__[i]}" for i in self.__dict__ if i != "name"])

    def __repr__(self):
        return "Videogame({})".format(", ".join([str(self.__dict__[i]) for i in self.__dict__]))

if __name__ == "__main__":
    The_Witcher = Videogame(
        "The Witcher 3: Wild Hunt",
        "CD Project Red",
        18,
        ("PS4", "XBOX ONE", "WINDOWS"),
        datetime(2015, 5, 19),
        ("Action RPG"),
        "Medieval Fantasy"
        )
    
    print(The_Witcher)
    print(repr(The_Witcher))
    print(The_Witcher.is_out())
    The_Witcher.change_data(datetime(2022, 3, 3))
    print(f"{The_Witcher.name} release date was succesfully changed!")
    print(The_Witcher.is_out())