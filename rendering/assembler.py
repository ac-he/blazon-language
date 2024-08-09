# the charger takes in JSON
# and outputs an IMAGE GUID
import os

import cairo
from PIL import Image

from const import canvas
from rendering.z_util_images import delete_image_path, supply_guid
from rendering.trimmer import make_trimmed_image

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_assembled_image(assembled_dict):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, assembled_dict.get("w"), assembled_dict.get("h"))
    context = cairo.Context(surface)

    background_str = os.getcwd() + "\\presets\\img\\" + assembled_dict.get("background")
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

            x = assembled_dict.get("margin")
            y = assembled_dict.get("margin")

            context.set_source_surface(background)
            context.rectangle(0, 0, assembled_dict.get("w"), assembled_dict.get("h"))
            context.fill()

        # draw crest
        draw_crest(assembled_dict, crest, x, y, scale_w, scale_h)

        # get new crest position
        x = x + assembled_dict.get("kerning") + scale_w
        if (x + scale_w) > (assembled_dict.get("w") - assembled_dict.get("margin")):
            x = assembled_dict.get("margin")
            y = y + assembled_dict.get("line-spacing") + scale_h
        if (y + scale_h) > (assembled_dict.get("h") - assembled_dict.get("margin")):
            page_name = os.getcwd() + "\\rendering\\img\\Page_" + str(pages) + ".png"
            surface.write_to_png(page_name)
            new_page = True

    page_name = os.getcwd() + "\\rendering\\img\\Page_" + str(pages) + ".png"
    surface.write_to_png(page_name)


def draw_crest(assembled_dict, crest, x, y, w, h):
    if assembled_dict.get("override-shapes"):
        crest["shape"] = "rect"

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
