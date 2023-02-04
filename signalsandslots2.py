import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My app")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.button_released)
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def button_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()