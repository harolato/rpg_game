import math

from constants import *
from models.GameObject import GameObjectModel


class ActorModel(GameObjectModel):

    base_hp = 100
    base_stamina = 20
    base_dmg_min = 1
    base_dmg_max = 2

    hp_cap = 0
    stamina_cap = 0

    hp = 0
    stamina = 0
    dmg_min = 0
    dmg_max = 0

    xp = 0
    next_xp = 100
    level = 1
    xp_reward = 0
    xp_reward_multiplier = 1

    state = STATE_NEUTRAL

    def __init__(self, coords, name, tile, hp, dmg_min, dmg_max, state=STATE_NEUTRAL):
        super(ActorModel, self).__init__(coords, name, tile)
        self.base_hp = hp
        self.base_dmg_max = dmg_max
        self.base_dmg_min = dmg_min
        self.state = state
        self.set_level(self.level)

    def set_level(self, level):
        self.level = level
        self.hp_cap += math.ceil(self.base_hp + (RATE * self.level))
        self.stamina_cap += math.ceil(self.base_stamina + (RATE * self.level))
        self.hp = self.hp_cap
        self.stamina = self.stamina_cap
        self.dmg_min += math.ceil(self.base_dmg_min + (RATE * self.level))
        self.dmg_max += math.ceil(self.base_dmg_max + (RATE * self.level))
        self.next_xp += math.ceil(self.next_xp + (RATE * self.xp))
        self.xp_reward = math.ceil(self.xp + (self.level * RATE * self.xp_reward_multiplier))

    def is_level_up(self):
        if self.xp >= self.next_xp:
            self.level_up()
            return True
        return False

    def level_up(self):
        self.set_level(self.level+1)

    def add_xp(self, xp):
        self.xp += xp

    def __str__(self):
        hud = "\n"

        health_bar = '['

        hp_percent = math.floor(((self.hp * 100) / self.hp_cap) / 10)
        for bar in range(hp_percent):
            health_bar += '#'
        for bar in range(10 - hp_percent):
            health_bar += '.'

        health_bar += ']'

        hud += 'Player:{} ([{}:{}])\nHP:{}/{}\ndamage:{} - {}\n' \
               '{}\n' \
               'Level: {}, XP: {}, next Level XP: {}\n' \
               '' \
            .format(
            self.name, self.coords.x, self.coords.y,
            self.hp, self.hp_cap, self.dmg_min, self.dmg_max,
            health_bar,
            self.level, self.xp, self.next_xp
        )
        return hud
