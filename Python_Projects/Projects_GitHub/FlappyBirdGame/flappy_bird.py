import pygame
import random
import os
import sys


def rotate_bird(bird_surface, movement):
    new_bird = pygame.transform.rotozoom(bird_surface, -movement * 3, 1)
    return new_bird


def move_pipes(all_pipes, base_pos):
    for pipe in all_pipes:
        pipe.centerx -= base_pos
    return all_pipes


class main_game:
    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.__FPS = 60
        self.fpsClock = 0
        self.__ScreenWidth = 400
        self.__ScreenHeight = 600

        self.__Window = pygame.display.set_mode((self.__ScreenWidth, self.__ScreenHeight))
        self.__GroundY = self.__ScreenHeight * 0.8
        self.__Game_sprites = {}
        self.__Game_sounds = {}
        self.__Player = None
        self.__Background = None
        self.__Pipe = None
        self.__Base = None
        self.__base_x = 0

        # Physics objects
        self.__gravity = 0.25
        self.__bird_movement = 0
        self.__flag = True

        self.__pipe_distance = 900

        # score_list
        self.__scores = [0]
        self.__game_font = pygame.font.SysFont('Ariel', 30)

        #     Initialization
        self.fpsClock = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird Game')
        self.__Game_sprites['numbers'] = (
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
        self.__Game_sounds['die'] = pygame.mixer.Sound(os.path.join('Sounds', 'die.wav'))
        self.__Game_sounds['hit'] = pygame.mixer.Sound(os.path.join('Sounds', 'hit.wav'))
        self.__Game_sounds['point'] = pygame.mixer.Sound(os.path.join('Sounds', 'point.wav'))
        self.__Game_sounds['swoosh'] = pygame.mixer.Sound(os.path.join('Sounds', 'swoosh.wav'))
        self.__Game_sounds['wing'] = pygame.mixer.Sound(os.path.join('Sounds', 'wing.wav'))

        self.__Game_sprites['screen'] = pygame.transform.scale(pygame.image.load(os.path.join('Img', 'message.png')),
                                                               (250, 300)). \
            convert_alpha()
        self.__Game_sprites['background'] = pygame.transform.scale(pygame.image.load(os.path.join('Img', 'background'
                                                                                                         '.png')),
                                                                   (self.__ScreenWidth, self.__ScreenHeight)).convert()
        self.__Game_sprites['player'] = pygame.image.load(os.path.join('Img', 'bird.png')).convert_alpha()
        self.__Game_sprites['Pipe'] = pygame.image.load(os.path.join('Img', 'pipe.png'))
        self.__Game_sprites['Pipe'] = pygame.transform.scale(self.__Game_sprites['Pipe'],
                                                             (self.__Game_sprites['Pipe'].get_width() + 10,
                                                              self.__Game_sprites[
                                                                  'Pipe'].get_height() + 70)).convert_alpha()

        self.__Game_sprites['Base'] = pygame.transform.scale(pygame.image.load(os.path.join('Img', 'base.png')),
                                                             (self.__ScreenWidth,
                                                              int(self.__ScreenHeight / 8))).convert()
        # Game fonts
        self.__game_screen_rect = self.__Game_sprites['screen'].get_rect(center=(self.__ScreenWidth // 2,
                                                                                 self.__ScreenHeight // 2))

    # -----------------

    def game_start_screen(self):
        self.__Window.blit(self.__Game_sprites['background'], (0, 0))
        self.__Window.blit(self.__Game_sprites['screen'], self.__game_screen_rect)
        self.__Window.blit(self.__Game_sprites['Base'], (0, 530))
        self.__Window.blit(self.__Game_sprites['screen'], self.__game_screen_rect)
        pygame.display.update()
        for event in pygame.event.get():
            m_btn = pygame.mouse.get_pressed(num_buttons=3)
            if m_btn[0]:
                return True
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return False

    def draw_score_winner_screen(self, all_scores, current_score, Highest_scorer):
        self.__Window.blit(self.__Game_sprites['screen'], self.__game_screen_rect)
        score_surface = self.__game_font.render(f"Score: {str(int(current_score))}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(self.__ScreenWidth // 2, self.__ScreenHeight // 8))
        self.__Window.blit(score_surface, score_rect)
        if not Highest_scorer:
            high_score_surface = self.__game_font.render(f"High Score: {str(int(max(self.__scores)))}", True,
                                                         (255, 0, 0))
            high_score_rect = high_score_surface.get_rect(center=(self.__ScreenWidth // 2, 500))
            self.__Window.blit(high_score_surface, high_score_rect)
        else:
            line = f"""New High Score :: {str(int(max(all_scores)))}"""
            high_score_surface = self.__game_font.render(line, True, (255, 255, 0))
            high_score_rect = high_score_surface.get_rect(center=(self.__ScreenWidth // 2, 480))
            highest_score_message = self.__game_font.render(f"You are the new Highest scorer", True, (0, 255, 255))
            highest_score_message_rect = highest_score_message.get_rect(center=(self.__ScreenWidth // 2, 500))
            self.__Window.blit(high_score_surface, high_score_rect)
            self.__Window.blit(highest_score_message, highest_score_message_rect)
        pygame.display.update()

    def create_pipe(self):
        pipe_high = random.randrange(300, 550, 70)

        new_bottom_pipe = (self.__Game_sprites['Pipe']).get_rect(midtop=(self.__ScreenWidth + self.__pipe_distance,
                                                                         pipe_high))
        new_top_pipe = (self.__Game_sprites['Pipe'].get_rect(midbottom=(self.__ScreenWidth + self.__pipe_distance,
                                                                        pipe_high - 200)))
        return new_bottom_pipe, new_top_pipe

    def draw_pipes(self, all_pipes):
        for pipe in all_pipes:
            if pipe.bottom >= 600:
                self.__Window.blit(self.__Game_sprites['Pipe'], pipe)
            else:
                self.__Window.blit(pygame.transform.flip(self.__Game_sprites['Pipe'], False, True), pipe)

    def draw_screen(self, bird_surface, bird_rect, Floor_flow, all_pipes, current_score, game_Status):
        self.__Window.blit(self.__Game_sprites['background'], (0, 0))
        self.__Window.blit(bird_surface, bird_rect)
        if game_Status == "main_game":
            self.draw_pipes(all_pipes)
            self.display_live_score(game_Status, current_score)
        self.__Window.blit(self.__Game_sprites['Base'], (Floor_flow, 530))
        self.__Window.blit(self.__Game_sprites['Base'], (Floor_flow + 390, 530))
        pygame.display.update()
        self.fpsClock.tick(self.__FPS)

    def is_collide(self, bird_rect, pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                return True
        if bird_rect.top <= -20:
            return True
        if bird_rect.bottom >= 600 - self.__ScreenHeight // 8:
            return True
        return False

    def display_live_score(self, game_status, score):
        print(game_status)
        if game_status == "main_game":
            score_surface = self.__game_font.render(str(int(score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(self.__ScreenWidth // 2, self.__ScreenHeight // 8))
            self.__Window.blit(score_surface, score_rect)

    def main_loop(self):
        score = 0
        jump_power = 5
        # Pipes
        pipe_lst = []
        SPAWN_PIPE = pygame.USEREVENT
        pygame.time.set_timer(SPAWN_PIPE, 1200)

        gravity_var = self.__gravity
        bird_movement_local = self.__bird_movement

        running = True
        bird_surface = self.__Game_sprites['player']
        bird_rect = bird_surface.get_rect(center=(self.__ScreenWidth // 2, self.__ScreenHeight // 2))
        base_pos = 0
        moving_speed = 2

        last_score = 0
        highest_scorer = False
        game_start = False
        is_Active = False

        while running:

            if not game_start:
                is_Active = self.game_start_screen()
                if is_Active:
                    game_start = True
            else:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == SPAWN_PIPE:
                        pipe_lst.extend(self.create_pipe())

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and is_Active:
                        bird_movement_local = 0
                        bird_movement_local -= jump_power
                        self.__Game_sounds['wing'].play()

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_Active:
                        is_Active = True
                        bird_rect.center = (self.__ScreenWidth // 4, self.__ScreenHeight // 9)
                        score = 0
                        pipe_lst.clear()
                        bird_movement_local = 0
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        print("yes")
                        is_Active = False
                        game_start = False

                if is_Active:
                    score += 0.02
                    rotate_bird_animation = rotate_bird(bird_surface, bird_movement_local)
                    self.draw_screen(rotate_bird_animation, bird_rect, base_pos, pipe_lst, score, "main_game")
                    pipe_lst = move_pipes(pipe_lst, moving_speed)
                    bird_movement_local += gravity_var
                    bird_rect.centery += bird_movement_local

                    if score <= 50:
                        base_pos -= 2
                        moving_speed = 2

                    elif 50 <= score <= 79:
                        if score == 50:
                            pipe_lst.clear()
                        base_pos -= 3
                        moving_speed = 3

                    elif 80 <= score <= 100:
                        if score == 80:
                            pipe_lst.clear()
                        base_pos -= 6
                        moving_speed = 6

                    if base_pos <= -390:
                        base_pos = 0

                    if self.is_collide(bird_rect, pipe_lst):
                        self.__Game_sounds['hit'].play()
                        if score in self.__scores:
                            highest_scorer = False
                        elif score > max(self.__scores):
                            highest_scorer = True
                        elif score < max(self.__scores):
                            highest_scorer = False
                        self.__scores.append(score)
                        self.__Game_sounds['die'].play()
                        self.draw_screen(rotate_bird_animation, bird_rect, base_pos, pipe_lst, score, "game_over")
                        is_Active = False
                        last_score = score
                        score = 0
                    if not is_Active:
                        self.draw_score_winner_screen(self.__scores, last_score, highest_scorer)
                        pygame.time.delay(2000)
                        score = 0
                        pipe_lst.clear()
                        bird_rect.center = (self.__ScreenWidth // 4, self.__ScreenHeight // 9)
                        bird_movement_local = 0
                        game_start = False

    def start_game(self):
        self.main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
