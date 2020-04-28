from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from random import random as r
from kivy.vector import Vector
from constants import *
import math
from models.Actor import ActorModel
from models.GameObject import GameObjectModel
from models.coord import Coord


class Map(RelativeLayout):
    tiles = []

    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)

    def generate_tiles(self):
        x_num_tiles = math.ceil(WINDOW_SIZE[0]/TILE_SIZE[0])
        y_num_tiles = math.ceil(WINDOW_SIZE[1]/TILE_SIZE[1])

        for x in range(x_num_tiles):
            for y in range(y_num_tiles):
                self.tiles.append({
                    'tile': EMPTY_TILE,
                    'pos': (TILE_SIZE[0] * x, TILE_SIZE[1] * y)
                })

    def draw(self, *args):
        self.generate_tiles()

        self.canvas.clear()
        with self.canvas:
            for tile in self.tiles:
                Rectangle(
                    pos=tile['pos'],
                    size=TILE_SIZE,
                    source=tile['tile']
                )


class GameObject(Widget):
    entity = None

    def __init__(self, actor_obj, **kwargs):
        super(GameObject, self).__init__(**kwargs)
        self.entity = actor_obj

    def draw(self):
        self.size = TILE_SIZE
        self.pos = self.entity.draw_coord
        with self.canvas:
            Rectangle(
                pos=self.entity.draw_coord,
                source=self.entity.tile,
                # color=Color(255,0,0),
                size=TILE_SIZE
            )


class Actor(Widget):
    entity = None

    def __init__(self, actor_obj, **kwargs):
        super(Actor, self).__init__(**kwargs)
        self.entity = actor_obj

    def draw(self):
        self.size = TILE_SIZE
        self.pos = self.entity.draw_coord
        with self.canvas:
            Rectangle(
                pos=self.entity.draw_coord,
                source=self.entity.tile,
                # color=Color(255,0,0),
                size=TILE_SIZE
            )

    def on_touch_down(self, touch, after=False):
        if self.collide_point(*touch.pos):
            self.parent.toolbar.children[0].text = str(self.entity)
            return True
        self.parent.toolbar.children[0].text = ''
        return super(Actor, self).on_touch_down(touch)


class BongGame(Widget):
    player_object = None
    game_objects = []
    toolbar = None

    def __init__(self, **kwargs):
        super(BongGame, self).__init__(**kwargs)
        self.toolbar = RelativeLayout(pos=(100, 50))
        label = Label(text='test')
        self.toolbar.add_widget(label)
        self.add_widget(self.toolbar)

    def set_player(self, player):
        self.player_object = player

    def add_object(self, obj):
        self.add_widget(obj)
        obj.draw()
        self.game_objects.append(obj)


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class BongApp(App):
    def build(self):
        tiles_widget = Map(size=WINDOW_SIZE, pos=(0, 0))
        tiles_widget.draw()

        game = BongGame(size=WINDOW_SIZE)

        player = Actor(
            ActorModel(
                coords=Coord(9, 8),
                name="Super Chicken",
                tile=CHICKEN,
                hp=200,
                dmg_min=1,
                dmg_max=2,
                state=STATE_PLAYER
            )
        )

        enemy = Actor(
            ActorModel(
                coords=Coord(20, 15),
                name="Evil Sheep",
                tile=SHEEP,
                hp=200,
                dmg_min=1,
                dmg_max=2,
                state=STATE_HOSTILE
            )
        )

        tree = GameObject(
            GameObjectModel(Coord(11, 15), "Tree", TREE_TILE, False)
        )
        tree1 = GameObject(
            GameObjectModel(Coord(12, 15), "Tree", TREE_TILE, False)
        )
        tree2 = GameObject(
            GameObjectModel(Coord(11, 16), "Tree", TREE_TILE, False)
        )

        game.add_object(enemy)
        game.add_object(player)
        game.add_object(tree)
        game.add_object(tree1)
        game.add_object(tree2)

        game.set_player(player)

        # Clock.schedule_interval(game.update, 1.0 / 60.0)

        root = RootWidget()
        root.add_widget(tiles_widget)

        root.add_widget(game)

        return root


if __name__ == '__main__':
    BongApp().run()
