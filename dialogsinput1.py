import sys

from PySide6.QtWidgets import(
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog input")

        button1 = QPushButton("Integer")

        button1.clicked.connect(self.getAnInt)

        self.setCentralWidget(button1)

    def getAnInt(self):
        intVal, ok = QInputDialog.getInt(
            self, "Get an Integer", "Enter a number"
        )
        print("Result:", ok, intVal)

app = QApplication()

window = MainWindow()
window.show()

app.exec()