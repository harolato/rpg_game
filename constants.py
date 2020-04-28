# Constants
WIDTH = 30
HEIGHT = 20
BORDER = {
    'corner': '+',
    'side': '|',
    'top_even': '--',
    'top_odd': '\u001b[31m--\u001b[0m'
}
EMPTY_TILE = 'assets/tiles/grass00.png'
TREE_TILE = 'assets/objects/baum.png'
CHICKEN = 'assets/objects/ChickenWalking_08.png'
SHEEP = 'assets/objects/SheepWalking_08.png'

"""
FRIENDLY - Quest, talk, hint
HOSTILE - Fight or flee
NEUTRAL - Talk
STATIC - non-intractable environment object i.e. tree, rock etc. 
"""
STATE_FRIENDLY = 0
STATE_HOSTILE = 1
STATE_NEUTRAL = 2
STATE_STATIC = 3
STATE_PLAYER = 4
STATE_PASSAGE = 5

TILE_SIZE = (32, 32)
WINDOW_SIZE = (860, 640)

COORD_BOUNDS = (WINDOW_SIZE[0]/TILE_SIZE[0], WINDOW_SIZE[1]/TILE_SIZE[1])

try:
    import pydevd
    DEBUGGING = True
except ImportError:
    DEBUGGING = False

RATE = 0.3
