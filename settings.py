import pygame

WINDOW_NAME = "Sharik Jargysh"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 30
DRAW_FPS = True

# sizes
BUTTONS_SIZES = (600, 60)
HAND_SIZE = 200
HAND_HITBOX_SIZE = (60, 80)
BALLOONS_SIZES = (53, 100)
BALLOON_SIZE_RANDOMIZE = (
    1,
    2,
)  # for each new balloon, it will multiply the size with an random value beteewn X and Y
BEE_SIZES = (50, 50)
BEE_SIZE_RANDOMIZE = (1.2, 1.5)

# drawing
DRAW_HITBOX = False  # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.08  # the frame of the insects will change every X sec

# difficulty
GAME_DURATION = 60  # the game will last X sec
BALLOONS_SPAWN_TIME = 1
BALLOONS_MOVE_SPEED = {"min": 5, "max": 15}
BEE_PENALITY = 10  # will remove X of the score of the player (if he kills a bee)

# colors
COLORS = {
    "title": (38, 61, 93),
    "score": (38, 61, 93),
    "timer": (38, 61, 93),
    "buttons": {
        "default": (56, 67, 209),
        "second": (87, 99, 255),
        "text": (255, 255, 255),
        "shadow": (46, 54, 163),
    },
    "toggle": {
        "active": (87, 99, 255),
        "inactive": (128, 128, 128),
        "background": (200, 200, 200),
    },
}  # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16  # value between 0 and 1
SOUNDS_VOLUME = 1
MUSIC_ENABLED = True  # Default to music on

# fonts
pygame.font.init()
FONTS = {}
FONTS["small"] = pygame.font.Font(None, 48)
FONTS["medium"] = pygame.font.Font(None, 72)
FONTS["big"] = pygame.font.Font(None, 96)

# Add at the top with other window settings
FULLSCREEN_MODE = False  # Default to windowed mode
