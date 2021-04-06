import pygame
import random
import os
import sys

# global parameters
# -----------------

FPS = 60
fpsClock = 0
ScreenWidth = 390
ScreenHeight = 600

Window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
GroundY = ScreenHeight * 0.8
Game_sprites = {}
Game_sounds = {}
Player = None
Background = None
Pipe = None
Base = None
base_x = 0

# Physics objects
gravity = 0.25
bird_movement = 0

# -----------------


def draw_screen(bird_surface, bird_rect, Floor_flow):
    Window.blit(Game_sprites['background'], (0, 0))
    Window.blit(bird_surface, bird_rect)
    Window.blit(Game_sprites['Base'], (Floor_flow, 530))
    Window.blit(Game_sprites['Base'], (Floor_flow + 390, 530))
    pygame.display.update()
    fpsClock.tick(FPS)


def get_random_pipe():
    pass


def main_loop():
    score = 0

    jump_power = 2

    gravity_var = gravity
    bird_movement_local = bird_movement

    print(Game_sounds, Game_sprites)
    running = True
    bird_surface = Game_sprites['player']
    bird_rect = bird_surface.get_rect(center=(ScreenWidth // 2, ScreenHeight // 2))
    base_pos = 0

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_movement_local = 0
                bird_movement_local -= 10

        bird_movement_local += gravity_var
        bird_rect.centery += bird_movement_local
        draw_screen(bird_surface, bird_rect, base_pos)
        base_pos -= 1
        if base_pos <= -390:
            base_pos = 0


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

    Game_sprites['background'] = pygame.transform.scale(pygame.image.load(os.path.join('Img', 'background.png')),
                                                        (ScreenWidth, ScreenHeight)).convert()
    Game_sprites['player'] = pygame.image.load(os.path.join('Img', 'bird.png')).convert_alpha()
    Game_sprites['Pipe'] = pygame.image.load(os.path.join('Img', 'pipe.png')).convert_alpha()
    Game_sprites['Base'] = pygame.transform.scale(pygame.image.load(os.path.join('Img', 'base.png')),
                                                  (ScreenWidth, int(ScreenHeight / 8))).convert()

    main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
