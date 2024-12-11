class VariableManager:
    def __init__(self):
        self.variables = {}
        self.stacks = {}

    def store(self, variable_label, variable_value):
        self.variables[variable_label] = int(variable_value)

    def retrieve(self, variable_label):
        return self.variables[variable_label]

    def push_stack(self, stack_label, stack_value):
        if not self.stacks.get(stack_label):
            self.stacks[stack_label] = [stack_value]
        else:
            self.stacks[stack_label].append(stack_value)

    def pop_stack(self, stack_label):
        if len(self.stacks[stack_label]) == 0:
            return -1
        else:
            return self.stacks[stack_label].pop()

    def peek_stack(self, stack_label):
        s_len = len(self.stacks[stack_label])
        if s_len == 0:
            return -1
        else:
            return self.stacks[stack_label][s_len - 1]

