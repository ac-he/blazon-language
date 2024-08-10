import os
from random import random
import cairo
from PIL import Image

from const import canvas, charge_size


def supply_guid():
    return os.getcwd() + "\\rendering\\img\\" + str(random()) + ".png"


def delete_image_path(path):
    if os.path.isfile(path):
        os.remove(path)


def delete_all_images(base="\\rendering\\img"):
    path = os.getcwd() + base
    for i in os.listdir(path):
        delete_image_path(path + "\\" + i)


def configure_svg_assets():
    png_path = os.getcwd() + "\\rendering\\assets\\png\\"

    delete_all_images(png_path + "l")
    delete_all_images(png_path + "m")
    delete_all_images(png_path + "s")

    for i in os.listdir(png_path + "f"):
        for letter, size in charge_size.items():
            if letter != "f":
                image = Image.open(png_path + "f\\" + i).resize((int(size), int(size)))
                image.save(png_path + letter + "\\" + i)
