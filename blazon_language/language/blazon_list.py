from tatsu.util import asjson

from blazon_language.language._parser import BlazonParser
from blazon_language.language.divisions.per_bend import PerBend
from blazon_language.language.divisions.per_bend_sinister import PerBendSinister
from blazon_language.language.divisions.per_chevron import PerChevron
from blazon_language.language.divisions.per_cross import PerCross
from blazon_language.language.divisions.per_fess import PerFess
from blazon_language.language.divisions.per_nothing import PerNothing
from blazon_language.language.divisions.per_pale import PerPale
from blazon_language.language.divisions.per_pall import PerPall
from blazon_language.language.divisions.per_saltire import PerSaltire
from blazon_language.language.program_data.branch_manager import BranchManager
from blazon_language.language.program_data.variable_manager import VariableManager
from blazon_language.language.settings.settings import Settings
from blazon_language.rendering.draw_blazon_list import DrawBlazonList


class BlazonList:
    def __init__(
        self,
        blazon
    ):
        self.settings = Settings("default")

        # read blazon file
        file = open(blazon, 'r')
        blazon_as_string = file.read()

        # parse blazon
        parser = BlazonParser()
        ast = parser.parse(blazon_as_string, start='start')
        ast_json = asjson(ast)

        self.blazons = []
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

    def interpret(self):
        if self.settings.pseudocode_mode:
            self.interpret_as_pseudocode()
        if self.settings.image_mode:
            self.interpret_as_image()
        if self.settings.program_mode:
            self.interpret_as_program()

    # Interpret as pseudocode
    def interpret_as_pseudocode(self):
        for blazon in self.blazons:
            print(blazon.get_pseudocode())

            if self.settings.pseudocode.space_between:
                print()

    # Interpret as image
    def interpret_as_image(self):
        if self.settings.image.preserve_individual_images:
            images = []
            for blazon in self.blazons:
                images.append(blazon.get_image(self.settings.image.image_overlay))

        DrawBlazonList(self.blazons, self.settings.image)

    # Interpret as program
    def interpret_as_program(self):
        vm = VariableManager()
        bm = BranchManager(self.blazons)

        instruction = 0
        instructions = len(self.blazons)

        while instruction < instructions:
            blazon = self.blazons[instruction]

            if self.settings.program.debug:
                print(blazon.get_pseudocode())

            branch = blazon.get_program(vm, bm)

            if self.settings.program.debug:
                print("Variables:", vm.variables)
                print("Branches:", bm.branches)
                print()

            if branch:
                instruction = branch
            else:
                instruction += 1
