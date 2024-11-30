from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language._evaluation import get_int_value
from blazon_language.language.field import Field


class Saltire(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "saltire"
        self.shape = "heater"

        self.field = blazon_json.get("field")
        self.tinctures = blazon_json.get("tincture")

        self.field = Field(self.field, self.tinctures[0].lower(), "saltire", "field")
        self.ordinary = Field({}, self.tinctures[1], "saltire", "ordinary")

    def get_pseudocode(self):
        function = get_int_value(self.field)
        return f"Call Function{function}."

    def get_program(self, vm, bm):
        pass
        # TODO FM here
