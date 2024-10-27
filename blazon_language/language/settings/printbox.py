class Printbox:
    def __init__(self, printbox_json):
        self.x = printbox_json.get("x")
        self.y = printbox_json.get("y")
        self.w = printbox_json.get("w")
        self.h = printbox_json.get("h")
        self.kerning = printbox_json.get("kerning")
        self.line_spacing = printbox_json.get("line-spacing")