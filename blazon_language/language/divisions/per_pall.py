from abc import ABC
from blazon_language.language.divisions.blazon import Blazon
from blazon_language.language._evaluation import get_int_value, do_operation, get_operator
from blazon_language.language.field import Field


class PerPall(Blazon, ABC):
    def __init__(self, blazon_json):
        self.division = "per pall"
        self.shape = "heater"

        self.dexter = blazon_json.get("dexter")
        self.sinister = blazon_json.get("sinister")
        self.chief = blazon_json.get("chief")
        self.tinctures = blazon_json.get("tincture")

        if not self.chief:
            self.chief = {}

        self.chief = Field(self.chief, self.tinctures[0], "per pall", "chief")
        self.dexter = Field(self.dexter, self.tinctures[1], "per pall", "dexter")
        self.sinister = Field(self.sinister, self.tinctures[2], "per pall", "sinister")

    def get_pseudocode(self):
        value = get_int_value(self.sinister)
        variable = get_int_value(self.dexter)
        operation = get_operator(self.chief)
        match operation:
            case "Add":
                return f"Add {value} to Variable{variable}."
            case "Subtract":
                return f"Subtract {value} from Variable{variable}."
            case "Multiply":
                return f"Multiply Variable{variable} by {value}."
            case "Divide":
                return f"Divide Variable{variable} by {value}."
            case "Mod":
                return f"Mod Variable{variable} by {value}."
            case "Power":
                return f"Raise Variable{variable} to the power of {value}."
            case "Root":
                return f"Take the {value}th root of Variable{variable}."

    def get_program(self, vm, bm):
        value = get_int_value(self.sinister)
        variable = get_int_value(self.dexter)

        var_value = vm.retrieve(variable)
        result = do_operation(self.chief.field_tincture, var_value, value)

        vm.store(variable, result)
