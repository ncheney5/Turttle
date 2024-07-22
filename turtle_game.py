import pygame as pg
from objects import turtle,tower,icetower,box,mouse,box_1,box_2,box_3
import time

pg.init()
win=pg.display.set_mode((1100,750))
pg.display.set_caption('Turtle Game')
image = pg.image.load('background.jpeg')
screen= pg.transform.scale(image, (1100, 750))
clock = pg.time.Clock()
font = pg.font.Font(None, 36)
grid=pg.transform.scale_by(pg.image.load('grid.png'), 0.9)
mouse=mouse(0,0)
sidebar1=pg.transform.rotate(pg.image.load('side_bar.jpeg'),90)
sidebar1.set_alpha(150)
sidebar=pg.transform.scale(sidebar1, (400, 900))
screen_tint=pg.transform.scale(pg.image.load('side_bar.jpeg'), (720, 720))
screen_tint.set_alpha(60)

def draw(turt,set_1,set_2,set_3,tile_size=50,):
    win.blit(screen, (0, 0))
    win.blit(screen_tint, (15,15))
    win.blit(grid, (15, 15))
    win.blit(sidebar, (800, 0))
    
    set_1.draw(win)
    set_2.draw(win)
    set_3.draw(win)

    win.blit(turt.image, (turt.rect.x, turt.rect.y))

    # for i in range(100,550,tile_size):
    #     pg.draw.line(win,'black', (i,500), (i,100))
    #     pg.draw.line(win,'black', (500,i), (100,i))
    
    pg.display.update()

def main():
    turt=turtle(100,100)
    running = True
    move_count=0
    turn_left=0
    turn_right=0
    set_1=box_1()
    set_2=box_2()
    set_3=box_3()

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        clock.tick(60)

        if move_count>0:
            move_count+=1
        if move_count==5:
            move_count=0
        if turn_left>0:
            turn_left+=1
        if turn_left==50:
            turn_left=0
        if turn_right>0:
            turn_right+=1
        if turn_right==50:
            turn_right=0

        draw(turt,set_1,set_2,set_3)

        kyes=pg.key.get_pressed()
        if kyes[pg.K_LEFT] and turn_left==0:
            turt.rotate_left(90)
            turn_left=1
        if kyes[pg.K_RIGHT] and turn_right==0:
            turt.rotate_right(-90)
            turn_right=1
        if kyes[pg.K_UP] and move_count==0:
            turt.move_forward(turt.speed)
            move_count=1
        

    pg.quit()


main()