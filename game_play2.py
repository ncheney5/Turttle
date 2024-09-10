import pygame as pg
import time as t
from objects import turtle, tower, icetower, box, mouse, box_1, box_2, box_3, box_4,box_5,box_6,box_7,box_8,box_9,box_10,gem_1,gem_2,gem_3,gem_4, selection_box

#this will need to be modularized to acount for funtions and text options as well as cards

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

def map_selector():
    # Initialize text input variables
    input_active = True
    user_text = ''
    input_box = pg.Rect(600, 600, 140, 32)
    color_inactive = pg.Color('black')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive

    while input_active:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return None
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    input_active = False
                elif event.key == pg.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        win.blit(screen, (0, 0))

        # Render text
        txt_surface = font.render(user_text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.draw.rect(win, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)

    return user_text

map_name = map_selector()