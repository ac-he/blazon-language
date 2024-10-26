from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value
from language.field import Field
from rendering.draw_dof import make_dof_image


class PerPale(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "per pale"
        self.shape = "heater"

        self.dexter = blazon_json.get("dexter")
        self.sinister = blazon_json.get("sinister")
        self.tinctures = blazon_json.get("tincture")

        self.dexter = Field(self.dexter, self.tinctures[0], "per pale", "dexter")
        self.sinister = Field(self.sinister, self.tinctures[1], "per pale", "sinister")

    def get_pseudocode(self):
        value = get_int_value(self.sinister)
        variable = get_int_value(self.dexter)
        return f"Save the value {value} to Variable{variable}."

    def get_program(self):
        pass
