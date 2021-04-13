from flappy_bird import main_game
import pygame
import os

if __name__ == "__main__":
    pygame.init()
    background_sound = pygame.mixer.Sound(os.path.join('Sounds', 'videoplayback_4.mp3'))
    game_runner_obj = main_game()
    background_sound.play(loops=-1)
    game_runner_obj.start_game()
