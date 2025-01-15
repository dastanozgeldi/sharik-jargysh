import os
import sys

import pygame

from game import Game
from menu import Menu
from settings import *


# Setup pygame/window --------------------------------------------- #
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (100, 32)
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

main_clock = pygame.time.Clock()


fps_font = pygame.font.SysFont("coopbl", 22)


pygame.mixer.music.load("assets/sounds/Komiku_-_12_-_Bicycle.mp3")
pygame.mixer.music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1)

state = "menu"


game = Game(SCREEN, None)
menu = Menu(SCREEN, game)
game.menu = menu


def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if state == "menu":
            menu.handle_event(event)


def update():
    global state
    if state == "menu":
        if menu.update() == "game":
            game.reset()
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    main_clock.tick(FPS)


while True:
    user_events()
    update()
    
    # Clear previous FPS display by drawing background at that spot
    if DRAW_FPS:
        fps_label = fps_font.render(
            f"FPS: {int(main_clock.get_fps())}", 1, (255, 200, 20)
        )
        SCREEN.blit(fps_label, (5, 70))
    
    # Update the display after drawing everything
    pygame.display.flip()
