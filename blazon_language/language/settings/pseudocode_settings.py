from pathlib import Path


class PseudocodeSettings:
    def __init__(self, config_json):
        self.output_to_file = config_json.get("output-to-file")
        self.output_to_console = config_json.get("output-to-console")

        self.output_destination = str(Path.cwd())
