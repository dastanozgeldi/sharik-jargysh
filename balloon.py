import random
import time

import pygame

import image
from settings import *


class Balloon:
    def __init__(self, window_size):
        self.window_size = window_size
        # size
        random_size_value = random.uniform(
            BALLOON_SIZE_RANDOMIZE[0], BALLOON_SIZE_RANDOMIZE[1]
        )
        size = (
            int(BALLOONS_SIZES[0] * random_size_value),
            int(BALLOONS_SIZES[1] * random_size_value),
        )
        # moving
        moving_direction, start_pos = self.define_spawn_pos(size)
        # sprite
        self.rect = pygame.Rect(
            start_pos[0], start_pos[1], size[0] // 1.4, size[1] // 1.4
        )
        self.images = [
            image.load(
                "assets/balloon/balloon.png",
                size=size,
                flip=moving_direction == "right",
            )
        ]
        self.current_frame = 0
        self.animation_timer = 0

    def define_spawn_pos(
        self, size
    ):  # define the start pos and moving vel of the balloon
        vel = random.uniform(BALLOONS_MOVE_SPEED["min"], BALLOONS_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (
                -size[0],
                random.randint(size[1], self.window_size[1] - size[1]),
            )
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (
                self.window_size[0] + size[0],
                random.randint(size[1], self.window_size[1] - size[1]),
            )
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (
                random.randint(size[0], self.window_size[0] - size[0]),
                self.window_size[1] + size[1],
            )
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (
                random.randint(size[0], self.window_size[0] - size[0]),
                -size[1],
            )
            self.vel = [0, vel]
        return moving_direction, start_pos

    def move(self):
        self.rect.move_ip(self.vel)

    def animate(self):  # change the frame of the insect when needed
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images) - 1:
                self.current_frame = 0

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        self.animate()
        image.draw(
            surface,
            self.images[self.current_frame],
            self.rect.center,
            pos_mode="center",
        )
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def kill(self, balloons):  # remove the balloon from the list
        balloons.remove(self)
        return 1
