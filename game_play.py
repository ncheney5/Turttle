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
        