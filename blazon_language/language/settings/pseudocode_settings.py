from pathlib import Path


class PseudocodeSettings:
    def __init__(self, config_json):
        self.space_between = config_json.get("space-between")
        self.output_destination = str(Path.cwd())
