import pygame
import os

pygame.font.init()
pygame.mixer.init()

#  Actual game starts here
# PARAMETERS
# ------------------
# sounds
# -----------
Bullet_sound = pygame.mixer.Sound(os.path.join('Sounds', 'Grenade+1.mp3'))
Bullet_fire_sound = pygame.mixer.Sound(os.path.join('Sounds', 'Gun+Silencer.mp3'))
Background_Sound = pygame.mixer.Sound(os.path.join('Sounds', 'videoplayback_4.mp3'))
pygame.mixer.music.set_volume(1.0)
# -----------

# Width & Height
# -------------------
spaceship_width = 55
spaceship_height = 40
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("SpaceShooter Game")
# -------------------

# Colors
# ------------
white = (255, 255, 255)
black = (0, 0, 0)
# -------------

FPS = 60
Yellow_SpaceShip = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
Red_SpaceShip = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
yellow_spaceship = pygame.transform.rotate(
    pygame.transform.scale(Yellow_SpaceShip, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.transform.rotate(
    pygame.transform.scale(Red_SpaceShip, (spaceship_width, spaceship_height)),
    270)

VEL = 5
Border = pygame.Rect(width // 2, 0, 10, height)
Bullet_VEL = 5
MAX_BULLETS_PER_FIRE = 5
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2
space = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (width, height))

# printing scores
Health_font = pygame.font.SysFont('comicsans', 40)
Winner_font = pygame.font.SysFont('comicsans', 100)


def draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health):
    """
    :param red: red Spaceship
    :param yellow: yellow spaceship
    :param yellow_bullets: All the fired Bullets by Yellow spaceship will be here but it will be updated every time
    :param red_bullets:
    :param red_health:
    :param yellow_health:

    :Convention == > we just draw the whole screen or fill it every time
    with updated content such as scores and health it is the main
    function which draws every surface on the window without this
    we can not draw contents in the screen

    """
    window.blit(space, (0, 0))
    pygame.draw.rect(window, black, Border)

    print(red_health)
    print(yellow_health)

    red_health_text = Health_font.render("Health :: " + str(red_health), True, white)
    yellow_health_text = Health_font.render("Health :: " + str(yellow_health), True, white)
    window.blit(red_health_text, (width - red_health_text.get_width() - 30, 10))
    window.blit(yellow_health_text, (5, 10))

    window.blit(red_spaceship, (red.x, red.y))
    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(window, (255, 255, 0), bullet)
    pygame.display.update()


def red_handle_movement(keys_pressed, red):
    """
    :param keys_pressed:
    :param red:
    :return:

    """
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > Border.x + Border.width + 15:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < width:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height + 20 < height:  # DOWN
        red.y += VEL


def yellow_handle_movement(keys_pressed, yellow):
    """
    :param keys_pressed:
    :param yellow:
    :return:
    """
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < Border.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 20 < height:  # DOWN
        yellow.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    """
    :param yellow_bullets:
    :param red_bullets:
    :param yellow:
    :param red:
    :return:
    """
    for bullets in yellow_bullets:
        bullets.x += Bullet_VEL
        if red.colliderect(bullets):
            print("yes red collide")
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullets)
        elif bullets.x > width:
            yellow_bullets.remove(bullets)

    for bullets in red_bullets:
        bullets.x -= Bullet_VEL
        if yellow.colliderect(bullets):
            print("yes yellow collide")
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullets)
        elif bullets.x < 0:
            red_bullets.remove(bullets)


def draw_winner_text(text):
    """
    :param text:
    :return:
    """
    # print("yes")
    draw_txt = Winner_font.render(text, True, white)
    window.blit(draw_txt, (width // 2 - draw_txt.get_width() // 2,
                           height // 2 - draw_txt.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    """
    :return:
    """
    # spaceship dimensions
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # Background_Sound.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS_PER_FIRE:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    Bullet_fire_sound.play()

                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS_PER_FIRE:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    Bullet_fire_sound.play()

            if event.type == red_hit:
                red_health -= 1
                print(red_health)
                Bullet_sound.play()

            if event.type == yellow_hit:
                yellow_health -= 1
                print(yellow_health)
                Bullet_sound.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins !!! viola..."

        if yellow_health <= 0:
            winner_text = "Red Wins !!! viola..."

        if winner_text != "":
            draw_winner_text(winner_text)
            run = False

        keys_pressed = pygame.key.get_pressed()
        print(red_bullets, yellow_bullets)

        # For movement---------------->>
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        # <<---------------------------

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health)
        pygame.display.update()
    # quit()
