from PyQt6.QtCore import QThread

from logic import draw_fractal


class FractalThread(QThread):
    def __init__(self, lists: list, widget, x_center: int, y_center: int, cota_dim: int):
        super(FractalThread, self).__init__()
        self.lists = lists
        self.x_center = x_center
        self.y_center = y_center
        self.cota_dim = cota_dim
        self.widget = widget

    def run(self) -> None:
        draw_fractal(self.lists, self.widget, self.x_center, self.y_center, self.cota_dim)
