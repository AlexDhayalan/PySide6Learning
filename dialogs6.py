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
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went wrong.",
            buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard            
        )
        if button == QMessageBox.Discard:
            print("Discard")
        elif button == QMessageBox.NoToAll:
            print("No to All")
        else:
            print("Ignore!")

app = QApplication()

window = MainWindow()
window.show()

app.exec()