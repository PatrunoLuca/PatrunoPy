import matplotlib.pyplot as plt
from guizero import *

def file_selector():
    try:
        file_name = app.select_file(filetypes=[["File di testo", "*.txt"]])
        if file_name != "":
            text_box.value = file_name
    except:
        pass



def create_graphic():
    ListX = []
    ListY = []
    try:
        with open(text_box.value, "r") as filename:
            for line in filename:
                valori = line.strip("\n").split(",")
                ListX.append(int(valori[0]))
                ListY.append(int(valori[1]))
        ListX.sort()
        ListY.sort()
        plt.scatter(ListX,ListY)
        #Creo il grafico a dispersione
        plt.savefig("grafico.png")
        picture = Picture(app, image="grafico.png")
    except Exception as E:
        app.error("Errore",E)
        
        
if __name__ == "__main__":    
    app = App(title="Leggi File",width=640, height=580 )
    choose_file_button = PushButton(app, text="Seleziona file",command=file_selector, width="fill")
    text_box = TextBox(app, width="fill")
    graphic_button = PushButton(app, text="Genera grafico",command=create_graphic, width="fill")
    app.display()