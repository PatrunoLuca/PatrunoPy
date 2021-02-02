#Autore --> Luca Patruno
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure


def file_selector():
    global file_name
    try:
        file_name = tk.filedialog.askopenfile(mode='r', filetypes=[("File di testo", '*.txt'), ("Valori separati da una virgola", '*.csv')]).name
        text_box.delete(0,"end")
        text_box.insert(0, file_name)
    except:
        pass


def create_graphic():
    ListX = []
    ListY = []
    try:
        with open(text_box.get(), "r") as filename:
            for line in filename:
                valori = line.strip("\n").split(",")
                ListX.append(int(valori[0]))
                ListY.append(int(valori[1]))
        ListX.sort()
        ListY.sort()
        fig = Figure(figsize=(5, 4), dpi=100) 
        fig.add_subplot(111).scatter(ListX,ListY)
        canvas = FigureCanvasTkAgg(fig, master=app)
        canvas.draw() 
        toolbar = NavigationToolbar2Tk(canvas,app) 
        toolbar.update() 
        canvas.get_tk_widget().pack()
    except Exception as E:
        tk.messagebox.showerror("Errore",E)

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("500x500")
    app.title("Leggi File")
    app.resizable(False, False)

    choose_file_button = tk.Button(app, command=file_selector, text="Seleziona file", font = ("Tahoma",  12 ))
    choose_file_button.pack()
    choose_file_button.config(width=55)

    text_box = tk.Entry(app, text="", font = ("Tahoma",  12 ))
    text_box.pack()
    text_box.config(width=55)

    graphic_button = tk.Button(app, command=create_graphic, text="Genera il grafico",font = ("Tahoma",  12 ) )
    graphic_button.pack()
    graphic_button.config(width=55)

    app.mainloop()
