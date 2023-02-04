import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from layoutcolorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout 1")

        widget = Color('red')
        self.setCentralWidget(widget)

app = QApplication()

window = MainWindow()
window.show()

app.exec()