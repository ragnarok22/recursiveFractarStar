import sys

from PyQt6.QtWidgets import QApplication

from windows import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    app.exec()
