import pygame as pg
from objects import turtle,tower,icetower,box
import time

pg.init()
win=pg.display.set_mode((600,600))
pg.display.set_caption('Turtle Game')
image = pg.image.load('background.jpeg')
screen= pg.transform.scale(image, (600, 600))
clock = pg.time.Clock()
font = pg.font.Font(None, 36)

def draw(turt,tile_size=50):
    win.blit(screen, (0, 0))

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

        draw(turt)

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