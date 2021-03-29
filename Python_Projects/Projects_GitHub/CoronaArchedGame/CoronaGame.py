from __future__ import division
import pygame as pg
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'Assets')
sound_dir = path.join(path.dirname(__file__), 'Sonds')

width = 480
height = 600
FPS = 60
power_time = 5000

white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Go Corona")
clock = pg.time.Clock()

font_name = pg.font.match_font('arial')


def main_menu():
    global screen

    menu_song = pg.mixer.music.load(path.join(sound_dir, "menu.ogg"))
    title = pg.image.load(path.join(img_dir, "main.png")).convert()
    title = pg.transform.scale(title, (width, height), screen)

    screen.blit(title, (0, 0))
    pg.display.update()

    while True:
        ev = pg.event.poll()
        if ev.type == pg.KEYDOWN:
            if ev.key == pg.K_RETURN:
                break
            elif ev.key == pg.K_q:
                pg.quit()
                quit()

        else:
            draw_text(screen, "press [Enter] to Begin", 30, width / 2, height / 2)
            draw_text(screen, "Press [Q] to Quit", 30, width/2, (height/2)+40)
            pg.display.update()
    
    ready = pg.mixer.Sound(path.join(sound_dir, 'getready.ogg'))
    ready.play()
    screen.fill((0, 0, 0))
    draw_text(screen, "Get Ready!!", 40, width/2, height/2)
    pg.display.update()


def draw_text(surface, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def draw_shield_bar(surface, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length
    outline_rect = pg.Rect(x, y, fill, bar_height)
    pg.draw.rect(surface, white, outline_rect, 2)


def draw_lives(surface, x, y, lives, img):
    pass




