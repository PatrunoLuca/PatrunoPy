from pygame.image import load as img_load
from pygame.transform import scale
from glob import glob
from os import walk, getcwd

def import_animations(path, x, y):
    full_path = f"{getcwd()}/{path}"
    folders = [folder for folder in  walk(full_path)][0][1]
    animations = {}
    for folder in folders:
        image_list = glob(f"{full_path}/{folder}/*.png")
        animations[folder] = [
            scale(img_load(image), (x, y)) 
            for image in image_list
            ]
    return animations

def zero_import_animations(path):
    full_path = f"{getcwd()}/{path}"
    folders = [folder for folder in  walk(full_path)][0][1]
    animations = {}
    for folder in folders:
        image_list = glob(f"{full_path}/{folder}/*.png")
        animations[folder] = [i[0:-4] for i in image_list]
    return animations