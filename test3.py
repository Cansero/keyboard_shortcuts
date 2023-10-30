import keyboard
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGroupBox, QApplication


class Win(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test')

        layout = QVBoxLayout()
        btn = QPushButton('Press')
        btn.clicked.connect(self.do_something)
        layout.addWidget(btn)

        self.setLayout(layout)

        keyboard.add_hotkey('m+n', print, ('hola',))

    def do_something(self):
        keyboard.send('m+n')


if __name__ == '__main__':
    app = QApplication([])
    w = Win()
    w.show()
    app.exec()
    