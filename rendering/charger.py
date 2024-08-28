# the charger takes in JSON
# and outputs an IMAGE GUID
import os
import random
from math import floor, ceil

import cairo

import const
from const import canvas, tinctures, charge_loc, charge_size, charges
from presets.assembled_views import all_tinctures
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

    if charges.get(charge):
        if charges[charge]["type"] == "cm" or charges[charge]["type"] == "agoprsv":
            stamp_feature(charge, charge_dict.get("tincture"), charge_dict["quantity"], shape, dof, division,
                          charges[charge]["type"], charge_dict.get("charge-tincture"))
        elif charges[charge]["type"] == "geo":
            if charge == "label":
                draw_feature_label(charge_dict.get("charge-tincture"), charge_dict["quantity"], shape, dof, division)
            if charge == "quarterly_of_eight":
                draw_feature_quarterly_of_eight(charge_dict.get("charge-tincture"), shape, dof, division)
        elif charges[charge]["type"] == "oversize":
            draw_feature_oversize(charge, shape, dof, division, charge_dict.get("charge-tincture"))

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def set_field_tincture(tincture):
    global surface, context
    context.set_source_rgb(tinctures[tincture]["r"], tinctures[tincture]["g"], tinctures[tincture]["b"])
    context.rectangle(0, 0, canvas["w"], canvas["h"])
    context.fill()


def stamp_feature(charge, tincture, quantity, shape, dof, field, c_type, c_tincture):
    if c_type == "cm":
        suffix = "_m.png"
        if tinctures[tincture].get("type") == "colour":
            suffix = "_c.png"
    else:
        suffix = f"_{c_tincture}.png"

    size = charge_loc[dof][field][shape][quantity]["size"]

    size_d = "f"
    for letter, value in charge_size.items():
        if size is value:
            size_d = letter

    path = f"{os.getcwd()}\\rendering\\assets\\{c_type}\\{size_d}\\{charge}{suffix}"

    for stamp in range(0, quantity):
        loc_x = charge_loc[dof][field][shape][quantity]["loc_x"][stamp]
        loc_y = charge_loc[dof][field][shape][quantity]["loc_y"][stamp]

        surf1 = surface.create_from_png(path)
        context.set_source_surface(surf1, loc_x, loc_y)
        context.rectangle(loc_x, loc_y, size, size)
        context.close_path()
        context.fill()


def draw_feature_quarterly_of_eight(tincture_list, shape, dof, division):
    global surface, context
    fess_line = const.charge_detail["qoe"][dof][division][shape]["fess"]
    dexter_line = const.charge_detail["qoe"][dof][division][shape]["dexter"]
    pale_line = const.charge_detail["qoe"][dof][division][shape]["pale"]
    sinister_line = const.charge_detail["qoe"][dof][division][shape]["sinister"]

    fesses = [0, fess_line, canvas['h']]
    pales = [0, dexter_line, pale_line, sinister_line, canvas['w']]

    if isinstance(tincture_list, str):
        t = []
        for i in range(8):
            t.append(all_tinctures[floor(random.random() * 7)])
    else:
        t = tincture_list

    for quarter in range(8):
        color = tinctures[t[quarter]]

        top = fesses[floor((quarter / 4) + 0.01)]
        bottom = fesses[ceil((quarter / 4) + 0.01)]
        left = pales[(quarter % 4) - 0]
        right = pales[(quarter % 4) + 1]

        context.set_source_rgb(color["r"], color["g"], color["b"])
        context.move_to(left, top)
        context.line_to(right, top)
        context.line_to(right, bottom)
        context.line_to(left, bottom)

        context.close_path()
        context.fill()


def draw_feature_label(feature_tincture, quantity, shape, dof, division):
    global surface, context
    context.set_source_rgb(tinctures[feature_tincture]["r"], tinctures[feature_tincture]["g"],
                           tinctures[feature_tincture]["b"])

    bar_h = const.charge_detail["label"][dof][division][shape]["bar_h"]
    bar_y = const.charge_detail["label"][dof][division][shape]["bar_y"]
    center = const.charge_detail["label"][dof][division][shape]["center"]
    spacing = const.charge_detail["label"][dof][division][shape]["spacing"]

    label_in_y = bar_y + bar_h * 0.500
    label_out_y = bar_y + bar_h * 1.750
    label_w = bar_h * 1.01

    label_centers = []
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


def draw_feature_oversize(charge, shape, dof, field, c_tincture):
    path = f"{os.getcwd()}\\rendering\\assets\\oversize\\{charge}_{c_tincture}.png"
    midpoint = charge_loc[dof][field][shape][1]["size"] / 2
    loc_x = charge_loc[dof][field][shape][1]["loc_x"][0] + midpoint - 500
    loc_y = charge_loc[dof][field][shape][1]["loc_y"][0] + midpoint - 500

    surf1 = surface.create_from_png(path)
    context.set_source_surface(surf1, loc_x, loc_y)
    context.rectangle(loc_x, loc_y, 1000, 1000)
    context.close_path()
    context.fill()
