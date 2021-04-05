import pygame
import math
import random
import numpy as np
import os
import sys

# global parameters
# -----------------

FPS = 30
fpsClock = 0
ScreenWidth = 289
ScreenHeight = 511

Window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
GroundY = ScreenHeight * 0.8
Game_sprites = {}
Game_sounds = {}
Player = None
Background = None
Pipe = None
Base = None
base_x = 0


# -----------------


def draw_screen(player_x, player_y):
    Window.blit(Game_sprites['background'], (0, 0))
    Window.blit(Game_sprites['player'], (player_x, player_y))
    Window.blit(Game_sprites['Base'], (base_x, GroundY))
    pygame.display.update()
    fpsClock.tick(FPS)


def get_random_pipe():
    """
    :doc: Generate pipes of random height
    """
    pipe_height = Game_sprites['Pipe'].get_height()
    offset = ScreenHeight // 3
    y2 = offset * random.randrange(0, int(ScreenHeight - Game_sprites['Base'].get_height() - 1.2 * offset))
    pipe_x = ScreenWidth + 10
    y1 = pipe_height - y2 + offset
    pipe = [
        {'x': pipe_x, 'y': -y1},  # upper
        {'x': pipe_x, 'y': y2}  # lower
    ]
    return pipe


def isCollide(player_x, player_y, upper_pipes, lower_pipes):
    return True
    pass


def main_loop():
    score = 0
    print(Game_sounds, Game_sprites)
    running = True
    player_x = int(ScreenWidth / 5)
    player_y = int(ScreenHeight - Game_sprites['player'].get_height()) / 2
    newPipe1 = get_random_pipe()
    newPipe2 = get_random_pipe()

    upperPipes = [
        {'x': ScreenWidth + 200, 'y': newPipe1[0]['y']},
        {'x': ScreenWidth + 200 + (ScreenWidth // 2), 'y': newPipe2[1]['y']}
    ]
    lowerPipes = [
        {'x': ScreenWidth + 200, 'y': newPipe1[0]['y']},
        {'x': ScreenWidth + 200 + (ScreenWidth // 2), 'y': newPipe2[1]['y']}
    ]

    player_acc_y = 1
    player_velocity_y = -9
    player_max_velocity = 10
    player_min_velocity = -8

    player_flapped = False
    player_flap_velocity = -8

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if player_y > 0:
                    player_velocity_y = player_flap_velocity
                    player_flapped = True
                    Game_sounds['wing'].play()

            crash_test = isCollide(player_x, player_y, upperPipes, lowerPipes)
            if crash_test:
                return

            player_mid_position = player_x + Game_sprites['player'].get_width() // 2
            for pipe in upperPipes:
                pipe_mid = pipe['x'] + Game_sprites['pipe'][0].get_width()//2
                if pipe_mid <= pipe_mid < pipe_mid + 4:
                    score += 1
                    print(f"Your score is {score}")
                    Game_sounds['point'].play()

        draw_screen(player_x, player_y + player_velocity_y)


if __name__ == '__main__':
    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')
    Game_sprites['numbers'] = (
        pygame.image.load(os.path.join('Img', '0.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '1.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '2.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '3.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '4.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '5.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '7.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '8.png')).convert_alpha(),
        pygame.image.load(os.path.join('Img', '9.png')).convert_alpha()
    )
    # Game_sprites['message'] = pygame.image.load(os.path.join('Img', 'message.png')).convert_alpha()
    # Game_Sounds
    Game_sounds['die'] = pygame.mixer.Sound(os.path.join('Sounds', 'die.wav'))
    Game_sounds['hit'] = pygame.mixer.Sound(os.path.join('Sounds', 'hit.wav'))
    Game_sounds['point'] = pygame.mixer.Sound(os.path.join('Sounds', 'point.wav'))
    Game_sounds['swoosh'] = pygame.mixer.Sound(os.path.join('Sounds', 'swoosh.wav'))
    Game_sounds['wing'] = pygame.mixer.Sound(os.path.join('Sounds', 'wing.wav'))

    Game_sprites['background'] = pygame.image.load(os.path.join('Img', 'background.png')).convert()
    Game_sprites['player'] = pygame.image.load(os.path.join('Img', 'bird.png')).convert_alpha()
    Game_sprites['Pipe'] = pygame.image.load(os.path.join('Img', 'pipe.png')).convert_alpha()
    Game_sprites['Base'] = pygame.image.load(os.path.join('Img', 'base.png')).convert_alpha()

    main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
