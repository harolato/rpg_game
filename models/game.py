import os

from models.Actor import Actor
from models.input_handler import InputHandler
from models.Interaction import Interaction
from models.GameObject import GameObject
from constants import *
from models.observer import subject


class Game:
    objects = []            # type: list[GameObject]
    map_layout = []         # type: list[str]
    is_running = True       # type: bool
    player_object = None    # type: Actor
    input = None            # type: InputHandler
    output = ""             # type: str

    def __init__(self):
        pass

    def detect_collision(self):
        for obj in self.objects:
            for m in self.objects:
                if not obj.__cmp__(m):
                    if obj.coords.__cmp__(m.coords):
                        subject.notify_observers('collision')
                        if not m.passable:
                            self.player_object.undo_move()
                        Interaction(self, m).action()

    def tick(self):
        """
        TikTok
        :return:
        """
        self.output = ""
        if DEBUGGING:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.is_running = False
        else:
            self.input.read()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player_object.move(self.input)

        self.detect_collision()

        for g_object in self.objects:
            if isinstance(g_object, Actor):
                if g_object.is_level_up():
                    self.output += "\n!!!LEVEL UP!!!\n"

        self.output += self.draw()

    def set_player_object(self, player_object):
        """

        :param player_object: GameObject
        :return: Game
        """
        player_object.state = STATE_PLAYER
        self.player_object = player_object
        return self

    def set_input(self, input_typ):
        self.input = input_typ

    def add_object(self, game_object):
        """

        :type game_object: GameObject
        :return: Game
        """
        self.objects.append(game_object)
        return self

    def draw(self):
        """

        :return: str
        """
        board = ''
        objects = self.generate()

        for y in range(len(objects)):
            objects[y] = [BORDER['side']] + objects[y] + [BORDER['side']]

        border = ''
        border += BORDER['corner']

        for x in range(WIDTH):
            if x % 2 == 0:
                border += BORDER['top_even']
            if x % 2 != 0:
                border += BORDER['top_odd']

        border += BORDER['corner']
        board_list = [border] + objects + [border]

        for tile_y in range(len(board_list)):
            for tile in board_list[tile_y]:
                board += str(tile[0].symbol) if isinstance(tile, list) else str(tile)
            board += '\n'

        return board + str(self.player_object)

    def generate(self):
        """

        :return: list[str]
        """

        self.is_running = self.input.get_data()

        map_layout = [[EMPTY_TILE for x in range(WIDTH)] for x in range(HEIGHT)]

        for obj in self.objects:
            if map_layout[obj.coords.y - 1][obj.coords.x - 1] is list:
                map_layout[obj.coords.y - 1][obj.coords.x - 1].append(obj)
            else:
                map_layout[obj.coords.y - 1][obj.coords.x - 1] = [obj]
        return map_layout

