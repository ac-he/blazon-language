from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, is_metal
from language.field import Field


class PerBend(Blazon, ABC):

    def __init__(self, blazon_json):
        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        if not self.chief:
            self.chief = {}

        self.chief = Field(self.chief, self.tinctures[0], "per bend", "chief")
        self.base = Field(self.base, self.tinctures[1], "per bend", "base")

    def get_pseudocode(self):
        variable = get_int_value(self.base)
        if is_metal(self.chief.field_tincture):
            return f"Output Variable{variable} as a number."
        else:
            return f"Output Variable{variable} as a character."

    def get_image(self):
        pass

    def get_program(self):
        pass
