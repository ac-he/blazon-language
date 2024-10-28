import math
import random
from pathlib import Path

import cairo
from PIL import Image

from blazon_language.rendering._image_management import delete_image_path
from blazon_language.rendering._render_config import canvas
from blazon_language.rendering.draw_blazon import make_blazon_image


class DrawBlazonList:
    def __init__(self, blazon_list, image_settings):
        self.settings = image_settings

        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.settings.width, self.settings.height)
        self.context = cairo.Context(self.surface)

        self.print_name = "Page_"
        self.fx = ".png"
        self.print_dir = None
        self.shape_index = -1

        self.cur_printbox = 0
        self.x = self.settings.printboxes[self.cur_printbox].x
        self.y = self.settings.printboxes[self.cur_printbox].y

        if self.settings.background_path == "builtins":
            background_str = str(Path.joinpath(Path.cwd(), "blazon_language", "presets", "img", self.settings.background))
        else:
            background_str = self.settings.background_path
        self.background = self.surface.create_from_png(background_str)

        self.scale_w = int(self.settings.crest_scale_width)
        self.scale_h = int(self.scale_w * canvas.get("h") / canvas.get("w"))

        self.print_path = str(Path.joinpath(Path(self.settings.output_destination), "blazon_as_image-page"))

        self.new_page = True
        self.pages = 0

        for blazon in blazon_list:
            # create new page if needed
            if self.new_page:
                self.create_new_page()

            shape_len = len(self.settings.shapes)
            if self.settings.randomize_shapes:
                self.shape_index = math.floor(random.random() * shape_len)
            else:
                self.shape_index += 1
                self.shape_index %= shape_len

            # draw crest
            self.draw_blazon_in_image(blazon)

            # get new crest position
            self.get_new_position()

        self.print_page()

    def get_new_position(self):
        printbox = self.settings.printboxes[self.cur_printbox]

        x_limit = printbox.x + printbox.w
        x_next = printbox.kerning + self.scale_w
        # If it fits on this line
        if self.x + x_next + self.scale_w <= x_limit:
            self.x += x_next

        # If it doesn't fit on this line
        else:
            y_limit = printbox.y + printbox.h
            y_next = printbox.line_spacing + self.scale_h

            # If another line fits in this printbox
            if self.y + y_next + self.scale_h <= y_limit:
                self.x = printbox.x
                self.y += y_next

            # If another line doesn't fit in this printbox
            else:
                self.cur_printbox += 1
                # If this is the last printbox
                if len(self.settings.printboxes) <= self.cur_printbox:
                    self.cur_printbox = 0
                    self.print_page()

                printbox = self.settings.printboxes[self.cur_printbox]

                self.x = printbox.x
                self.y = printbox.y

    def print_page(self):
        self.draw_page_overlay()
        page_name = self.print_path + str(self.pages) + ".png"
        self.surface.write_to_png(page_name)
        self.new_page = True

    def create_new_page(self):
        self.new_page = False
        self.pages += 1

        self.context.set_source_surface(self.background)
        self.context.rectangle(0, 0, self.settings.width, self.settings.height)
        self.context.fill()

    def draw_blazon_in_image(self, blazon):
        blazon.shape = self.settings.shapes[self.shape_index]
        blazon_guid = make_blazon_image(blazon, self.settings.image_overlay)

        # scale image
        image = Image.open(blazon_guid).resize((self.scale_w, self.scale_h))
        image.save(blazon_guid)

        # create surface
        surf1 = self.surface.create_from_png(blazon_guid)

        # draw
        self.context.set_source_surface(surf1, self.x, self.y)
        self.context.rectangle(self.x, self.y, self.scale_w, self.scale_h)
        self.context.close_path()
        self.context.fill()

        # cleanup
        delete_image_path(blazon_guid)

    def draw_page_overlay(self):
        if self.settings.page_overlay:
            overlay = str(Path.joinpath(Path.cwd(), "blazon_language", "presets", "img",
                                        f"overlay_{self.settings.page_overlay}.png"))

            # scale image
            image = Image.open(overlay).resize((self.settings.width, self.settings.height))
            image.save(overlay)

            # create surface
            surf1 = self.surface.create_from_png(overlay)

            # draw
            self.context.set_source_surface(surf1)
            self.context.rectangle(0, 0, self.settings.width, self.settings.height)
            self.context.close_path()
            self.context.fill()