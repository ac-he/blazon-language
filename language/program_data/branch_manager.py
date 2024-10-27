from language._evaluation import get_int_value


class BranchManager():
    def __init__(self, blazons):
        self.branches = {}

        i = 0
        for blazon in blazons:
            if blazon.division == "per nothing":
                value = get_int_value(blazon.field)
                self.branches[value] = i
            i += 1
