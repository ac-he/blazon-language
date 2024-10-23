import json
from pathlib import Path

from tatsu.util import asjson

from language._parser import BlazonParser
from language.evaluate_charge import get_int_value
from language.pseudocode import *


class BlazonList:
    blazons = []
    output_config = None

    def __init__(
        self,
        blazon,
        output_config="default"
    ):
        file = open(blazon, 'r')
        blazon_as_string = file.read()

        if output_config == "default":
            self.output_config = Path.joinpath(Path.cwd(), 'presets', 'default_output_config.json')
        else:
            self.output_config = output_config

        file = open(self.output_config, 'r')
        self.output_config = json.load(file)

        parser = BlazonParser()
        ast = parser.parse(blazon_as_string, start='start')
        ast_json = asjson(ast)

        for blazon in ast_json.get("blazons"):
            self.blazons.add(Blazon())

    # Interpret as pseudocode
    def interpret_as_pseudocode(self):
        for blazon in self.blazons:
            blazon.get_pseudocode();

    # Interpret as image
    def interpret_as_image(self):
        for blazon in self.blazons:
            blazon.get_image();

    # Interpret as program
    def interpret_as_program(self):
        for blazon in self.blazons:
            blazon.get_program();


# add a new blazon.py in a new file later on
class Blazon(ABC):
    division = None
    shape = None
    
    base = None
    chief = None
    dexter = None
    escutcheon = None
    sinister = None
    dexter_chief = None
    sinister_chief = None
    dexter_base = None
    sinister_base = None
    no_division = None

    @abstractmethod
    def __init__(self, blazon_json):
        pass

    @abstractmethod
    def get_pseudocode():
        pass

    @abstractmethod
    def get_image():
        pass

    @abstractmethod
    def get_program():
        pass


#then make classes to inherit from this for all the different dofs


class Field:
    field_tincture = None
    charge = None
    charge_tincture = None
    charge_tincture = None

    def __init__(self, field_json):
        pass
        # set what can be set
        # if there is no field tincture throw an error
    
