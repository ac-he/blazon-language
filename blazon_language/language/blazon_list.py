import os
from pathlib import Path

from tatsu.util import asjson

from blazon_language.language._parser import BlazonParser
from blazon_language.language.divisions.bend import Bend
from blazon_language.language.divisions.bend_sinister import BendSinister
from blazon_language.language.divisions.cross import Cross
from blazon_language.language.divisions.per_bend import PerBend
from blazon_language.language.divisions.per_bend_sinister import PerBendSinister
from blazon_language.language.divisions.per_chevron import PerChevron
from blazon_language.language.divisions.per_cross import PerCross
from blazon_language.language.divisions.per_fess import PerFess
from blazon_language.language.divisions.escutcheon import Escutcheon
from blazon_language.language.divisions.per_nothing import PerNothing
from blazon_language.language.divisions.per_pale import PerPale
from blazon_language.language.divisions.per_pall import PerPall
from blazon_language.language.divisions.per_saltire import PerSaltire
from blazon_language.language.divisions.saltire import Saltire
from blazon_language.language.program_data.branch_manager import BranchManager
from blazon_language.language.program_data.variable_manager import VariableManager
from blazon_language.language.settings.settings import Settings
from blazon_language.rendering._image_management import delete_all_images
from blazon_language.rendering.draw_blazon_list import DrawBlazonList


class BlazonList:
    def __init__(
        self,
        blazon,
        output_config
    ):
        self.settings = Settings(output_config)

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

            b = None
            match division:
                case "bend":
                    b = Bend(this_blazon)
                case "bend_sinister":
                    b = BendSinister(this_blazon)
                case "cross":
                    b = Cross(this_blazon)
                case "escutcheon":
                    b = Escutcheon(this_blazon)
                case "saltire":
                    b = Saltire(this_blazon)
                case "per_bend":
                    b = PerBend(this_blazon)
                case "per_bend_sinister":
                    b = PerBendSinister(this_blazon)
                case "per_chevron":
                    b = PerChevron(this_blazon)
                case "per_cross":
                    b = PerCross(this_blazon)
                case "per_fess":
                    b = PerFess(this_blazon)
                case "per_pale":
                    b = PerPale(this_blazon)
                case "per_pall":
                    b = PerPall(this_blazon)
                case "per_saltire":
                    b = PerSaltire(this_blazon)
                case "per_nothing":
                    b = PerNothing(this_blazon)

            b.settings = self.settings
            self.blazons.append(b)

    def interpret(self):
        if self.settings.pseudocode_mode:
            self.interpret_as_pseudocode()
        if self.settings.image_mode:
            self.interpret_as_image()
        if self.settings.program_mode:
            self.interpret_as_program()

    # Interpret as pseudocode
    def interpret_as_pseudocode(self):
        file = Path.joinpath(Path(self.settings.pseudocode.output_destination), f"blazon_as_pseudocode.txt")
        if self.settings.pseudocode.output_to_file:
            try:
                file = open(file, "x")
            except FileExistsError as ex:
                file = open(file, "w")

        for blazon in self.blazons:
            pc = blazon.get_pseudocode()

            if self.settings.pseudocode.output_to_file:
                file.write(pc)
                file.write("\n")

            if self.settings.pseudocode.output_to_console:
                print(pc)

        if self.settings.pseudocode.output_to_file:
            file.close()
            print(f"Output pseudocode to {self.settings.pseudocode.output_destination}")

    # Interpret as image
    def interpret_as_image(self):
        delete_all_images()
        if self.settings.image.preserve_individual_images:
            images = []
            i = 0
            for blazon in self.blazons:
                i += 1
                new_image = Path.joinpath(Path(self.settings.image.output_destination), f"blazon_as_image-{i}.png")
                b = blazon.get_image(self.settings.image.image_overlay)
                images.append(b)
                try:
                    os.remove(new_image)
                except FileNotFoundError:
                    pass
                os.rename(b, new_image)

            print(f"Output {i} individual blazon renders to {self.settings.image.output_destination}")

        dbl = DrawBlazonList(self.blazons, self.settings.image)
        print(f"Output {dbl.pages} page(s) of blazon renders to {self.settings.image.output_destination}")

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
                print()
                print("Variables:", vm.variables)
                print("Branches:", bm.branches)
                if self.settings.program.step_thru:
                    print("[hit enter to continue]", end="")
                    input()
                print()

            if branch:
                instruction = branch
            else:
                instruction += 1
