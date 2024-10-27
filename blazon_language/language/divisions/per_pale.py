from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language._evaluation import get_int_value
from blazon_language.language.field import Field


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

    def get_program(self, vm, bm):
        value = get_int_value(self.sinister)
        variable = get_int_value(self.dexter)
        vm.store(variable, value)
