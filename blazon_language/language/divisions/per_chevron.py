import random
import re
from abc import ABC

from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language.evaluation import get_int_value, is_metal
from blazon_language.language.field import Field


class PerChevron(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "per chevron"
        self.shape = "heater"

        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.tinctures = blazon_json.get("tincture")

        if not self.base:
            self.base = {}

        self.chief = Field(self.chief, self.tinctures[0], "per chevron", "chief")
        self.base = Field(self.base, self.tinctures[1], "per chevron", "base")

    def get_pseudocode(self):
        variable = get_int_value(self.chief)
        if is_metal(self.base.field_tincture):
            return f"Read in a character and store its value to Variable{variable}."
        else:
            return f"Generate a random integer 0-9 and store it to Variable{variable}."

    def get_program(self, vm, bm):
        variable = get_int_value(self.chief)

        if is_metal(self.base.field_tincture):
            i = input()
            if re.match("^-?[0-9]+$", i):
                pass
            elif len(i) == 1:
                i = ord(i[0])
            else:
                # todo throw error
                print('input was not int or char')
                return
            vm.store(variable, i)

        else:
            vm.store(variable, random.randint(0, 9))
