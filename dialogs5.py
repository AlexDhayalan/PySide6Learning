import sys

from PySide6.QtWidgets import(
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Question dialog")

        btn = QPushButton("Press me!")
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)

    def button_clicked(self, s):
        button = QMessageBox.question(
            self, "Question dialog", "The longer message"
        )
        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No")

app = QApplication()

window = MainWindow()
window.show()

app.exec()