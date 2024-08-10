# the charger takes in JSON
# and outputs an IMAGE GUID
import os

import cairo
from PIL import Image
from const import canvas, tinctures, charge_loc, charge_size
from rendering.z_util_images import supply_guid

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_charge_image(charge_dict, shape="rect", dof="per fess", division="chief"):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    context = cairo.Context(surface)

    set_field_tincture(charge_dict.get("tincture"))
    charge = charge_dict.get("charge")

    if not charge_dict.get("quantity"):
        charge_dict["quantity"] = 1

    match charge:
        case "label":
            draw_feature_label(charge_dict.get("charge-tincture"), charge_dict.get("quantity"))
            pass
        case None:
            pass
        case _:
            stamp_feature(charge, charge_dict.get("tincture"), charge_dict["quantity"], shape, dof, division)

    pass

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def set_field_tincture(tincture):
    global surface, context
    context.set_source_rgb(tinctures[tincture]["r"], tinctures[tincture]["g"], tinctures[tincture]["b"])
    context.rectangle(0, 0, canvas["w"], canvas["h"])
    context.fill()


def stamp_feature(charge, tincture, quantity, shape, dof, field):
    suffix = "_m.png"
    if tinctures[tincture].get("type") == "colour":
        suffix = "_c.png"

    size = charge_loc[dof][field][shape][quantity]["size"]

    size_d = "f"
    for letter, value in charge_size.items():
        if size is value:
            size_d = letter

    path = os.getcwd() + "\\rendering\\assets\\png\\" + size_d + "\\" + charge + suffix

    for stamp in range(0, quantity):
        loc_x = charge_loc[dof][field][shape][quantity]["loc_x"][stamp]
        loc_y = charge_loc[dof][field][shape][quantity]["loc_y"][stamp]

        surf1 = surface.create_from_png(path)
        context.set_source_surface(surf1, loc_x, loc_y)
        context.rectangle(loc_x, loc_y, size, size)
        context.close_path()
        context.fill()


def draw_feature_label(feature_tincture, quantity):
    global surface, context
    context.set_source_rgb(tinctures[feature_tincture]["r"], tinctures[feature_tincture]["g"],
                           tinctures[feature_tincture]["b"])

    for i in range(quantity):
        context.move_to(130, 250 + i * 200)
        context.line_to(190, 150 + i * 200)
        context.line_to(250, 250 + i * 200)
        context.close_path()

        context.move_to(290, 250 + i * 200)
        context.line_to(350, 150 + i * 200)
        context.line_to(410, 250 + i * 200)
        context.close_path()
        context.fill()

        context.move_to(450, 250 + i * 200)
        context.line_to(510, 150 + i * 200)
        context.line_to(570, 250 + i * 200)
        context.close_path()
        context.fill()

        context.rectangle(0, 130 + i * 200, canvas["w"], 70)
        context.fill()

