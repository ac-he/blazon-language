from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, get_comparison
from language.field import Field


class PerCross(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "per cross"
        self.shape = "heater"

        self.dexter_chief = blazon_json.get("dexter_chief")
        self.sinister_chief = blazon_json.get("sinister_chief")
        self.dexter_base = blazon_json.get("dexter_base")
        self.sinister_base = blazon_json.get("sinister_base")
        self.tinctures = blazon_json.get("tincture")

        if not self.dexter_chief:
            self.dexter_chief = {}

        self.dexter_chief = Field(self.dexter_chief, self.tinctures[0], "per cross",
                                  "dexter-chief")
        self.sinister_chief = Field(self.sinister_chief, self.tinctures[1], "per cross",
                                    "sinister-chief")
        self.dexter_base = Field(self.dexter_base, self.tinctures[2], "per cross",
                                 "dexter-base")
        self.sinister_base = Field(self.sinister_base, self.tinctures[3], "per cross",
                                   "sinister-base")

    def get_pseudocode(self):
        variable1 = get_int_value(self.sinister_chief)
        variable2 = get_int_value(self.dexter_base)
        branch = get_int_value(self.sinister_base)
        comparison = get_comparison(self.dexter_chief)
        return f"If Variable{variable1} is {comparison} Variable{variable2}, go to Branch{branch}."

    def get_program(self):
        pass
