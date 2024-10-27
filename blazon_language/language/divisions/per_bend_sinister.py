from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language._evaluation import get_int_value, is_metal
from blazon_language.language.field import Field


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
        value = get_int_value(self.base)
        if is_metal(self.chief.field_tincture):
            return f"Output '{value}'."
        else:
            if value == 32:
                return f"Output newline, the character value of {value}."
            else:
                return f"Output '{chr(value)}', the character value of {value}."

    def get_program(self, vm, bm):
        value = get_int_value(self.base)

        if is_metal(self.chief.field_tincture):
            print(value, end="")
        else:
            print(chr(value), end="")
