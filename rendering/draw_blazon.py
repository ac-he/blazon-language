from pathlib import Path

import cairo

from rendering._render_config import canvas
from rendering._image_management import supply_guid, delete_image_path
from rendering.draw_dof import make_dof_image

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_blazon_image(blazon, overlay=None):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    context = cairo.Context(surface)

    blazon_guid = make_dof_image(blazon)
    surf1 = surface.create_from_png(blazon_guid)
    context.set_source_surface(surf1)
    delete_image_path(blazon_guid)

    match blazon.shape:
        case "banner": trim_to_banner()
        case "heater": trim_to_heater()
        case "pennant": trim_to_pennant()
        case "rect": trim_to_rect()
        case "shield": trim_to_shield()
    context.fill()

    if overlay:
        draw_overlay(blazon.shape, overlay)

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def trim_to_banner():
    context.move_to(0, 0)
    context.line_to(0, canvas["h"])
    context.line_to(canvas["w"] / 2, canvas["h"] * 3 / 4)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(canvas["w"], 0)
    context.close_path()


def trim_to_heater():
    context.move_to(0, 0)
    context.line_to(0, canvas["h"] * 5 / 8)
    context.curve_to(0, canvas["h"] * 7 / 8,
                     canvas["w"] / 3, canvas["h"] * 7.5 / 8,
                     canvas["w"] / 2, canvas["h"])
    context.curve_to(canvas["w"] * 2 / 3, canvas["h"] * 7.5 / 8,
                     canvas["w"], canvas["h"] * 7 / 8,
                     canvas["w"], canvas["h"] * 5 / 8)
    context.line_to(canvas["w"], 0)
    context.close_path()


def trim_to_pennant():
    context.move_to(0, 0)
    context.line_to(canvas["w"]/2, canvas["h"])
    context.line_to(canvas["w"], 0)
    context.close_path()


def trim_to_rect():
    context.rectangle(0, 0, canvas["w"], canvas["h"])


def trim_to_shield():
    context.move_to(0, 0)
    context.line_to(canvas["w"] * 0 / 6, canvas["h"] * 6 / 8)
    context.curve_to(canvas["w"] * 0 / 6, canvas["h"] * 7 / 8,
                     canvas["w"] * 3 / 6, canvas["h"] * 7 / 8,
                     canvas["w"] * 3 / 6, canvas["h"] * 8 / 8)
    context.curve_to(canvas["w"] * 3 / 6, canvas["h"] * 7 / 8,
                     canvas["w"] * 6 / 6, canvas["h"] * 7 / 8,
                     canvas["w"] * 6 / 6, canvas["h"] * 6 / 8)
    context.line_to(canvas["w"], 0)
    context.close_path()


def draw_overlay(shape, overlay):
    overlay_guid = str(Path.joinpath(Path.cwd(), "presets", "img", f"overlay_{overlay}.png"))

    surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    surf1 = surface2.create_from_png(overlay_guid)
    context.set_source_surface(surf1)

    # draw
    match shape:
        case "banner": trim_to_banner()
        case "heater": trim_to_heater()
        case "pennant": trim_to_pennant()
        case "rect": trim_to_rect()
        case "shield": trim_to_shield()
    context.fill()
