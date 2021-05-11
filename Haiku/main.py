from json import load
from random import choice
from tkinter import Tk, Label, Button
from pyperclip import copy

#Creo una classe app
class App:
    #Definisco i widget
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x300")
        self.master.title("Haiku Generator")
        self.master.resizable(width=False, height=False)

        self.label = Label(self.master, text="GENERATORE HAIKU")
        self.label.pack()
        self.label.config(font=("Times", 35), justify="center")

        self.haiku_button = Button(self.master, text="Genera", command=self.generate_haiku)
        self.haiku_button.pack()
        self.haiku_button.config(font=("Times", 15), justify="center", width=70)

        self.haiku1 = Label(self.master, text="")
        self.haiku1.pack()
        self.haiku1.config(font=("Times", 15), justify="center")

        self.haiku2 = Label(self.master, text="")
        self.haiku2.pack()
        self.haiku2.config(font=("Times", 15), justify="center")

        self.haiku3 = Label(self.master, text="")
        self.haiku3.pack()
        self.haiku3.config(font=("Times", 15), justify="center")

        self.copy_button = Button(self.master, text="Copia", command=self.copy_haiku)
        self.copy_button.pack()
        self.copy_button.config(font=("Times", 15), justify="center", width=70)

    #Apre il file "haiku.json", estrae un elemento casuale per ogni verso e li assegna ai 3 label
    def generate_haiku(self):
        with open("haiku.json", "r") as outfile:
            self.haiku1["text"], self.haiku2["text"], self.haiku3["text"] = [str(choice(i)) for i in load(outfile).values()]

    #Copia l'haiku nella clipboard
    def copy_haiku(self):
        copy("\n".join([self.haiku1["text"], self.haiku2["text"], self.haiku3["text"]]))


if __name__ == "__main__":
    root = Tk()
    my_gui = App(root)
    root.mainloop()
