import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.s = ''

    def initUI(self):
        grid = QGridLayout()
        vbox = QVBoxLayout()
        self.display = QLineEdit('0')
        self.display.setFont(QFont('Times', 20))

        names = ['Clear', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '.', '0', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton()
            button.setText(str(name))
            grid.addWidget(button, *position)
            button.clicked.connect(self.buttonclicked)

        vbox.addWidget(self.display)
        vbox.addLayout(grid)
        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 400, 250)
        self.show()

    def buttonclicked(self):
        sender = self.sender()
        if sender.text() in '.0123456789+-*/':
            self.s+=sender.text()
            self.display.setText(self.s)
        if sender.text() == '=':
            res = str(eval(self.s))
            if res == '520':
                self.display.setText('520,zhang jiao')
            else:
                self.display.setText(res)
                self.s = ''
        if sender.text() == 'Back':
            self.s = self.s[:-1]
            self.display.setText(self.s)
        if sender.text() == 'Clear':
            self.s = '0'
            self.display.setText(self.s)
            self.s = ''
        if sender.text() == 'Close':
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exc = Example()
    sys.exit(app.exec_())


