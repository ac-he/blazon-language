import json
from pathlib import Path

from language.settings.image_settings import ImageSettings
from language.settings.pseudocode_settings import PseudocodeSettings


class Settings:
    def __init__(self, config_file):
        if config_file == "default":
            self.output_config = Path.joinpath(Path.cwd(), 'presets', 'default_output_config.json')
        else:
            self.output_config = config_file
        file = open(self.output_config, 'r')
        self.output_config = json.load(file)

        self.pseudocode_mode = not not self.output_config.get("modes").get("pseudocode")
        self.image_mode = not not self.output_config.get("modes").get("images")
        self.program_mode = not not self.output_config.get("modes").get("program")

        self.pseudocode = PseudocodeSettings(self.output_config.get("modes").get("pseudocode"))
        self.image = ImageSettings(self.output_config.get("modes").get("images"))

        # read output file
