import json
from pathlib import Path

from tatsu.util import asjson

from language._parser import BlazonParser
from language.evaluate_charge import get_int_value
from language.pseudocode import *


class Blazon:
    blazon = None
    output_config = None
    output_config_as_json = None
    blazon_as_string = None

    def __init__(
        self,
        blazon,
        output_config="default"
    ):
        self.blazon = blazon
        file = open(self.blazon, 'r')
        self.blazon_as_string = file.read()

        if output_config == "default":
            self.output_config = Path.joinpath(Path.cwd(), 'presets', 'default_output_config.json')
        else:
            self.output_config = output_config

        file = open(self.output_config, 'r')
        self.output_config_as_json = json.load(file)

    def parse_file(self):
        parser = BlazonParser()
        ast = parser.parse(self.blazon_as_string, start='start')
        ast_json = asjson(ast)

        for blazon in ast_json.get("blazons"):
            division = list(blazon[0].keys())[0]
            this_blazon = blazon[0][division]

            match division:
                case "per_bend": self.handle_per_bend(this_blazon)
                case "per_bend_sinister": self.handle_per_bend_sinister(this_blazon)
                case "per_chevron": self.handle_per_chevron(this_blazon)
                case "per_cross": self.handle_per_cross(this_blazon)
                case "per_fess": self.handle_per_fess_and_per_fess_escutcheon(this_blazon)
                case "per_pale": self.handle_per_pale(this_blazon)
                case "per_pall": self.handle_per_pall(this_blazon)
                case "per_saltire": self.handle_per_saltire(this_blazon)
                case "per_nothing": self.handle_per_nothing(this_blazon)
                case _: pass

    def handle_per_bend(self, division_json):
        if "images" in self.output_config_as_json["modes"]:
            pass

        if "pseudocode" in self.output_config_as_json["modes"]:
            variable = get_int_value(division_json["base"]["charge"], division_json["base"].get("quantity"))
            output_flag = division_json["tincture"][0]
            handle_per_bend(variable, output_flag)

    def handle_per_bend_sinister(self, division_json):
        pass

    def handle_per_chevron(self, division_json):
        pass

    def handle_per_cross(self, division_json):
        pass

    def handle_per_fess_and_per_fess_escutcheon(self, division_json):
        pass

    def handle_per_pale(self, division_json):
        pass

    def handle_per_pall(self, division_json):
        pass

    def handle_per_saltire(self, division_json):
        pass

    def handle_per_nothing(self, division_json):
        pass
