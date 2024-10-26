from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, get_comparison
from language.field import Field
from rendering.draw_dof import make_dof_image


class PerSaltire(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "per saltire"
        self.shape = "heater"

        self.dexter = blazon_json.get("dexter")
        self.sinister = blazon_json.get("sinister")
        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        if not self.chief:
            self.chief = {}

        self.chief = Field(self.chief, self.tinctures[0], "per saltire", "chief")
        self.dexter = Field(self.dexter, self.tinctures[1], "per saltire", "dexter")
        self.sinister = Field(self.sinister, self.tinctures[2], "per saltire", "sinister")
        self.base = Field(self.base, self.tinctures[3], "per saltire", "base")

    def get_pseudocode(self):
        variable1 = get_int_value(self.dexter)
        variable2 = get_int_value(self.sinister)
        branch = get_int_value(self.base)
        comparison = get_comparison(self.chief)
        return f"If Variable{variable1} is {comparison} {variable2}, go to Branch{branch}."

    def get_program(self):
        pass
