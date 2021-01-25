from os import remove 
from PIL import Image
import numpy as np

def Merge_Graph(file1, file2, ext):
    #Creo una lista con i file
    list_im = [f'{file1}.{ext}', f'{file2}.{ext}']
    #Trasformo quei file in oggetti immagine e li immagazzino in una lista
    imgs = [ Image.open(i) for i in list_im ]
    #Ordino la lista
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    #Trasformo la lista in un array e unisco gli elementi
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    #Trasformo l'array in un oggetto Image
    img= Image.fromarray( imgs_comb)
    #Salvo l'immagine
    img.save("Istat.png")
    #Elimino i due file che sono stati uniti
    remove("Utils/2018.png")
    remove("Utils/2019.png")
