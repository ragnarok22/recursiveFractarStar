from time import sleep

SLOW = 0.1
FAST = 0.01
FASTER = 0.001
NO_TIME = 0


def draw_fractal(lists, widget, x_center, y_center, cota_dim):
    side = cota_dim / 2
    if side < 1:
        return

    # calculate corners
    left = x_center - side / 2
    up = y_center - side / 2
    right = x_center + side / 2
    bottom = y_center + side / 2

    # recursively draw the 4 quadrants
    draw_fractal(lists, widget, left, up, cota_dim / 2)
    draw_fractal(lists, widget, left, bottom, side)
    draw_fractal(lists, widget, right, up, side)
    draw_fractal(lists, widget, right, bottom, side)

    # draw central square
    lists.append([left, up, right - left, bottom - up])
    sleep(NO_TIME)
    widget.update()
