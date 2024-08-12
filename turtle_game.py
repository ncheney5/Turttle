import pygame as pg
from objects import turtle, tower, icetower, box, mouse, box_1, box_2, box_3

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

def draw(turt, set_1, set_2, set_3, mouse, objects, selected_object,tile_size=50):
    pg.mouse.set_visible(False)
    win.blit(screen, (0, 0))
    win.blit(screen_tint, (15, 15))
    win.blit(grid, (15, 15))
    win.blit(sidebar, (800, 0))
    
    set_1.draw(win)
    set_2.draw(win)
    set_3.draw(win)

    if selected_object:
        win.blit(selected_object.image_2, selected_object.rect.topleft)

    for obj in objects:
        win.blit(obj.image_2, (obj.x, obj.y))
        #draw the hitbox
        pg.draw.rect(win, (255, 0, 0), obj.rect, 2)

    win.blit(turt.image, (turt.rect.x, turt.rect.y))
    win.blit(mouse.image, (mouse.x, mouse.y))
    
    pg.display.update()

def main():
    turt = turtle(100, 100)
    running = True
    move_count = 0
    turn_left = 0
    turn_right = 0
    set_1 = box_1()
    set_2 = box_2()
    set_3 = box_3()
    objects = []
    dragging = False
    selected_object = None

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                # Check if click is on set_1, set_2, or set_3
                for object in objects:
                    if object.rect.collidepoint(pos):
                        selected_object = object
                        dragging = True
                        objects.remove(object)
                        break

                if set_1.rect.collidepoint(pos):
                    selected_object = icetower(pos[0], pos[1])
                    dragging = True
                elif set_2.rect.collidepoint(pos):
                    selected_object = tower(pos[0], pos[1])
                    dragging = True
                elif set_3.rect.collidepoint(pos):
                    selected_object = box(pos[0], pos[1])
                    dragging = True

            elif event.type == pg.MOUSEBUTTONUP:
                if dragging and selected_object:
                    # Place the selected object
                    selected_object.update_position(*pg.mouse.get_pos())
                    if selected_object not in objects:
                        objects.append(selected_object)
                    selected_object = None
                    dragging = False

            elif event.type == pg.MOUSEMOTION and dragging and selected_object:
                # Update the position while dragging
                selected_object.update_position(*pg.mouse.get_pos())

        clock.tick(60)

        if move_count > 0:
            move_count += 1
        if move_count == 5:
            move_count = 0
        if turn_left > 0:
            turn_left += 1
        if turn_left == 50:
            turn_left = 0
        if turn_right > 0:
            turn_right += 1
        if turn_right == 50:
            turn_right = 0

        mouse.x, mouse.y = pg.mouse.get_pos()
        draw(turt, set_1, set_2, set_3, mouse, objects, selected_object)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and turn_left == 0:
            turt.rotate_left(90)
            turn_left = 1
        if keys[pg.K_RIGHT] and turn_right == 0:
            turt.rotate_right(-90)
            turn_right = 1
        if keys[pg.K_UP] and move_count == 0:
            turt.move_forward(turt.speed)
            move_count = 1
        
    pg.quit()

main()
