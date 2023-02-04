from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        button = QPushButton("Press me")
        button.setCheckable(True)
        button.clicked.connect(self.button_was_clicked)
        button.clicked.connect(self.button_was_toggled)

        self.setCentralWidget(button)
    
    def button_was_clicked(self):
        print("Clicked")
    
    def button_was_toggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()