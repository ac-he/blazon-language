from blazon_language.language._evaluation import get_int_value


class BranchManager():
    def __init__(self, blazons):
        self.branches = {}
        self.functions = {}

        self.callstack = []

        # preprocess: find branch and function labels
        i = 0
        for blazon in blazons:
            if blazon.division == "per nothing":
                value = get_int_value(blazon.field)
                self.branches[value] = i
            elif blazon.division == "bend":
                value = get_int_value(blazon.field)
                self.functions[value] = i
            i += 1
        self.end = i

    def push_callstack(self, function, index):
        self.callstack.append({"f": function, "i": index})
        return self.functions.get(function)

    def pop_callstack(self, function):
        last = self.callstack.pop()
        if last.get("f") == function:
            return last.get("i") + 1
        else:
            raise Exception
