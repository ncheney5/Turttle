import pygame as pg
import time as t
from objects import turtle, tower, icetower, box, mouse, box_1, box_2, box_3, box_4,box_5,box_6,box_7,box_8,box_9,box_10,gem_1,gem_2,gem_3,gem_4

pg.init()
win = pg.display.set_mode((1100, 750))
pg.display.set_caption('Turtle Game')
image = pg.image.load('background.jpeg')
screen = pg.transform.scale(image, (1100, 750))
clock = pg.time.Clock()
font = pg.font.Font(None, 36)
grid = pg.transform.scale_by(pg.image.load('grid.png'), 0.9)
mouse = mouse(0, 0)
sidebar1 = pg.transform.rotate(pg.image.load('side_bar.jpeg'), 90)
sidebar1.set_alpha(150)
sidebar = pg.transform.scale(sidebar1, (400, 900))
screen_tint = pg.transform.scale(pg.image.load('side_bar.jpeg'), (720, 720))
screen_tint.set_alpha(60)

def draw():
    pg.mouse.set_visible(False)
    win.blit(screen, (0, 0))
    win.blit(screen_tint, (15, 15))
    win.blit(mouse.image, (mouse.x, mouse.y))
    
    pg.display.update()

def main():
    run = True
    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEMOTION:
                mouse.x, mouse.y = pg.mouse.get_pos()
        draw()
    pg.quit()

main()