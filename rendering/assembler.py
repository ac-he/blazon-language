# the charger takes in JSON
# and outputs an IMAGE GUID
from datetime import datetime
import os

import cairo
from PIL import Image

from const import canvas
from rendering.z_util_images import delete_image_path, supply_guid, delete_all_images
from rendering.trimmer import make_trimmed_image

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_assembled_image(assembled_dict):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, assembled_dict.get("w"), assembled_dict.get("h"))
    context = cairo.Context(surface)

    print_dir = os.getcwd() + "\\rendering\\img"
    print_name = "Page_"
    if assembled_dict.get("print"):
        if assembled_dict["print"].get("clear-old-images"):
            delete_all_images()

        is_pdf = assembled_dict["print"]["pdf"]
        fx = ".png"

        if assembled_dict["print"]["output-directory"] != "default":
            print_dir = assembled_dict["print"]["output-directory"]
        if assembled_dict["print"]["file-name-base"] != "default":
            print_name = assembled_dict["print"]["file-name-base"]
        if assembled_dict["print"].get("include-timestamp"):
            now = datetime.now()
            print_name = print_name + now.strftime("%d.%m.%y-%I.%M%p_")

    else:
        is_pdf = False
        fx = ".png"

    print_path = f"{print_dir}\\{print_name}"

    background_str = os.getcwd() + "\\presets\\img\\" + assembled_dict.get("background")
    print(background_str)
    background = surface.create_from_png(background_str)

    scale_w = int(assembled_dict.get("crest-scale-width"))
    scale_h = int(assembled_dict.get("crest-scale-width") * canvas.get("h") / canvas.get("w"))

    new_page = True
    pages = 0
    x = 0
    y = 0
    for crest in assembled_dict.get("crests"):
        # create new page if needed
        if new_page:
            new_page = False
            pages = pages + 1

            x = assembled_dict.get("margin-x")
            y = assembled_dict.get("margin-y")

            context.set_source_surface(background)
            context.rectangle(0, 0, assembled_dict.get("w"), assembled_dict.get("h"))
            context.fill()

        # draw crest
        if assembled_dict.get("override-shapes"):
            crest["shape"] = "rect"

        draw_crest(crest, x, y, scale_w, scale_h)

        if assembled_dict.get("overlay"):
            draw_overlay(assembled_dict.get("overlay"), crest["shape"], x, y, scale_w, scale_h)

        # get new crest position
        x = x + assembled_dict.get("kerning") + scale_w
        if (x + scale_w) > (assembled_dict.get("w") - assembled_dict.get("margin-x")):
            x = assembled_dict.get("margin-x")
            y = y + assembled_dict.get("line-spacing") + scale_h
        if (y + scale_h) > (assembled_dict.get("h") - assembled_dict.get("margin-y")):
            page_name = print_path + str(pages) + fx
            surface.write_to_png(page_name)
            new_page = True

    page_name = print_path + str(pages) + fx
    surface.write_to_png(page_name)


def draw_crest(crest, x, y, w, h):
    # fetch trimmed image
    trimmed_guid = make_trimmed_image(crest)

    # scale image
    image = Image.open(trimmed_guid).resize((w, h))
    image.save(trimmed_guid)

    # create surface
    surf1 = surface.create_from_png(trimmed_guid)

    # draw
    context.set_source_surface(surf1, x, y)
    context.rectangle(x, y, w, h)
    context.close_path()
    context.fill()

    # cleanup
    delete_image_path(trimmed_guid)


def draw_overlay(name, shape, x, y, w, h):
    shape_dict = {
        "shape": shape,
        "field": {
            "name": f"{os.getcwd()}\\presets\\img\\overlay_{name}.png"
        }
    }

    # fetch trimmed image
    trimmed_guid = make_trimmed_image(shape_dict, True)

    # scale image
    image = Image.open(trimmed_guid).resize((w, h))
    image.save(trimmed_guid)

    # create surface
    surf1 = surface.create_from_png(trimmed_guid)

    # draw
    context.set_source_surface(surf1, x, y)
    context.rectangle(x, y, w, h)
    context.close_path()
    context.fill()

    # cleanup
    delete_image_path(trimmed_guid)
