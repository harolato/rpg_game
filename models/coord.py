from constants import *


class Coord:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __cmp__(self, other):
        if self.x == other.x and \
                self.y == other.y:
            return True
        else:
            return False

    def set_coords(self, x, y):
        """

        :param x: int
        :param y: int
        :return:
        """
        if x < 1:
            x = 1
        if y < 1:
            y = 1

        if x > COORD_BOUNDS[1]:
            x = COORD_BOUNDS[0]
        if y > COORD_BOUNDS[1]:
            y = COORD_BOUNDS[1]

        self.x = x
        self.y = y

    def add_x(self, val):
        self.set_coords(self.x + val, self.y)

    def add_y(self, val):
        self.set_coords(self.x, self.y + val)

    def mult_coords(self, val_x, val_y):
        return self.x * val_x, self.y * val_y

    def tuple(self):
        return self.x, self.y
