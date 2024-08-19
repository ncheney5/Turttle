import pygame as pg
from objects import turtle, tower, icetower, box, mouse, box_1, box_2, box_3, box_4,box_5,box_6,box_7,box_8,box_9,box_10,gem_1,gem_2,gem_3,gem_4
from main_menu import main

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

def get_map_name():
    # Initialize text input variables
    input_active = True
    user_text = ''
    input_box = pg.Rect(300, 300, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
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

        win.fill((30, 30, 30))  # Clear the screen

        # Render text
        txt_surface = font.render(user_text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pg.draw.rect(win, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)

    return user_text

def draw(set_1, set_2, set_3,set_4,set_5,set_6,set_7,set_8,set_9,set_10, mouse, objects, selected_object,tile_size=50):
    pg.mouse.set_visible(False)
    win.blit(screen, (0, 0))
    win.blit(screen_tint, (15, 15))
    win.blit(grid, (15, 15))
    win.blit(sidebar, (800, 0))
    
    set_1.draw(win)
    set_2.draw(win)
    set_3.draw(win)
    set_4.draw(win)
    set_5.draw(win)
    set_6.draw(win)
    set_7.draw(win)
    set_8.draw(win)
    set_9.draw(win)
    set_10.draw(win)

    if selected_object:
        win.blit(selected_object.image_2, selected_object.rect.topleft)

    for obj in objects: 
        win.blit(obj.image_2, (obj.x, obj.y))
        #draw the hitbox
        pg.draw.rect(win, (255, 0, 0), obj.rect, 2)

    win.blit(mouse.image, (mouse.x, mouse.y))
    
    pg.display.update()

def map_editor():
    running = True
    move_count = 0
    turn_left = 0
    turn_right = 0
    set_1 = box_1()
    set_2 = box_2()
    set_3 = box_3()
    set_4 = box_4()
    set_5 = box_5()
    set_6 = box_6()
    set_7 = box_7()
    set_8 = box_8()
    set_9 = box_9()
    set_10 = box_10()
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
                elif set_4.rect.collidepoint(pos):
                    selected_object = gem_1(pos[0], pos[1])
                    dragging = True
                elif set_5.rect.collidepoint(pos):
                    selected_object = gem_2(pos[0], pos[1])
                    dragging = True
                elif set_6.rect.collidepoint(pos):
                    selected_object = gem_3(pos[0], pos[1])
                    dragging = True
                elif set_7.rect.collidepoint(pos):
                    selected_object = gem_4(pos[0], pos[1])
                    dragging = True
                elif set_8.rect.collidepoint(pos):
                    selected_object = turtle(pos[0], pos[1])
                    dragging = True
                elif set_10.rect.collidepoint(pos):
                    map_name = get_map_name()
                    if map_name:
                        try:
                            with open('maps.txt', 'a') as f:
                                for obj in objects:
                                    image_filename = obj.__class__.__name__.lower() + '.png'
                                    f.write(f'{obj.x},{obj.y},{image_filename}\n')
                                f.write(f'map_name,{map_name}\n')
                            print("Map saved successfully")
                        except IOError as e:
                            print(f"Error saving map: {e}")
                    running=False
                    main()

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

            for object in objects:
                # Check if object is on set_9
                if object.rect.collidepoint(set_9.rect.topleft) or object.rect.collidepoint(set_9.rect.bottomleft) or object.rect.collidepoint(set_9.rect.topright) or object.rect.collidepoint(set_9.rect.bottomright):
                    objects.remove(object)

        clock.tick(60)

        mouse.x, mouse.y = pg.mouse.get_pos()
        draw(set_1, set_2, set_3,set_4,set_5,set_6,set_7,set_8,set_9,set_10, mouse, objects, selected_object)

       
    pg.quit()

