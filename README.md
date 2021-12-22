# recursiveFractarStar
Code to draw a Recursive Fractar Star:

```python
def draw(*args):
    # method to draw
    pass


def draw_fractal(x_center, y_center, cota_dim):
    side = cota_dim / 2
    if side < 1:
        return

    # calculate corners
    left = x_center - side / 2
    up = y_center - side / 2
    right = x_center + side / 2
    bottom = y_center + side / 2

    # recursively draw the 4 quadrants
    draw_fractal(left, up, cota_dim / 2)
    draw_fractal(left, bottom, side)
    draw_fractal(right, up, side)
    draw_fractal(right, bottom, side)

    # draw central square
    draw(left, up, right - left, bottom - up)
```