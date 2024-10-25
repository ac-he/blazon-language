from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, is_metal
from language.field import Field


class PerBendSinister(Blazon, ABC):

    def __init__(self, blazon_json):
        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        if not self.chief:
            self.chief = {}

        self.chief = Field(self.chief, self.tinctures[0])
        self.base = Field(self.base, self.tinctures[1])

    def get_pseudocode(self):
        variable = get_int_value(self.base)
        if is_metal(self.chief.field_tincture):
            return f"Output '{variable}'."
        else:
            if variable == 32:
                return f"Output newline, the character value of {variable}."
            else:
                return f"Output '{chr(variable)}', the character value of {variable}."


    def get_image(self):
        pass

    def get_program(self):
        pass
