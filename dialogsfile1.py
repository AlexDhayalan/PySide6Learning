import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File dialog")

        button1 = QPushButton("Open file")
        button1.clicked.connect(self.getFilename)

        self.setCentralWidget(button1)

    def getFilename(self):
        filename, selectedFilter = QFileDialog.getOpenFileName(self)
        print("Result:", filename, selectedFilter)

app = QApplication()

window = MainWindow()
window.show()

app.exec()