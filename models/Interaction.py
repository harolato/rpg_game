from game import *
from constants import *
import random


class Interaction:
    """

    """
    game = None     # type: Game
    target = None   # type: GameObject;Actor

    def __init__(self, game, target):
        """

        :param game: Game
        :param target: GameObject
        """
        self.game = game        # type: Game
        self.target = target    # type: Actor

    def action(self):
        if self.game.player_object.state == STATE_PLAYER:
            if self.target.state == STATE_STATIC:
                pass
            elif self.target.state == STATE_HOSTILE:
                self.game.input.read("Press A to attack. F to flee")
                if self.game.input.get_value() == 'a':
                    self.attack()
                else:
                    self.flee()
            elif self.target.state in (STATE_FRIENDLY, STATE_NEUTRAL):
                self.talk()
        return self

    def talk(self):

        pass

    def attack(self):

        fighting = True
        while self.target.hp > 0 and self.game.player_object.hp > 0 and fighting:
            self.game.input.read("Press A to attack. F to flee")
            os.system('cls' if os.name == 'nt' else 'clear')
            damage = 0
            damage_received = 0
            if self.game.input.get_value() == 'a':
                damage = random.randint(self.game.player_object.dmg_min, self.game.player_object.dmg_max)
                damage_received = random.randint(self.target.dmg_min, self.target.dmg_max)
                self.target.hp -= damage
                self.game.player_object.hp -= damage_received
            else:
                fighting = False

            print("damage dealt: {}".format(damage))
            print('\n')
            print("damage Received: {}".format(damage_received))
            print('\n')
            print(self.target)
            print('\n')
            print(self.game.player_object)
            print('\n')

        if self.target.hp <= 0 < self.game.player_object.hp:
            self.game.player_object.add_xp(self.target.xp_reward)
            del self.game.objects[self.game.objects.index(self.target)]
            print("XP received: {}".format(self.target.xp_reward))

    def flee(self):
        pass

    def quest(self):
        pass
