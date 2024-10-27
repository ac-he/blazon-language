import cairo
from blazon_language.rendering._render_config import canvas
from blazon_language.rendering.draw_division import make_division_image
from blazon_language.rendering._image_management import supply_guid, delete_image_path

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
context = cairo.Context(surface)


def make_dof_image(blazon):
    global surface, context
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    context = cairo.Context(surface)

    match blazon.division:
        case "per nothing": return make_division_image(blazon.field, blazon.shape)
        case "per bend": per_bend(blazon)
        case "per bend sinister": per_bend_sinister(blazon)
        case "per chevron": per_chevron(blazon)
        case "per cross": per_cross(blazon)
        case "per fess": per_fess(blazon)
        case "per fess escutcheon": per_fess_escutcheon(blazon)
        case "per pale": per_pale(blazon)
        case "per pall": per_pall(blazon)
        case "per saltire": per_saltire(blazon)
        case _: return

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def per_bend(blazon):
    side_intersect = canvas["h"]
    if blazon.shape == "pennant":
        side_intersect = canvas["h"] * 5 / 8

    db_guid = make_division_image(blazon.base, blazon.shape)
    surf1 = surface.create_from_png(db_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(0, canvas["h"])
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(canvas["w"], side_intersect)
    context.close_path()
    context.fill()
    delete_image_path(db_guid)

    sc_guid = make_division_image(blazon.chief, blazon.shape)
    surf2 = surface.create_from_png(sc_guid)
    context.set_source_surface(surf2)
    context.move_to(0, 0)
    context.line_to(canvas["w"], 0)
    context.line_to(canvas["w"], side_intersect)
    context.close_path()
    context.fill()
    delete_image_path(sc_guid)


def per_bend_sinister(blazon):
    side_intersect = canvas["h"]
    if blazon.shape == "pennant":
        side_intersect = canvas["h"] * 5 / 8

    dc_guid = make_division_image(blazon.chief, blazon.shape)
    surf1 = surface.create_from_png(dc_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"], 0)
    context.line_to(0, 0)
    context.line_to(0, side_intersect)
    context.close_path()
    context.fill()
    delete_image_path(dc_guid)

    sb_guid = make_division_image(blazon.base, blazon.shape)
    surf2 = surface.create_from_png(sb_guid)
    context.set_source_surface(surf2)
    context.move_to(canvas["w"], 0)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(0, canvas["h"])
    context.line_to(0, side_intersect)
    context.close_path()
    context.fill()
    delete_image_path(sb_guid)


def per_chevron(blazon):
    middle_side_h = canvas["h"] * 5 / 8
    middle_middle_h = canvas["h"] * 3 / 8
    if blazon.shape == "banner" or blazon.shape == "shield":
        middle_side_h = canvas["h"] * 4.5 / 8
        middle_middle_h = canvas["h"] * 2.5 / 8

    chief_guid = make_division_image(blazon.chief, blazon.shape)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"] * 0 / 6, canvas["h"] * 0 / 8)
    context.line_to(canvas["w"] * 0 / 6, middle_side_h)
    context.line_to(canvas["w"] * 3 / 6, middle_middle_h)
    context.line_to(canvas["w"] * 6 / 6, middle_side_h)
    context.line_to(canvas["w"] * 6 / 6, canvas["h"] * 0 / 8)
    context.close_path()
    context.fill()
    delete_image_path(chief_guid)

    base_guid = make_division_image(blazon.base, blazon.shape)
    surf2 = surface.create_from_png(base_guid)
    context.set_source_surface(surf2)
    context.move_to(canvas["w"] * 0 / 6, middle_side_h)
    context.line_to(canvas["w"] * 0 / 6, canvas["h"] * 8 / 8)
    context.line_to(canvas["w"] * 6 / 6, canvas["h"] * 8 / 8)
    context.line_to(canvas["w"] * 6 / 6, middle_side_h)
    context.line_to(canvas["w"] * 3 / 6, middle_middle_h)
    context.close_path()
    context.fill()
    delete_image_path(base_guid)


def per_cross(blazon):
    center_w = canvas["w"] / 2
    center_h = canvas["h"] / 2
    if blazon.shape == "pennant":
        center_h = canvas["h"] * 3 / 8
    elif blazon.shape == "banner" or blazon.shape == "shield" or blazon.shape == "heater":
        center_h = canvas["h"] * 3.5 / 8

    dc_guid = make_division_image(blazon.dexter_chief, blazon.shape)
    surf1 = surface.create_from_png(dc_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, center_w, center_h)
    context.fill()
    delete_image_path(dc_guid)

    sc_guid = make_division_image(blazon.sinister_chief, blazon.shape)
    surf1 = surface.create_from_png(sc_guid)
    context.set_source_surface(surf1)
    context.rectangle(center_w, 0, center_w, center_h)
    context.fill()
    delete_image_path(sc_guid)

    sb_guid = make_division_image(blazon.sinister_base, blazon.shape)
    surf1 = surface.create_from_png(sb_guid)
    context.set_source_surface(surf1)
    context.rectangle(center_w, center_h, center_w, canvas["h"] - center_h)
    context.fill()
    delete_image_path(sb_guid)

    db_guid = make_division_image(blazon.dexter_base, blazon.shape)
    surf1 = surface.create_from_png(db_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, center_h, center_w, canvas["h"] - center_h)
    context.fill()
    delete_image_path(db_guid)


def per_fess(blazon):
    fess = canvas["h"] / 2
    if blazon.shape == "pennant":
        fess = canvas["h"] * 3 / 8
    elif blazon.shape == "banner" or blazon.shape == "shield" or blazon.shape == "heater":
        fess = canvas["h"] * 3.5 / 8

    chief_guid = make_division_image(blazon.chief, blazon.shape)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, canvas["w"], fess)
    context.fill()
    delete_image_path(chief_guid)

    base_guid = make_division_image(blazon.base, blazon.shape)
    surf2 = surface.create_from_png(base_guid)
    context.set_source_surface(surf2)
    context.rectangle(0, fess, canvas["w"], canvas["h"] - fess)
    context.fill()
    delete_image_path(base_guid)


def per_fess_escutcheon(blazon):
    escutcheon_scale = 0.5
    fess = canvas["h"] / 2

    if blazon.shape == "pennant":
        fess = canvas["h"] * 3 / 8
        escutcheon_scale = 0.375
    elif blazon.shape == "banner" or blazon.shape == "shield" or blazon.shape == "heater":
        fess = canvas["h"] * 3.5 / 8

    esc_scale_w = canvas["w"] * escutcheon_scale
    esc_scale_h = canvas["h"] * escutcheon_scale
    esc_w = (canvas["w"] - esc_scale_w) / 2
    esc_h = fess - esc_scale_h / 2

    chief_guid = make_division_image(blazon.chief, blazon.shape)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, canvas["w"], fess)
    context.fill()
    delete_image_path(chief_guid)

    base_guid = make_division_image(blazon.base, blazon.shape)
    surf2 = surface.create_from_png(base_guid)
    context.set_source_surface(surf2)
    context.rectangle(0, fess, canvas["w"], canvas["h"] - fess)
    context.fill()
    delete_image_path(base_guid)

    escutcheon_guid = make_division_image(blazon.escutcheon, blazon.shape)
    surf3 = surface.create_from_png(escutcheon_guid)
    context.set_source_surface(surf3)
    context.move_to(esc_w + 0.000 * esc_scale_w, esc_h + 0.000 * esc_scale_h)
    context.line_to(esc_w + 0.000 * esc_scale_w, esc_h + 0.625 * esc_scale_h)
    context.curve_to(esc_w + 0.000 * esc_scale_w, esc_h + 0.875 * esc_scale_h,
                     esc_w + 0.333 * esc_scale_w, esc_h + 0.938 * esc_scale_h,
                     esc_w + 0.500 * esc_scale_w, esc_h + 1.000 * esc_scale_h)
    context.curve_to(esc_w + 0.667 * esc_scale_w, esc_h + 0.938 * esc_scale_h,
                     esc_w + 1.000 * esc_scale_w, esc_h + 0.875 * esc_scale_h,
                     esc_w + 1.000 * esc_scale_w, esc_h + 0.625 * esc_scale_h)
    context.line_to(esc_w + 1.000 * esc_scale_w, esc_h + 0.000 * esc_scale_h)
    context.close_path()
    context.fill()
    delete_image_path(escutcheon_guid)


def per_pale(blazon):
    dexter_guid = make_division_image(blazon.dexter, blazon.shape)
    surf1 = surface.create_from_png(dexter_guid)
    context.set_source_surface(surf1)
    context.rectangle(0, 0, canvas["w"] / 2, canvas["h"])
    context.fill()
    delete_image_path(dexter_guid)

    sinister_guid = make_division_image(blazon.sinister, blazon.shape)
    surf2 = surface.create_from_png(sinister_guid)
    context.set_source_surface(surf2)
    context.rectangle(canvas["w"] / 2, 0, canvas["w"] / 2, canvas["h"])
    context.fill()
    delete_image_path(sinister_guid)


def per_pall(blazon):
    center_x = canvas["w"] * 3 / 6
    center_y = canvas["h"] * 4 / 8
    if blazon.shape == "pennant":
        center_y = canvas["h"] * 2.5 / 8

    chief_guid = make_division_image(blazon.chief, blazon.shape)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(center_x, center_y)
    context.line_to(canvas["w"], 0)
    context.close_path()
    context.fill()
    delete_image_path(chief_guid)

    dexter_guid = make_division_image(blazon.dexter, blazon.shape)
    surf2 = surface.create_from_png(dexter_guid)
    context.set_source_surface(surf2)
    context.move_to(0, 0)
    context.line_to(0, canvas["h"])
    context.line_to(center_x, canvas["h"])
    context.line_to(center_x, center_y)
    context.close_path()
    context.fill()
    delete_image_path(dexter_guid)

    sinister_guid = make_division_image(blazon.sinister, blazon.shape)
    surf2 = surface.create_from_png(sinister_guid)
    context.set_source_surface(surf2)
    context.move_to(canvas["w"], 0)
    context.line_to(canvas["w"], canvas["h"])
    context.line_to(center_x, canvas["h"])
    context.line_to(center_x, center_y)
    context.close_path()
    context.fill()
    delete_image_path(sinister_guid)


def per_saltire(blazon):
    center_w = canvas["w"] / 2
    center_h = canvas["h"] / 2
    if blazon.shape == "pennant":
        center_h = canvas["h"] * 3 / 8
    elif blazon.shape == "heater" or blazon.shape == "shield" or blazon.shape == "banner":
        center_h = canvas["h"] * 3.5 / 8
    side_intersect = center_h * 2

    chief_guid = make_division_image(blazon.chief, blazon.shape)
    surf1 = surface.create_from_png(chief_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(center_w, center_h)
    context.line_to(canvas["w"], 0)
    context.fill()
    delete_image_path(chief_guid)

    sinister_guid = make_division_image(blazon.sinister, blazon.shape)
    surf1 = surface.create_from_png(sinister_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"], side_intersect)
    context.line_to(center_w, center_h)
    context.line_to(canvas["w"], 0)
    context.fill()
    delete_image_path(sinister_guid)

    base_guid = make_division_image(blazon.base, blazon.shape)
    surf1 = surface.create_from_png(base_guid)
    context.set_source_surface(surf1)
    context.move_to(canvas["w"], canvas["h"])
    context.line_to(canvas["w"], side_intersect)
    context.line_to(center_w, center_h)
    context.line_to(0, side_intersect)
    context.line_to(0, canvas["h"])
    context.fill()
    delete_image_path(base_guid)

    dexter_guid = make_division_image(blazon.dexter, blazon.shape)
    surf1 = surface.create_from_png(dexter_guid)
    context.set_source_surface(surf1)
    context.move_to(0, 0)
    context.line_to(center_w, center_h)
    context.line_to(0, side_intersect)
    context.fill()
    delete_image_path(dexter_guid)

