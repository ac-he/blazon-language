from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, is_metal
from language.field import Field
from rendering.draw_dof import make_dof_image


class PerChevron(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "per chevron"
        self.shape = "heater"

        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        if not self.base:
            self.base = {}

        self.chief = Field(self.chief, self.tinctures[0], "per chevron", "chief")
        self.base = Field(self.base, self.tinctures[1], "per chevron", "base")

    def get_pseudocode(self):
        variable = get_int_value(self.chief)
        if is_metal(self.base.field_tincture):
            return f"Read in a character and store its value to Variable{variable}."
        else:
            return f"Generate a random integer 1-9 and store it to Variable{variable}."

    def get_program(self):
        pass
