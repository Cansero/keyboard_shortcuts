from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGroupBox, QApplication
from random import randint

class Win(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test')

        self.test_grbox = QGroupBox('Test')
        self.test_grbox_lay = QVBoxLayout()
        self.test_grbox_lay.setAlignment(Qt.AlignTop)

        self.labels = {}

        self.add_btn = QPushButton('Press to add here')
        self.add_btn.clicked.connect(self.add_to_grbox)

        add_to(self.test_grbox_lay, self.add_btn)
        self.test_grbox.setLayout(self.test_grbox_lay)

        layout = QVBoxLayout()
        add_to(layout, self.test_grbox)
        self.setLayout(layout)

    def add_to_grbox(self):
        n = randint(0, 10000)
        label = QLabel(f'test{n}')
        btn = QPushButton('Remove this')
        btn.clicked.connect(lambda: self.remove_label(n))
        lay = QHBoxLayout()
        add_to(lay, label, btn)
        add_to(self.test_grbox_lay, lay, is_layout=True)
        self.labels[n] = [lay, [label, btn]]

    def remove_label(self, index):
        rmv = self.labels.pop(index)
        self.test_grbox_lay.removeItem(rmv[0])
        for item in rmv[1]:
            item.hide()


def add_to(layout, *args, is_layout=False):
    for arg in args:
        if is_layout:
            layout.addLayout(arg)
        else:
            layout.addWidget(arg)


if __name__ == '__main__':
    app = QApplication([])
    w = Win()
    w.show()
    app.exec()
