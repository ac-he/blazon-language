import os
from random import random
import cairo
from const import canvas


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
    png_path = "\\rendering\\assets\\png"
    svg_path = os.getcwd() + "\\rendering\\assets\\svg"
    delete_all_images(png_path)

    for i in os.listdir(svg_path):
        name = i[0:len(i)-4]
        i_svg_path = svg_path + "\\" + i
        i_svg2_path = svg_path + "\\2" + i
        i_png_path = os.getcwd() + png_path + "\\" + name + ".png"

        # os.popen(f"cp {i_svg_path} {i_svg2_path}")
        #
        # surf = cairo.SVGSurface(i_svg2_path, canvas["w"], canvas["h"])
        # surf.write_to_png(i_png_path)

        # https://www.youtube.com/watch?v=QQtJOsIg8hs
