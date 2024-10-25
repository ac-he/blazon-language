from abc import ABC, abstractmethod


class Blazon(ABC):
    division = None
    shape = None
    tinctures = None

    base = None
    chief = None
    dexter = None
    escutcheon = None
    sinister = None
    dexter_chief = None
    sinister_chief = None
    dexter_base = None
    sinister_base = None
    field = None

    @abstractmethod
    def __init__(self, blazon_json):
        pass

    @abstractmethod
    def get_pseudocode(self):
        pass

    @abstractmethod
    def get_image(self):
        pass

    @abstractmethod
    def get_program(self):
        pass


