import random
import re
from abc import ABC

from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language._evaluation import get_int_value, is_metal
from blazon_language.language.field import Field


class Fess(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "fess"
        self.shape = "heater"

        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.ordinary = blazon_json.get("ordinary")
        self.tinctures = blazon_json.get("tincture")

        if not self.ordinary:
            self.ordinary = {}

        self.chief = Field(self.chief, self.tinctures[0], self.division, "chief")
        self.base = Field(self.base, self.tinctures[1], self.division, "base")
        self.ordinary = Field(self.ordinary, self.tinctures[2], self.division, "ordinary")

    def get_pseudocode(self):
        variable = get_int_value(self.base)
        stack = get_int_value(self.chief)

        return f"Push Variable{variable} to Stack{stack}."

    def get_program(self, vm, bm):
        stack = get_int_value(self.chief)
        variable = get_int_value(self.base)
        value = vm.retrieve(variable)

        vm.push_stack(stack, value)
