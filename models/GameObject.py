import math
import copy

from constants import *


class GameObjectModel:
    prev_coords = None          # type: Coord
    coords = None               # type: Coord
    draw_coord = None           # type: tuple
    name = ''                   # type: str
    tile = ''                   # type: str
    state = STATE_STATIC        # type: int
    passable = True             # type: bool

    def __init__(self, coords, name, tile, passable=True):
        self.coords = coords
        self.name = name
        self.tile = tile
        self.passable = passable
        self.draw_coord = self.coords.mult_coords(TILE_SIZE[0], TILE_SIZE[1])

    def __cmp__(self, other):
        if self.name == other.name and \
                self.tile == other.tile and \
                self.coords.__eq__(other.coords):
            return True
        else:
            return False

    def move(self, input_handler):
        """

        :param input_handler: InputHandler
        :return: bool
        """

        self.prev_coords = copy.copy(self.coords)
        letter = input_handler.get_value()

        if letter == 'w':
            self.coords.add_y(-1)
        if letter == 'a':
            self.coords.add_x(-1)
        if letter == 's':
            self.coords.add_y(1)
        if letter == 'd':
            self.coords.add_x(1)
        if letter == 'q':
            input_handler.set_data(False)

    def undo_move(self):
        self.coords = copy.copy(self.prev_coords)
        del self.prev_coords

    def __str__(self):
        hud = "\n"

        health_bar = '['

        hp_percent = math.floor(((self.hp * 100) / self.hp_cap) / 10)
        for bar in range(hp_percent):
            health_bar += '#'
        for bar in range(10 - hp_percent):
            health_bar += '.'

        health_bar += ']'

        hud += 'Object:{} ([{}:{}])\nHP:{}/{} {}\ndamage:{} - {}'.format(
            self.name, self.coords.x, self.coords.y,
            self.hp, self.hp_cap, health_bar, self.dmg_min, self.dmg_max)
        return hud
