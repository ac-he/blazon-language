from abc import ABC

from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language.evaluation import get_int_value, is_metal
from blazon_language.language.field import Field


class Chevron(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "chevron"
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
        variable = get_int_value(self.chief)
        stack = get_int_value(self.base)
        operation = "Peek"
        if is_metal(self.base.field_tincture):
            operation = "Pop"

        return f"{operation} from Stack{stack} and store it to Variable{variable}."

    def get_program(self, vm, bm):
        variable = get_int_value(self.chief)
        stack = get_int_value(self.base)

        if is_metal(self.ordinary.field_tincture):
            value = vm.pop_stack(stack)
        else:
            value = vm.peek_stack(stack)

        vm.store(variable, value)
