from PyQt6 import QtGui
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QWidget

from thread import FractalThread


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Recursive Fractar star')
        self.lines = []

        self.thread = FractalThread(self.lines, self, 250, 250, 500)
        self.thread.start()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        for line in self.lines:
            painter.drawRect(line[0], line[1], line[2], line[3])
        # draw_fractal(painter, 250, 250, 500)
        painter.end()
