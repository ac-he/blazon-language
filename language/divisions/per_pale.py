from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value
from language.field import Field


class PerPale(Blazon, ABC):
    def __init__(self, blazon_json):
        self.dexter = blazon_json.get("dexter")
        self.sinister = blazon_json.get("sinister")
        self.tinctures = blazon_json.get("tincture")

        self.dexter = Field(self.dexter, self.tinctures[0])
        self.sinister = Field(self.sinister, self.tinctures[1])

    def get_pseudocode(self):
        value = get_int_value(self.sinister)
        variable = get_int_value(self.dexter)
        return f"Save the value {value} to Variable{variable}."

    def get_image(self):
        pass

    def get_program(self):
        pass
