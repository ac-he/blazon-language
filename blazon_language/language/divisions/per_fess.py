from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language.evaluation import get_int_value
from blazon_language.language.field import Field


class PerFess(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "per fess"
        self.shape = "heater"

        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        self.chief = Field(self.chief, self.tinctures[0], self.division, "chief")
        self.base = Field(self.base, self.tinctures[1], self.division, "base")

    def get_pseudocode(self):
        variable1 = get_int_value(self.chief)
        variable2 = get_int_value(self.base)
        return f"Save the value from {variable2} to Variable{variable1}."

    def get_program(self, vm, bm):
        variable1 = get_int_value(self.chief)
        variable2 = get_int_value(self.base)

        vm.store(variable1, vm.retrieve(variable2))
