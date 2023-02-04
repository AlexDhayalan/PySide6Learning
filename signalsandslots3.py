from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("my app")

        self.button = QPushButton("Press me")
        self.button.clicked.connect(self.button_was_clicked)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        self.button.setText("Already clicked")
        self.button.setEnabled(False)

        self.setWindowTitle("Oneshot")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()