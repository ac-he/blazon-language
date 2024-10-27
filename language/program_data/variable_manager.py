class VariableManager:
    def __init__(self):
        self.variables = {}

    def store(self, variable_label, variable_value):
        self.variables[variable_label] = int(variable_value)

    def retrieve(self, variable_label):
        return self.variables[variable_label]