from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, get_operator_string
from language.field import Field


class PerPall(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "per pall"
        self.shape = "heater"

        self.dexter = blazon_json.get("dexter")
        self.sinister = blazon_json.get("sinister")
        self.chief = blazon_json.get("chief")
        self.tinctures = blazon_json.get("tincture")

        if not self.chief:
            self.chief = {}

        self.chief = Field(self.chief, self.tinctures[0], "per pall", "chief")
        self.dexter = Field(self.dexter, self.tinctures[1], "per pall", "dexter")
        self.sinister = Field(self.sinister, self.tinctures[2], "per pall", "sinister")

    def get_pseudocode(self):
        value = get_int_value(self.sinister)
        variable = get_int_value(self.dexter)
        operation, preposition = get_operator_string(self.chief)
        if operation == "root":
            return f"Take the {value}th root of Variable{variable}."
        else:
            return f"{operation} the value {value} {preposition} Variable{variable}."

    def get_program(self):
        pass
