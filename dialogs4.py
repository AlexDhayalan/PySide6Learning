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
        self.setWindowTitle("Message box 2")

        btn = QPushButton("Press me!")
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)

    def button_clicked(self, s):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is the question dialog")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dlg.setIcon(QMessageBox.Question)
        button = dlg.exec()

        if button == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

app = QApplication()

window = MainWindow()
window.show()

app.exec()