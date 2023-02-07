import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Message box 1")

        button = QPushButton("Press me for a dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a simple dialog")
        button = dlg.exec()

        if(button == QMessageBox.Ok):
            print("OK!")

app = QApplication()

window = MainWindow()
window.show()

app.exec()