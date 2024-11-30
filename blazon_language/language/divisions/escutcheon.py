from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language._evaluation import get_int_value, do_operation, get_operator
from blazon_language.language.field import Field


class Escutcheon(Blazon, ABC):

    def __init__(self, blazon_json):
        self.division = "escutcheon"
        self.shape = "heater"

        self.chief = blazon_json.get("chief")
        self.base = blazon_json.get("base")
        self.escutcheon = blazon_json.get("escutcheon")
        self.tinctures = blazon_json.get("tincture")

        self.chief = Field(self.chief, self.tinctures[0], self.division, "chief")
        self.base = Field(self.base, self.tinctures[1], self.division, "base")
        self.escutcheon = Field(self.escutcheon, self.tinctures[2], self.division, "escutcheon")

    def get_pseudocode(self):
        variable1 = get_int_value(self.chief)
        variable2 = get_int_value(self.base)
        operation = get_operator(self.escutcheon)
        match operation:
            case "Add":
                return f"Add Variable{variable2} to Variable{variable1}."
            case "Subtract":
                return f"Subtract Variable{variable2} from Variable{variable1}."
            case "Multiply":
                return f"Multiply Variable{variable1} by Variable{variable2}."
            case "Divide":
                return f"Divide Variable{variable1} by Variable{variable2}."
            case "Mod":
                return f"Mod Variable{variable1} by Variable{variable2}."
            case "Power":
                return f"Raise Variable{variable1} to the power of Variable{variable2}."
            case "Root":
                return f"Take the Variable{variable2}th root of Variable{variable1}."

    def get_program(self, vm, bm):
        variable1 = get_int_value(self.chief)
        variable2 = get_int_value(self.base)

        value1 = vm.retrieve(variable1)
        value2 = vm.retrieve(variable2)
        result = do_operation(self.escutcheon.field_tincture, value1, value2)

        vm.store(variable1, result)
