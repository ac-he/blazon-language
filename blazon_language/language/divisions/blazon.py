from abc import ABC, abstractmethod

from blazon_language.rendering.draw_blazon import make_blazon_image


class Blazon(ABC):
    @abstractmethod
    def __init__(self, blazon_json):
        self.division = None
        self.shape = None
        self.tinctures = None

        self.base = None
        self.chief = None
        self.dexter = None
        self.escutcheon = None
        self.sinister = None
        self.dexter_chief = None
        self.sinister_chief = None
        self.dexter_base = None
        self.sinister_base = None
        self.field = None

    @abstractmethod
    def get_pseudocode(self):
        pass

    def get_image(self, overlay=None):
        return make_blazon_image(self, overlay)

    @abstractmethod
    def get_program(self, vm, bm):
        pass


