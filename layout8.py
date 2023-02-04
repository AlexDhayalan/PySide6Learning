import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QWidget
)

from layoutcolorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("stacked layout buttons")

        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addLayout(self.stacklayout)

        btn = QPushButton("Red")
        btn.pressed.connect(self.activateTab1)
        buttonLayout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn = QPushButton("Green")
        btn.pressed.connect(self.activateTab2)
        buttonLayout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        btn = QPushButton("Yellow")
        btn.pressed.connect(self.activateTab3)
        buttonLayout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def activateTab1(self):
        self.stacklayout.setCurrentIndex(0)

    def activateTab2(self):
        self.stacklayout.setCurrentIndex(1)

    def activateTab3(self):
        self.stacklayout.setCurrentIndex(2)

app = QApplication()

window = MainWindow()
window.show()

app.exec()