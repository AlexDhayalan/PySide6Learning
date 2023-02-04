import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import(
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QWidget
)
#QVboxlayout
from layoutcolorwidget import Color

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("layout 2a")

        layout = QHBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = Mainwindow()
window.show()

app.exec()