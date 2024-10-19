# the charger takes in JSON
# and outputs an IMAGE GUID
import random
from datetime import datetime
from math import floor
from pathlib import Path
import cairo
from PIL import Image

from rendering import const
from rendering.const import canvas
from rendering.z_util_images import delete_image_path, delete_all_images
from rendering.trimmer import make_trimmed_image

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)

print_path = None
fx = None
new_page = None
pages = None
x = None
y = None
scale_w = None
scale_h = None
background = None
cur_printbox = None


def make_assembled_image(assembled_dict):
    global print_path, fx, pages, new_page

    create_print_settings(assembled_dict)

    for crest in assembled_dict.get("crests"):
        # create new page if needed
        if new_page:
            create_new_page(assembled_dict)

        # override shape if needed
        if assembled_dict.get("override-shapes"):
            count = len(assembled_dict.get("shapes"))
            index = floor(random.random() * count)
            crest["shape"] = assembled_dict.get("shapes")[index]

        # draw crest
        draw_crest(crest, x, y, scale_w, scale_h)
        if assembled_dict.get("overlay"):
            draw_overlay(assembled_dict.get("overlay"), crest["shape"], x, y, scale_w, scale_h)

        # get new crest position
        get_new_crest_position(assembled_dict)

    print_page(assembled_dict)


def get_new_crest_position(assembled_dict):
    global x, y, scale_w, scale_h, cur_printbox
    printboxes = assembled_dict.get("printboxes")
    printbox = printboxes[cur_printbox]

    x_limit = printbox.get("x") + printbox.get("w")
    x_next = printbox.get("kerning") + scale_w
    # If it fits on this line
    if x + x_next + scale_w <= x_limit:
        x += x_next

    # If it doesn't fit on this line
    else:
        y_limit = printbox.get("y") + printbox.get("h")
        y_next = printbox.get("line-spacing") + scale_h

        # If another line fits in this printbox
        if y + y_next + scale_h <= y_limit:
            x = printbox.get("x")
            y += y_next

        # If another line doesn't fit in this printbox
        else:
            cur_printbox += 1
            # If this is the last printbox
            if len(printboxes) <= cur_printbox:
                cur_printbox = 0
                print_page(assembled_dict)

            printbox = printboxes[cur_printbox]

            x = printbox.get("x")
            y = printbox.get("y")


def create_printboxes(assembled_dict):
    global x, y, cur_printbox
    cur_printbox = 0

    printboxes = assembled_dict.get("printboxes")
    printbox = printboxes[cur_printbox]

    x = printbox.get("x")
    y = printbox.get("y")


def create_print_settings(assembled_dict):
    global print_path, fx, background, scale_w, scale_h, new_page, pages, surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, assembled_dict.get("w"), assembled_dict.get("h"))
    context = cairo.Context(surface)

    print_name = "Page_"
    fx = ".png"
    print_dir = None

    background_str = str(Path.joinpath(Path.cwd(), "presets", "img", assembled_dict.get("background")))
    background = surface.create_from_png(background_str)

    scale_w = int(assembled_dict.get("crest-scale-width"))
    scale_h = int(assembled_dict.get("crest-scale-width") * canvas.get("h") / canvas.get("w"))

    if assembled_dict.get("print"):
        if assembled_dict["print"].get("clear-old-images"):
            delete_all_images()
        if assembled_dict["print"]["output-directory"] != "default":
            print_dir = assembled_dict["print"]["output-directory"]
        if assembled_dict["print"]["file-name-base"] != "default":
            print_name = assembled_dict["print"]["file-name-base"]
        if assembled_dict["print"].get("include-timestamp"):
            now = datetime.now()
            print_name = print_name + now.strftime("%d.%m.%y-%I.%M%p_")

    if print_dir:
        print_path = str(Path.joinpath(print_dir, print_name))
    else:
        print_path = str(Path.joinpath(Path.cwd(), "rendering", "img", print_name))

    create_printboxes(assembled_dict)
    new_page = True
    pages = 0


def print_page(assembled_dict):
    global print_path, fx, surface, new_page, pages
    draw_page_overlay(assembled_dict)
    page_name = print_path + str(pages) + fx
    surface.write_to_png(page_name)
    new_page = True


def create_new_page(assembled_dict):
    global new_page, pages, context, background

    new_page = False
    pages = pages + 1

    context.set_source_surface(background)
    context.rectangle(0, 0, assembled_dict.get("w"), assembled_dict.get("h"))
    context.fill()


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
            "name": str(Path.joinpath(Path.cwd(), "presets", "img", f"overlay_{name}.png"))
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


def draw_single_flag_with_overlay(crest, overlay_name, save_to):
    w = const.canvas["w"]
    h = const.canvas["h"]

    shape_dict = {
        "shape": crest.get("shape"),
        "field": {
            "name": str(Path.joinpath(Path.cwd(), "presets", "img", f"overlay_{overlay_name}.png"))
        }
    }

    # fetch trimmed image
    main_guid = make_trimmed_image(crest)
    overlay_guid = make_trimmed_image(shape_dict, True)

    # scale image
    main_image = Image.open(main_guid).resize((w, h))
    main_image.save(main_guid)
    overlay_image = Image.open(overlay_guid).resize((w, h))
    overlay_image.save(overlay_guid)

    # create surface
    main_surf = surface.create_from_png(main_guid)
    overlay_surf = surface.create_from_png(overlay_guid)

    # draw
    context.set_source_surface(main_surf)
    context.rectangle(0, 0, w, h)
    context.close_path()
    context.fill()

    context.set_source_surface(overlay_surf)
    context.rectangle(0, 0, w, h)
    context.close_path()
    context.fill()

    surface.write_to_png(save_to)

    # cleanup
    delete_image_path(main_guid)
    delete_image_path(overlay_guid)


def draw_page_overlay(assembled_dict):
    if assembled_dict.get("page-overlay"):
        name = assembled_dict["page-overlay"]
        w = assembled_dict["w"]
        h = assembled_dict["h"]

        overlay = str(Path.joinpath(Path.cwd(), "presets", "img", f"overlay_{name}.png"))

        # scale image
        image = Image.open(overlay).resize((w, h))
        image.save(overlay)

        # create surface
        surf1 = surface.create_from_png(overlay)

        # draw
        context.set_source_surface(surf1)
        context.rectangle(0, 0, w, h)
        context.close_path()
        context.fill()
