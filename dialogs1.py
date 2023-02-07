import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog")

        button = QPushButton("Press me for a dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        dlg = QDialog(self)
        dlg.setWindowTitle("?")
        dlg.exec()

app = QApplication()

window = MainWindow()
window.show()

app.exec()