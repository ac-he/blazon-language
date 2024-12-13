from abc import ABC

from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language.evaluation import get_int_value
from blazon_language.language.field import Field


class Pale(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "pale"
        self.shape = "heater"

        self.dexter = blazon_json.get("dexter")
        self.sinister = blazon_json.get("sinister")
        self.ordinary = blazon_json.get("ordinary")
        self.tinctures = blazon_json.get("tincture")

        if not self.ordinary:
            self.ordinary = {}

        self.dexter = Field(self.dexter, self.tinctures[0], self.division, "dexter")
        self.sinister = Field(self.sinister, self.tinctures[1], self.division, "sinister")
        self.ordinary = Field(self.ordinary, self.tinctures[2], self.division, "ordinary")

    def get_pseudocode(self):
        value = get_int_value(self.sinister)
        stack = get_int_value(self.dexter)

        return f"Push {value} to Stack{stack}."

    def get_program(self, vm, bm):
        stack = get_int_value(self.dexter)
        value = get_int_value(self.sinister)

        vm.push_stack(stack, value)
