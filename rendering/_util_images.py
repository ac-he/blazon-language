import os
from random import random


def supply_guid():
    return os.getcwd() + "\\rendering\\img\\" + str(random()) + ".png"


def delete_image_path(path):
    if os.path.isfile(path):
        os.remove(path)


def delete_all_images():
    path = os.getcwd() + "\\rendering\\img"
    for i in os.listdir(path):
        delete_image_path(path + "\\" + i)
