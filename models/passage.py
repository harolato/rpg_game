import math

from constants import *
from models.GameObject import GameObject


class Passage(GameObject):

    map_name = None
    state = STATE_PASSAGE

    def __init__(self, coords, name, symbol, map_name):
        super().__init__(coords, name, symbol)
        self.map_name = map_name

    def __str__(self):
        return super().__str__()
