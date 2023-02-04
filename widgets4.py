import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

#combo box

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combo box")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        widget.setMaxCount(10)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

app = QApplication()

window = MainWindow()
window.show()

app.exec()