from pathlib import Path

import cairo

from blazon_language.rendering._render_config import canvas
from blazon_language.rendering.image_management import supply_guid, delete_image_path
from blazon_language.rendering._render_config import shape_points
from blazon_language.rendering.draw_dof import make_dof_image

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

    draw_shape(blazon.shape)
    context.fill()

    if overlay:
        draw_overlay(blazon.shape, overlay)

    guid = supply_guid()
    surface.write_to_png(guid)

    return guid


def draw_shape(shape, this_context=None, x_scale=1, y_scale=1, x_offset=0, y_offset=0):
    if not this_context:
        this_context = context
    points = shape_points[shape]
    for point in points:
        if point[0] == "m":
            this_context.move_to(canvas["w"] * point[1] * x_scale + x_offset,
                                 canvas["h"] * point[2] * y_scale + y_offset)
        if point[0] == "l":
            this_context.line_to(canvas["w"] * point[1] * x_scale + x_offset,
                                 canvas["h"] * point[2] * y_scale + y_offset)
        if point[0] == "c":
            this_context.curve_to(canvas["w"] * point[1][0] * x_scale + x_offset,
                                  canvas["h"] * point[1][1] * y_scale + y_offset,
                                  canvas["w"] * point[2][0] * x_scale + x_offset,
                                  canvas["h"] * point[2][1] * y_scale + y_offset,
                                  canvas["w"] * point[3][0] * x_scale + x_offset,
                                  canvas["h"] * point[3][1] * y_scale + y_offset)
    context.close_path()


def draw_overlay(shape, overlay):
    overlay_guid = str(Path.joinpath(Path.cwd(), "blazon_language", "presets", "img", f"overlay_{overlay}.png"))

    surface2 = cairo.ImageSurface(cairo.FORMAT_ARGB32, canvas["w"], canvas["h"])
    surf1 = surface2.create_from_png(overlay_guid)
    context.set_source_surface(surf1)

    # draw
    draw_shape(shape)
    context.fill()
