import pygame
import os

#  Actual game starts here

# PARAMETERS
# ------------------

spaceship_width = 55
spaceship_height = 40
width, height = 900, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("SpaceShooter Game")

white = (255, 255, 255)
black = (0, 0, 0)

FPS = 60
Yellow_SpaceShip = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
Red_SpaceShip = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
yellow_spaceship = pygame.transform.rotate(
    pygame.transform.scale(Yellow_SpaceShip, (spaceship_width, spaceship_height)), 90)
red_spaceship = pygame.transform.rotate(pygame.transform.scale(Red_SpaceShip, (spaceship_width, spaceship_height)), 270)
VEL = 5
Border = pygame.Rect(width // 2, 0, 10, height)
Bullet_VEL = 5
MAX_BULLETS = 5
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

# ------------------


def draw_window(red, yellow, yellow_bullets, red_bullets):
    window.fill(white)
    pygame.draw.rect(window, black, Border)
    window.blit(red_spaceship, (red.x, red.y))
    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    for bullet in red_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(window, (255, 255, 0), bullet)
    pygame.display.update()


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > Border.x + Border.width + 15:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < width:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height + 20 < height:  # DOWN
        red.y += VEL


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < Border.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 20 < height:  # DOWN
        yellow.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullets in yellow_bullets:
        bullets.x += Bullet_VEL
        if red.colliderect(bullets):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullets)
        elif bullets.x > width:
            yellow_bullets.remove(bullets)

    for bullets in red_bullets:
        bullets.x -= Bullet_VEL
        if yellow.colliderect(bullets):
            pygame.event.post(pygame.event.Event(red_hit))
            red_bullets.remove(bullets)
        elif bullets.x < 0:
            red_bullets.remove(bullets)


def main():
    # spaceship dimensions
    red = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    yellow = pygame.Rect(100, 300, spaceship_width, spaceship_height)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        keys_pressed = pygame.key.get_pressed()
        print(red_bullets, yellow_bullets)

        # For movement---------------->>
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        # <<---------------------------

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        draw_window(red, yellow, yellow_bullets, red_bullets)
    pygame.quit()


if __name__ == "__main__":
    main()
