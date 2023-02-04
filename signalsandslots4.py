from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    "My app",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong"
]

class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.count = 0
        self.setWindowTitle("My app")

        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.button_was_clicked)

        self.windowTitleChanged.connect(self.window_title_changed)

        self.setCentralWidget(self.button)
    
    def button_was_clicked(self):
        print("Clicked")
        new_window_title = choice(window_titles)
        print("Setting title : %s" %new_window_title)
        self.setWindowTitle(new_window_title)

    def window_title_changed(self, window_title):
        print("window title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication()

window = MainWindow()
window.show()

app.exec()
