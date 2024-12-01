from math import floor, ceil

import cairo
from pathlib import Path

from blazon_language.language._evaluation import integerify_quantity, charges, stringify_charge
from blazon_language.rendering._image_management import supply_guid
from blazon_language.rendering._render_config import canvas, tinctures, charge_loc, charge_size, charge_detail

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_division_image(field, shape="rect"):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    context = cairo.Context(surface)

    set_field_tincture(field.field_tincture)

    qf_charge = charges.get(field.get_render_friendly_charge())
    if qf_charge:
        charge_type = qf_charge["type"]
        if charge_type == "cm" or charge_type == "agoprsv":
            stamp_feature(field, shape, charge_type)
        elif charge_type == "geo":
            charge = stringify_charge(field.charge)
            if charge == "alabelof":
                draw_feature_label(field, shape)
            if charge == "quarterlyofeight":
                draw_feature_quarterly_of_eight(field, shape)
        elif charge_type == "oversize":
            draw_feature_oversize(field, shape)

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def set_field_tincture(tincture):
    global surface, context
    context.set_source_rgb(tinctures[tincture]["r"], tinctures[tincture]["g"], tinctures[tincture]["b"])
    context.rectangle(0, 0, canvas["w"], canvas["h"])
    context.fill()


def stamp_feature(field, shape, charge_type):
    if charge_type == "cm":
        suffix = "_m.png"
        if tinctures[field.field_tincture].get("type") == "color":
            suffix = "_c.png"
    else:
        tincture = tinctures[field.charge_tincture]["initial"]
        suffix = f"_{tincture}.png"

    charge = charge_loc[field.dof][field.division]
    quantity = integerify_quantity(field.charge_quantity)

    size = charge[shape][quantity]["size"]
    size_d = "f"
    for letter, value in charge_size.items():
        if size is value:
            size_d = letter

    path = Path.joinpath(Path.cwd(), "blazon_language", "rendering", "assets", charge_type, size_d,
                         field.get_render_friendly_charge() + suffix)

    for stamp in range(0, quantity):
        loc_x = charge[shape][quantity]["loc_x"][stamp]
        loc_y = charge[shape][quantity]["loc_y"][stamp]

        surf1 = surface.create_from_png(str(path))
        context.set_source_surface(surf1, loc_x, loc_y)
        context.rectangle(loc_x, loc_y, size, size)
        context.close_path()
        context.fill()


def draw_feature_quarterly_of_eight(field, shape):
    global surface, context
    line = charge_detail["qoe"][field.dof][field.division][shape]
    fess_line = line["fess"]
    dexter_line = line["dexter"]
    pale_line = line["pale"]
    sinister_line = line["sinister"]

    fesses = [0, fess_line, canvas['h']]
    pales = [0, dexter_line, pale_line, sinister_line, canvas['w']]

    for quarter in range(8):
        tincture = tinctures.get(field.charge_tincture[quarter * 2])

        top = fesses[floor((quarter / 4) + 0.01)]
        bottom = fesses[ceil((quarter / 4) + 0.01)]
        left = pales[(quarter % 4) - 0]
        right = pales[(quarter % 4) + 1]

        context.set_source_rgb(tincture["r"], tincture["g"], tincture["b"])
        context.move_to(left, top)
        context.line_to(right, top)
        context.line_to(right, bottom)
        context.line_to(left, bottom)

        context.close_path()
        context.fill()


def draw_feature_label(field, shape):
    global surface, context
    point = charge_detail["label"][field.dof][field.division][shape]
    context.set_source_rgb(tinctures[field.charge_tincture]["r"], tinctures[field.charge_tincture]["g"],
                           tinctures[field.charge_tincture]["b"])

    bar_h = point["bar_h"]
    bar_y = point["bar_y"]
    center = point["center"]
    spacing = point["spacing"]

    label_in_y = bar_y + bar_h * 0.500
    label_out_y = bar_y + bar_h * 1.750
    label_w = bar_h * 1.01

    label_centers = []
    quantity = integerify_quantity(field.charge_quantity)
    if quantity == 1:
        label_centers = [center]
    elif quantity == 2:
        label_centers = [center - spacing / 2, center + spacing / 2]
    elif quantity == 3:
        label_centers = [center - spacing, center, center + spacing]

    for label in label_centers:
        context.move_to(label - label_w/2, label_out_y)
        context.line_to(label, label_in_y)
        context.line_to(label + label_w/2, label_out_y)
        context.close_path()

    context.rectangle(0, bar_y, canvas["w"], bar_h)
    context.fill()


def draw_feature_oversize(field, shape):
    tincture = tinctures[field.charge_tincture]["initial"]
    path = Path.joinpath(Path.cwd(), "blazon_language", "rendering", "assets", "oversize",
                         f"{field.charge}_{tincture}.png")

    surf1 = surface.create_from_png(str(path))
    if field.charge == "gorge" or field.charge == "fret" or field.charge == "gyronny":
        if field.charge != "fret" and (
                field.dof == "saltire" or field.dof == "bend" or field.dof == "bend sinister"):
            loc_x = charge_detail["qoe"][field.dof][field.division][shape]["pale"] - 500
            loc_y = charge_detail["qoe"][field.dof][field.division][shape]["fess"] - 500
        else:
            midpoint = charge_loc[field.dof][field.division][shape][1]["size"] / 2
            loc_x = charge_loc[field.dof][field.division][shape][1]["loc_x"][0] + midpoint - 500
            loc_y = charge_loc[field.dof][field.division][shape][1]["loc_y"][0] + midpoint - 500
        context.set_source_surface(surf1, loc_x, loc_y)
        context.rectangle(loc_x, loc_y, 1000, 1000)
    else:
        context.set_source_surface(surf1)
        context.rectangle(0, 0, 1000, 1000)
    context.close_path()
    context.fill()
