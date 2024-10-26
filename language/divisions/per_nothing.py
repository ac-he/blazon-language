from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value
from language.field import Field
from rendering.draw_division import make_division_image
from rendering.draw_dof import make_dof_image


class PerNothing(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "per nothing"
        self.shape = "heater"

        self.field = blazon_json.get("field")
        self.tinctures = [blazon_json.get("tincture").lower()]

        self.field = Field(self.field, self.tinctures[0], "per nothing", "field")

    def get_pseudocode(self):
        branch = get_int_value(self.field)
        return f"Begin Branch{branch}."

    def get_program(self):
        pass
