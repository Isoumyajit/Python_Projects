import pygame
import time
import random
import math
import sys
from pygame.math import Vector2

# -------------------------


class main_game:
    cell_size = None
    cell_number = None
    window = None

    def __init__(self):
        pygame.init()
        main_game.cell_size = 32
        main_game.cell_number = 20
        main_game.window = pygame.display.set_mode((main_game.cell_size * main_game.cell_number,
                                               main_game.cell_size * main_game.cell_number))
        self.__FPS = 60
        self.__fps_checker = pygame.time.Clock()

        self.__sprites = {}
        self.__sounds = {}

    def main_game(self):
        running = True
        fruit_object = fruit()

        while running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            fruit_object.draw_fruit()
            pygame.display.update()
            self.__fps_checker.tick(self.__FPS)

    pass


class fruit:
    def __init__(self):
        self.__x = random.randint(0, main_game.cell_number - 1)
        self.__y = random.randint(0, main_game.cell_number - 1)
        self.pos = Vector2(self.__x, self.__y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * main_game.cell_size), int(self.pos.y*main_game.cell_size),
                                 main_game.cell_size, main_game.cell_size)
        pygame.draw.rect(main_game.window, (126, 166, 110), fruit_rect)


class snake:
    def __init__(self):
        pass

    def draw_snake(self):
        pass
