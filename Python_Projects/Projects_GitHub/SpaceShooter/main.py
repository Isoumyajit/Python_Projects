from spaceShooter import main
import pygame
import os

pygame.init()

# Colors
# --------------
color = (0, 0, 0)
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)
# --------------
background_sound = pygame.mixer.Sound(os.path.join('Sounds', 'videoplayback_4.mp3'))

width_main_menu, main_menu_height = 900, 500

main_screen = pygame.display.set_mode((width_main_menu, main_menu_height))
pygame.display.set_caption("Space Shooter Main Menu")
background = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (width_main_menu,
                                                                                             main_menu_height))

text_font = pygame.font.SysFont('Corbel', 35)

start_game_txt = text_font.render('Start Game', True, color)
Exit_txt = text_font.render('Exit', True, color)

# USER EVENTS
# -----------------
start_game_event = pygame.USEREVENT + 1
Exit_game_event = pygame.USEREVENT + 2


# -----------------


def draw_main_menu():
    main_screen.blit(background, (0, 0))
    pygame.draw.rect(main_screen, color_light, [width_main_menu / 2 - 100, main_menu_height / 2 - 100, 200,
                                                30])
    pygame.draw.rect(main_screen, color_light, [width_main_menu / 2 - 100, main_menu_height / 2, 200, 30])
    # print(start_game, Exit)
    main_screen.blit(start_game_txt, (width_main_menu / 2 - 100, main_menu_height / 2 - 100))
    main_screen.blit(Exit_txt, (width_main_menu / 2 - 30, main_menu_height / 2))
    pygame.display.update()


def main_loop():
    running = True
    background_sound.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                if width_main_menu / 2 - 100 <= mouse[0] <= width_main_menu / 2 - 100 + 200 and \
                        main_menu_height / 2 - 100 <= mouse[1] <= main_menu_height / 2 - 100 + 30:
                    main()

                if width_main_menu / 2 - 30 <= mouse[0] <= width_main_menu / 2 - 30 + 200 and \
                        main_menu_height / 2 <= mouse[1] <= main_menu_height / 2 + 30:
                    pygame.quit()
                    quit()

        draw_main_menu()


if __name__ == "__main__":
    main_loop()
