from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, is_metal
from language.field import Field
from rendering.draw_dof import make_dof_image


class PerBendSinister(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "per bend sinister"
        self.shape = "heater"

        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        if not self.chief:
            self.chief = {}

        self.chief = Field(self.chief, self.tinctures[0], "per bend sinister", "chief")
        self.base = Field(self.base, self.tinctures[1], "per bend sinister", "base")

    def get_pseudocode(self):
        variable = get_int_value(self.base)
        if is_metal(self.chief.field_tincture):
            return f"Output '{variable}'."
        else:
            if variable == 32:
                return f"Output newline, the character value of {variable}."
            else:
                return f"Output '{chr(variable)}', the character value of {variable}."

    def get_program(self):
        pass
