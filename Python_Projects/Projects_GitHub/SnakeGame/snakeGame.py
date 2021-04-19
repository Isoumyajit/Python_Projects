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

        self.__screen_update = pygame.USEREVENT
        pygame.time.set_timer(self.__screen_update, 150)

    def main_game(self):
        running = True
        fruit_object = fruit()
        snake_obj = snake()
        game_runner = game_logic(snake_obj, fruit_object)

        while running:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == self.__screen_update:
                    snake_obj.move_snake()
                    game_runner.check_collision()
                    game_runner.hit()

                if events.type == pygame.KEYDOWN and events.key == pygame.K_UP:
                    snake_obj.direction = Vector2(0, -1)

                elif events.type == pygame.KEYDOWN and events.key == pygame.K_DOWN:
                    snake_obj.direction = Vector2(0, 1)

                elif events.type == pygame.KEYDOWN and events.key == pygame.K_LEFT:
                    snake_obj.direction = Vector2(-1, 0)

                elif events.type == pygame.KEYDOWN and events.key == pygame.K_RIGHT:
                    snake_obj.direction = Vector2(1, 0)

            self.window.fill((170, 220, 90))
            fruit_object.draw_fruit()
            snake_obj.draw_snake()
            pygame.display.update()
            self.__fps_checker.tick(self.__FPS)


class fruit:
    def __init__(self):
        self.x = random.randint(0, main_game.cell_number - 1)
        self.y = random.randint(0, main_game.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * main_game.cell_size), int(self.pos.y * main_game.cell_size),
                                 main_game.cell_size, main_game.cell_size)
        pygame.draw.rect(main_game.window, (126, 190, 200), fruit_rect)

    def randomize(self):
        self.__init__()


class snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(main_game.cell_size * block.x)
            y_pos = int(main_game.cell_size * block.y)
            block_rect = pygame.Rect(x_pos, y_pos, main_game.cell_size, main_game.cell_size)
            pygame.draw.rect(main_game.window, (180, 111, 222), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class game_logic:
    def __init__(self, snake_obj, fruit_obj):
        self.snake = snake_obj
        self.fruit = fruit_obj

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def hit(self):
        if not 0 <= self.snake.body[0].x < main_game.cell_number or \
                not 0 <= self.snake.body[0].y < main_game.cell_number:
            pygame.quit()
            sys.exit()
        else:
            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    pygame.quit()
                    sys.exit()
