import json
from pathlib import Path

from tatsu.util import asjson

from language._parser import BlazonParser
from language.divisions.per_bend import PerBend
from language.divisions.per_bend_sinister import PerBendSinister
from language.divisions.per_chevron import PerChevron
from language.divisions.per_cross import PerCross
from language.divisions.per_fess import PerFess
from language.divisions.per_nothing import PerNothing
from language.divisions.per_pale import PerPale
from language.divisions.per_pall import PerPall
from language.divisions.per_saltire import PerSaltire


class BlazonList:
    blazons = []
    output_config = None

    def __init__(
        self,
        blazon,
        output_config="default"
    ):
        # read blazon file
        file = open(blazon, 'r')
        blazon_as_string = file.read()

        # read output file
        if output_config == "default":
            self.output_config = Path.joinpath(Path.cwd(), 'presets', 'default_output_config.json')
        else:
            self.output_config = output_config
        file = open(self.output_config, 'r')
        self.output_config = json.load(file)

        # parse blazon
        parser = BlazonParser()
        ast = parser.parse(blazon_as_string, start='start')
        ast_json = asjson(ast)

        for blazon in ast_json.get("blazons"):
            division = list(blazon[0].keys())[0]
            this_blazon = blazon[0][division]

            match division:
                case "per_bend":
                    self.blazons.append(PerBend(this_blazon))
                case "per_bend_sinister":
                    self.blazons.append(PerBendSinister(this_blazon))
                case "per_chevron":
                    self.blazons.append(PerChevron(this_blazon))
                case "per_cross":
                    self.blazons.append(PerCross(this_blazon))
                case "per_fess":
                    self.blazons.append(PerFess(this_blazon))
                case "per_pale":
                    self.blazons.append(PerPale(this_blazon))
                case "per_pall":
                    self.blazons.append(PerPall(this_blazon))
                case "per_saltire":
                    self.blazons.append(PerSaltire(this_blazon))
                case "per_nothing":
                    self.blazons.append(PerNothing(this_blazon))
                case _:
                    pass

    # Interpret as pseudocode
    def interpret_as_pseudocode(self):
        for blazon in self.blazons:
            print(blazon.get_pseudocode())

    # Interpret as image
    def interpret_as_image(self):
        for blazon in self.blazons:
            blazon.get_image()

    # Interpret as program
    def interpret_as_program(self):
        for blazon in self.blazons:
            blazon.get_program()
