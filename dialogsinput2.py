import sys

from PySide6.QtWidgets import(
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Dialog input")

        layout = QVBoxLayout()

        button1 = QPushButton("Integer")
        button1.clicked.connect(self.getInt)
        layout.addWidget(button1)

        button2 = QPushButton("Float")
        button2.clicked.connect(self.getFloat)
        layout.addWidget(button2)

        button3 = QPushButton("Select")
        button3.clicked.connect(self.getStrFromList)
        layout.addWidget(button3)

        button4 = QPushButton("String")
        button4.clicked.connect(self.getStr)
        layout.addWidget(button4)

        button5 = QPushButton("Text")
        button5.clicked.connect(self.getText)
        layout.addWidget(button5)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def getInt(self):
        title = "Enter a integer"
        label = "Type your integer here"
        myIntVal, ok = QInputDialog.getInt(
            self, 
            title,
            label,
            value=0,
            minValue=-5,
            maxValue=5,
            step=1
        )
        print("Result:", ok, myIntVal)
    def getFloat(self):
        title = "Enter a float"
        label = "Type your float here"
        myFloatValue, ok = QInputDialog.getDouble(
            self,
            title,
            label,
            value=0,
            minValue=-5.3,
            maxValue=5.6,
            decimals=2
        )
        print("Result:", ok, myFloatValue)
    def getStrFromList(self):
        title = "Select a string"
        label = "Select a fruit from the list"
        items = ["apple", "pear", "orange", "grape"]
        initial_selection = 2
        mySelectedStr, ok = QInputDialog.getItem(
            self,
            title, 
            label,
            items,
            current=initial_selection,
            editable=False
        )
        print("Result:", ok, mySelectedStr)
    def getStr(self):
        title = "Enter a string"
        label = "Type your password"
        text = "my secret password"
        mode = QLineEdit.Password
        mySelectedStr, ok = QInputDialog.getText(
            self,
            title,
            label,
            mode,
            text
        )
        print("Result:", ok, mySelectedStr)
    def getText(self):
        title = "Enter text"
        label = "Type your novel here"
        text = "Once upon a time.."
        mySelectedStr, ok = QInputDialog.getMultiLineText(
            self,
            title,
            label, 
            text
        )
        print("Result:", ok, mySelectedStr)

app = QApplication()

window = MainWindow()
window.show()

app.exec()