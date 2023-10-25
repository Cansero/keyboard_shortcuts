from PySide6.QtCore import QSize, QObject
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QDialogButtonBox, QMainWindow, QWidget, \
    QPushButton, QBoxLayout, QHBoxLayout

from time import sleep


class Message(QMainWindow):
    def __init__(self):
        super(Message, self).__init__()
        self.setWindowTitle('test')
        self.label = QLabel('Hola')

        self.layout = QVBoxLayout()
        add_to(self.layout, [self.label])

        lista = ['test', 'test2', 'test3']
        for i in lista:
            lay = QHBoxLayout()
            lab = QLabel(i)
            btn = QPushButton(self, 'print parent')
            btn.setToolTip(i)
            btn.clicked.connect(self.print_parent)
            btn.clicked.emit(lab)
            add_to(lay, [lab, btn])
            add_to(self.layout, [lay], True)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def print_parent(self, lab):
        lab.setText('lol')


def add_to(layout: QBoxLayout, widgets, is_layout=False):
    for widget in widgets:
        if is_layout:
            layout.addLayout(widget)
        else:
            layout.addWidget(widget)


if __name__ == '__main__':
    app = QApplication([])
    x = Message()
    x.show()
    app.exec()
