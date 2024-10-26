from abc import ABC, abstractmethod

from rendering.draw_blazon import make_blazon_image


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

    def get_image(self, overlay=None):
        return make_blazon_image(self, overlay)

    @abstractmethod
    def get_program(self):
        pass


