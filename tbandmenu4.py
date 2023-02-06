import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QStatusBar,
    QWidget,
    QToolBar
)
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar")

        label = QLabel("Hellow")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        # toolbar.setNativeToolBar(False)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolbarButtonClick)
        button_action.setCheckable(True)

        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolbarButtonClick(self, s):
        print("click", s)

app = QApplication()

window = MainWindow()
window.show()

app.exec()