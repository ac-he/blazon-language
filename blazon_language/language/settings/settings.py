import json
from pathlib import Path

from blazon_language.language.settings.image_settings import ImageSettings
from blazon_language.language.settings.program_settings import ProgramSettings
from blazon_language.language.settings.pseudocode_settings import PseudocodeSettings


class Settings:
    def __init__(self, config_file):
        if config_file == "default":
            self.output_config = Path.joinpath(Path.cwd(), "blazon_language", 'presets', 'default_output_config.json')
        else:
            self.output_config = config_file
        file = open(self.output_config, 'r')
        self.output_config = json.load(file)

        self.pseudocode_mode = not not self.output_config.get("modes").get("pseudocode")
        self.image_mode = not not self.output_config.get("modes").get("images")
        self.program_mode = not not self.output_config.get("modes").get("program")

        if self.pseudocode_mode:
            self.pseudocode = PseudocodeSettings(self.output_config.get("modes").get("pseudocode"))
        if self.image_mode:
            self.image = ImageSettings(self.output_config.get("modes").get("images"))
        if self.program_mode:
            self.program = ProgramSettings(self.output_config.get("modes").get("program"))
