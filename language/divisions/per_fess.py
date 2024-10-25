from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value, get_operator_string
from language.field import Field


class PerFess(Blazon, ABC):

    def __init__(self, blazon_json):
        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        self.chief = Field(self.chief, self.tinctures[0])
        self.base = Field(self.base, self.tinctures[1])

        if len(self.tinctures) == 3:
            self.escutcheon = blazon_json.get("escutcheon")
            if not self.escutcheon:
                self.escutcheon = {}
            self.escutcheon = Field(self.escutcheon, self.tinctures[2])

    def get_pseudocode(self):
        if self.escutcheon:
            variable1 = get_int_value(self.chief)
            variable2 = get_int_value(self.base)
            operation, preposition = get_operator_string(self.escutcheon)
            if operation == "root":
                return f"Take the Variable{variable2}th root of Variable{variable1}."
            else:
                return f"{operation} Variable{variable1} {preposition} Variable{variable2}."
        else:
            variable1 = get_int_value(self.chief)
            variable2 = get_int_value(self.base)
            return f"Save the value from {variable2} to Variable{variable1}."

    def get_image(self):
        pass

    def get_program(self):
        pass
