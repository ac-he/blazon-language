class ProgramSettings:
    def __init__(self, config_json):
        self.debug = config_json.get("debug")
        self.step_thru = config_json.get("step-thru")
