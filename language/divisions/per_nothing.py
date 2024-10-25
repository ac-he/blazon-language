from abc import ABC
from language.divisions.blazon import Blazon
from language._evaluation import get_int_value
from language.field import Field
from rendering.charger import make_division_image


class PerNothing(Blazon, ABC):
    def __init__(self, blazon_json):
        self.field = blazon_json.get("field")
        self.tinctures = [blazon_json.get("tincture").lower()]

        self.field = Field(self.field, self.tinctures[0], "per nothing", "field")

    def get_pseudocode(self):
        branch = get_int_value(self.field)
        return f"Begin Branch{branch}."

    def get_image(self, shape):
        make_division_image(self.field, shape)

    def get_program(self):
        pass
