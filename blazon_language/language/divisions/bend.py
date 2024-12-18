from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language.evaluation import get_int_value
from blazon_language.language.field import Field


class Bend(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "bend"
        self.shape = "heater"

        self.field = blazon_json.get("field")
        self.tinctures = blazon_json.get("tincture")

        self.field = Field(self.field, self.tinctures[0].lower(), self.division, "field")
        self.ordinary = Field({}, self.tinctures[1], self.division, "ordinary")

        self.field.enforce_rule_of_tincture(self.ordinary.field_tincture)

    def get_pseudocode(self):
        function = get_int_value(self.field)
        return f"Begin Function{function}."

    def get_program(self, vm, bm):
        pass
