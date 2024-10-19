import os
from random import random
from pathlib import Path
from PIL import Image
from rendering.const import charge_size


def supply_guid():
    return Path.joinpath(Path.cwd(), 'rendering', 'img', str(random()) + ".png")


def delete_image_path(path):
    if os.path.isfile(path):
        os.remove(path)


def delete_all_images():
    path = Path.joinpath(Path.cwd(), 'rendering', 'img')
    for i in os.listdir(path):
        delete_image_path(path.joinpath(i))


def configure_svg_assets():
    img_sets = ["cm", "agoprsv"]
    scaling_sizes = ["l", "m", "s", "xs"]

    for img_set in img_sets:
        for size in scaling_sizes:
            path = Path.joinpath(Path.cwd(), 'rendering', 'assets', img_set, size)
            for i in os.listdir(path):
                delete_image_path(path.joinpath(i))

        png_path = Path.joinpath(Path.cwd(), 'rendering', 'assets', img_set)
        f_path = png_path.joinpath("f")
        for f_image in os.listdir(f_path):
            for size in scaling_sizes:
                image_path = f_path.joinpath(f_image)
                save_path = png_path.joinpath(size, f_image)
                resize = int(charge_size[size])

                image = Image.open(image_path).resize((resize, resize))
                image.save(save_path)
