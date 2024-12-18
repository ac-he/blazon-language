from pathlib import Path

from blazon_language.language.settings.printbox import Printbox


class ImageSettings:
    def __init__(self, config_json):
        self.output_destination = str(Path.cwd())

        self.width = config_json.get("w")
        self.height = config_json.get("h")

        self.background_path = config_json.get("background-path")
        self.background = config_json.get("background")

        self.crest_scale_width = config_json.get("crest-scale-width")

        self.printboxes = []
        pbs = config_json.get("printboxes")
        for pb in pbs:
            self.printboxes.append(Printbox(pb))

        self.randomize_shapes = config_json.get("randomize-shapes")
        self.shapes = config_json.get("shapes")

        self.page_overlay = config_json.get("page-overlay")
        self.image_overlay = config_json.get("image-overlay")

        self.image_outline_width = config_json.get("image-outline-width")
        self.image_outline_tincture = config_json.get("image-outline-tincture")

        self.preserve_individual_images = config_json.get("preserve-individual-images")
