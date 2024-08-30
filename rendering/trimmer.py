# the trimmer takes in JSON
# and outputs an IMAGE GUID
import cairo

from const import canvas
from rendering.z_util_images import supply_guid, delete_image_path
from rendering.compositor import make_parted_image

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_trimmed_image(shape_dict, overlay=False):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    context = cairo.Context(surface)

    shape = shape_dict.get("shape")
    field = shape_dict.get("field")

    field["shape"] = shape

    match shape:
        case "banner":
            trim_to_banner(field, overlay)
        case "heater":
            trim_to_heater(field, overlay)
        case "pennant":
            trim_to_pennant(field, overlay)
        case "rect":
            if overlay:
                trim_to_rect(field)
            else:
                return make_parted_image(field)
        case "shield":
            trim_to_shield(field, overlay)
        case _:
            pass

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def trim_to_banner(field, overlay):
    if overlay:
        field_guid = field.get("name")
    else:
        field_guid = make_parted_image(field)

    surf1 = surface.create_from_png(field_guid)
    context.set_source_surface(surf1)

    context.move_to(0, 0)
    context.line_to(0, canvas["h"])
    context.line_to(canvas["w"] / 2, canvas["h"] * 3 / 4)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(canvas["w"], 0)
    context.close_path()

    context.fill()

    if overlay:
        pass
    else:
        delete_image_path(field_guid)


def trim_to_heater(field, overlay):
    if overlay:
        field_guid = field.get("name")
    else:
        field_guid = make_parted_image(field)

    surf1 = surface.create_from_png(field_guid)
    context.set_source_surface(surf1)

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

    context.fill()

    if overlay:
        pass
    else:
        delete_image_path(field_guid)


def trim_to_pennant(field, overlay):
    if overlay:
        field_guid = field.get("name")
    else:
        field_guid = make_parted_image(field)

    surf1 = surface.create_from_png(field_guid)
    context.set_source_surface(surf1)

    context.move_to(0, 0)
    context.line_to(canvas["w"]/2, canvas["h"])
    context.line_to(canvas["w"], 0)
    context.close_path()

    context.fill()

    if overlay:
        pass
    else:
        delete_image_path(field_guid)


def trim_to_rect(field):
    field_guid = field.get("name")

    surf1 = surface.create_from_png(field_guid)
    context.set_source_surface(surf1)

    context.move_to(0, 0)
    context.line_to(canvas["w"], 0)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(0, canvas["h"])
    context.close_path()

    context.fill()


def trim_to_shield(field, overlay):
    if overlay:
        field_guid = field.get("name")
    else:
        field_guid = make_parted_image(field)

    surf1 = surface.create_from_png(field_guid)
    context.set_source_surface(surf1)

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

    context.fill()

    if overlay:
        pass
    else:
        delete_image_path(field_guid)
