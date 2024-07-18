import pygame as pg
from objects import turtle,tower,icetower,box
import time

pg.init()
win=pg.display.set_mode((800,600))
pg.display.set_caption('Turtle Game')
image = pg.image.load('background.jpeg')
screen= pg.transform.scale(image, (800, 600))
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

def draw(turt):
    win.blit(screen, (0, 0))
    win.blit(turt.image, (turt.x, turt.y))
    
    pg.display.update()

def main():
    turt=turtle(100,100)
    running = True
    move_count=0

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        clock.tick(60)

        if move_count>0:
            mover_count+=1
        if move_count==5:
            move_count=0

        draw(turt)

        kyes=pg.key.get_pressed()
        if kyes[pg.K_LEFT]:
            turt.rotate_left
        if kyes[pg.K_RIGHT]:
            turt.rotate_right
        if kyes[pg.K_UP]:
            turt.move_forward
            move_count=1
        

    pg.quit()


main()