import pygame as pg
import time as t
from objects import turtle, tower, icetower, box, mouse, box_1, box_2, box_3, box_4,box_5,box_6,box_7,box_8,box_9,box_10,gem_1,gem_2,gem_3,gem_4, selection_box
from turtle_game import map_editor

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

def draw(box_1, box_2, box_3, box_4, box_5,cards,txt,funtions):
    pg.mouse.set_visible(False)
    win.blit(screen, (0, 0))

    #title box
    pg.draw.rect(win, 'black', (300, 10, 500, 150), 0)
    pg.draw.rect(win, 'dark green', (305, 15, 490, 140), 0)
    title = font.render('Turtle Game', True, 'light green')
    card= font.render('Cards', True, 'white')
    text= font.render('Text', True, 'white')
    funtion= font.render('Funtions', True, 'white')
    play= font.render('Play', True, 'white')
    build= font.render('Build Map', True, 'white')
    card=pg.transform.scale(card, (100, 50))
    text=pg.transform.scale(text, (100, 50))
    funtion=pg.transform.scale(funtion, (100, 50))
    play=pg.transform.scale(play, (100, 50))
    build=pg.transform.scale(build, (100, 50))
    title=pg.transform.scale(title, (450, 100))
    win.blit(title, (325, 30))

    box_1.draw(win,color='black')
    box_2.draw(win,color='black')
    if cards:
        box_3.draw(win,color='blue')
    if not cards:
        box_3.draw(win,color='black')
    if txt:
        box_4.draw(win,color='blue')
    if not txt:
        box_4.draw(win,color='black')
    if funtions:
        box_5.draw(win,color='blue')
    if not funtions:
        box_5.draw(win,color='black')

    win.blit(card, (100, 500))
    win.blit(text, (450, 500))
    win.blit(funtion, (800, 500))
    win.blit(play, (150, 300))
    win.blit(build, (600, 300))

    win.blit(mouse.image, (mouse.x, mouse.y))
    
    
    pg.display.update()

def main():
    box_1=selection_box(125,190,400,250)
    box_2=selection_box(575,190,400,250)
    box_3=selection_box(75,475,250,250)
    box_4=selection_box(420,475,250,250)
    box_5=selection_box(760,475,250,250)

    cards=True
    txt=False
    funtions=False


    run = True
    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEMOTION:
                mouse.x, mouse.y = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if box_1.rect.collidepoint(mouse.x, mouse.y):
                    if not cards and not txt:
                        pass
                    elif cards:
                        pass
                if box_2.rect.collidepoint(mouse.x, mouse.y):
                    run=False
                    map_editor()
                if box_3.rect.collidepoint(mouse.x, mouse.y):
                    if cards:
                        cards=False
                    elif not cards:
                        cards=True
                        txt=False
                if box_4.rect.collidepoint(mouse.x, mouse.y):
                    if txt:
                        txt=False
                    elif not txt:
                        txt=True
                        cards=False
                if box_5.rect.collidepoint(mouse.x, mouse.y):
                    if funtions:
                        funtions=False
                    elif not funtions:
                        funtions=True
        

        
        draw(box_1, box_2, box_3, box_4, box_5,cards,txt,funtions)

    

    pg.quit()