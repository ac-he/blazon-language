# the compositor takes in JSON
# and outputs an IMAGE GUID
import cairo

from const import canvas
from rendering.charger import make_charge_image
from rendering._util_images import supply_guid, delete_image_path

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_parted_image(party_dict):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    context = cairo.Context(surface)

    party = party_dict.get("party")

    match party:
        case "per bend":
            per_bend(party_dict.get("dexter-base"), party_dict.get("sinister-chief"))
        case "per bend sinister":
            per_bend_sinister(party_dict.get("dexter-chief"), party_dict.get("sinister-base"))
        case "per chevron":
            per_chevron(party_dict.get("chief"), party_dict.get("base"))
        case "per cross":
            per_cross(party_dict.get("dexter-chief"), party_dict.get("sinister-chief"), party_dict.get("sinister-base"),
                      party_dict.get("dexter-base"))
        case "per fess":
            per_fess(party_dict.get("chief"), party_dict.get("base"))
        case "per pale":
            per_pale(party_dict.get("dexter"), party_dict.get("sinister"))
        case "per pall":
            per_pall(party_dict.get("chief"), party_dict.get("dexter"), party_dict.get("sinister"))
        case "per saltire":
            per_saltire(party_dict.get("chief"), party_dict.get("sinister"), party_dict.get("base"),
                        party_dict.get("dexter"), )
        case _:
            pass

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def per_bend(dexter_base, sinister_chief):
    db_guid = make_charge_image(dexter_base)
    surf1 = surface.create_from_png(db_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(0, canvas["h"])
    context.line_to(canvas["w"], canvas["h"])
    context.close_path()
    context.fill()
    delete_image_path(db_guid)

    sc_guid = make_charge_image(sinister_chief)
    surf2 = surface.create_from_png(sc_guid)
    context.set_source_surface(surf2)
    context.move_to(0, 0)
    context.line_to(canvas["w"], 0)
    context.line_to(canvas["w"], canvas["h"])
    context.close_path()
    context.fill()
    delete_image_path(sc_guid)


def per_bend_sinister(dexter_chief, sinister_base):
    dc_guid = make_charge_image(dexter_chief)
    surf1 = surface.create_from_png(dc_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"], 0)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(0, canvas["h"])
    context.close_path()
    context.fill()
    delete_image_path(dc_guid)

    sb_guid = make_charge_image(sinister_base)
    surf2 = surface.create_from_png(sb_guid)
    context.set_source_surface(surf2)
    context.move_to(canvas["w"], 0)
    context.line_to(0, 0)
    context.line_to(0, canvas["h"])
    context.close_path()
    context.fill()
    delete_image_path(sb_guid)


def per_chevron(chief, base):
    chief_guid = make_charge_image(chief)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"] * 0 / 6, canvas["h"] * 0 / 8)
    context.line_to(canvas["w"] * 0 / 6, canvas["h"] * 5 / 8)
    context.line_to(canvas["w"] * 3 / 6, canvas["h"] * 3 / 8)
    context.line_to(canvas["w"] * 6 / 6, canvas["h"] * 5 / 8)
    context.line_to(canvas["w"] * 6 / 6, canvas["h"] * 0 / 8)
    context.close_path()
    context.fill()
    delete_image_path(chief_guid)

    base_guid = make_charge_image(base)
    surf2 = surface.create_from_png(base_guid)
    context.set_source_surface(surf2)
    context.move_to(canvas["w"] * 0 / 6, canvas["h"] * 5 / 8)
    context.line_to(canvas["w"] * 0 / 6, canvas["h"] * 8 / 8)
    context.line_to(canvas["w"] * 6 / 6, canvas["h"] * 8 / 8)
    context.line_to(canvas["w"] * 6 / 6, canvas["h"] * 5 / 8)
    context.line_to(canvas["w"] * 3 / 6, canvas["h"] * 3 / 8)
    context.close_path()
    context.fill()
    delete_image_path(base_guid)


def per_cross(dexter_chief, sinister_chief, sinister_base, dexter_base):
    center_w = canvas["w"] / 2
    center_h = canvas["h"] / 2

    dc_guid = make_charge_image(dexter_chief)
    surf1 = surface.create_from_png(dc_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, center_w, center_h)
    context.fill()
    delete_image_path(dc_guid)

    sc_guid = make_charge_image(sinister_chief)
    surf1 = surface.create_from_png(sc_guid)
    context.set_source_surface(surf1)
    context.rectangle(center_w, 0, center_w, center_h)
    context.fill()
    delete_image_path(sc_guid)

    sb_guid = make_charge_image(sinister_base)
    surf1 = surface.create_from_png(sb_guid)
    context.set_source_surface(surf1)
    context.rectangle(center_w, center_h, center_w, center_h)
    context.fill()
    delete_image_path(sb_guid)

    db_guid = make_charge_image(dexter_base)
    surf1 = surface.create_from_png(db_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, center_h, center_w, center_h)
    context.fill()
    delete_image_path(db_guid)


def per_fess(chief, base):
    chief_guid = make_charge_image(chief)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, canvas["w"], canvas["h"] / 2)
    context.fill()
    delete_image_path(chief_guid)

    base_guid = make_charge_image(base)
    surf2 = surface.create_from_png(base_guid)
    context.set_source_surface(surf2)
    context.rectangle(0, canvas["h"]/2, canvas["w"], canvas["h"] / 2)
    context.fill()
    delete_image_path(base_guid)


def per_pale(dexter, sinister):
    dexter_guid = make_charge_image(dexter)
    surf1 = surface.create_from_png(dexter_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, canvas["w"] / 2, canvas["h"])
    context.fill()
    delete_image_path(dexter_guid)

    sinister_guid = make_charge_image(sinister)
    surf2 = surface.create_from_png(sinister_guid)
    context.set_source_surface(surf2)
    context.rectangle(canvas["w"] / 2, 0, canvas["w"] / 2, canvas["h"])
    context.fill()
    delete_image_path(sinister_guid)


def per_pall(chief, dexter, sinister):
    center_x = canvas["w"] * 3 / 6
    center_y = canvas["h"] * 4 / 8

    chief_guid = make_charge_image(chief)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(center_x, center_y)
    context.line_to(canvas["w"], 0)
    context.close_path()
    context.fill()
    delete_image_path(chief_guid)

    dexter_guid = make_charge_image(dexter)
    surf2 = surface.create_from_png(dexter_guid)
    context.set_source_surface(surf2)
    context.move_to(0, 0)
    context.line_to(0, canvas["h"])
    context.line_to(center_x, canvas["h"])
    context.line_to(center_x, center_y)
    context.close_path()
    context.fill()
    delete_image_path(dexter_guid)

    sinister_guid = make_charge_image(sinister)
    surf2 = surface.create_from_png(sinister_guid)
    context.set_source_surface(surf2)
    context.move_to(canvas["w"], 0)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(center_x, canvas["h"])
    context.line_to(center_x, center_y)
    context.close_path()
    context.fill()
    delete_image_path(sinister_guid)


def per_saltire(chief, sinister, base, dexter):
    center_w = canvas["w"] / 2
    center_h = canvas["h"] / 2

    chief_guid = make_charge_image(chief)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(center_w, center_h)
    context.line_to(canvas["w"], 0)
    context.fill()
    delete_image_path(chief_guid)

    sinister_guid = make_charge_image(sinister)
    surf1 = surface.create_from_png(sinister_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"], canvas["h"])
    context.line_to(center_w, center_h)
    context.line_to(canvas["w"], 0)
    context.fill()
    delete_image_path(sinister_guid)

    base_guid = make_charge_image(base)
    surf1 = surface.create_from_png(base_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"], canvas["h"])
    context.line_to(center_w, center_h)
    context.line_to(0, canvas["h"])
    context.fill()
    delete_image_path(base_guid)

    dexter_guid = make_charge_image(dexter)
    surf1 = surface.create_from_png(dexter_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(center_w, center_h)
    context.line_to(0, canvas["h"])
    context.fill()
    delete_image_path(dexter_guid)
