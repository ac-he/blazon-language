from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, get_comparison, do_comparison
from language.field import Field


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
        variable = get_int_value(self.dexter)
        value = get_int_value(self.sinister)
        branch = get_int_value(self.base)
        comparison = get_comparison(self.chief)
        return f"If Variable{variable} is {comparison} {value}, go to Branch{branch}."

    def get_program(self, vm, bm):
        operator = self.chief.field_tincture

        variable = get_int_value(self.dexter)
        value1 = vm.retrieve(variable)
        value2 = get_int_value(self.sinister)

        branch = get_int_value(self.base)

        comparison = do_comparison(operator, value1, value2)
        if comparison:
            return bm.branches.get(branch)
