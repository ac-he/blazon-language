from abc import ABC

from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language.field import Field


class Cross(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "cross"
        self.shape = "heater"

        self.tinctures = blazon_json.get("tincture")

        self.field = Field({}, self.tinctures[0].lower(), "cross", "field")
        self.ordinary = Field({}, self.tinctures[1], "cross", "ordinary")

        self.field.enforce_rule_of_tincture(self.ordinary.field_tincture)

    def get_pseudocode(self):
        return "Halt the program."

    def get_program(self, vm, bm):
        return bm.end
