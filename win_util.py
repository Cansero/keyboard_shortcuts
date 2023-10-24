import keyboard
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


class Win(QDialog):
    def __init__(self, shortcuts=None, abbreviations=None):
        super().__init__()
        self.setWindowTitle('Shortcuts and Abbreviations')

        layout = QVBoxLayout()
        short = QLabel('Shortcuts:')
        add_to_layout(layout, [short])
        for key, handler in shortcuts.items():
            lay = QHBoxLayout()
            btn = QPushButton(key)
            btn.clicked.connect(self.use_shortcut)
            rmv_btn = QPushButton('Remove')
            rmv_btn.clicked.connect(lambda: rmv_handler(handler))

            add_to_layout(lay, [btn, rmv_btn])
            add_to_layout(layout, [lay], is_layout=True)

        abbre = QLabel('Abbreviations:')
        add_to_layout(layout, [abbre])
        for key, word in abbreviations.items():
            lay = QHBoxLayout()
            label = QLabel(f'{key} = {word[0]}')
            rmv_btn = QPushButton('Remove')
            rmv_btn.clicked.connect(lambda: rmv_abbre(word[1]))

            add_to_layout(lay, [label, rmv_btn])
            add_to_layout(layout, [lay], is_layout=True)

        self.setLayout(layout)

    def use_shortcut(self):
        keyboard.send(self.sender().text())


def add_to_layout(layout, gadgets, is_layout=False):
    for gadget in gadgets:
        if is_layout:
            layout.addLayout(gadget)
        else:
            layout.addWidget(gadget)



def rmv_handler(handler):
    keyboard.remove_hotkey(handler)


def rmv_abbre(handler):
    keyboard.remove_abbreviation(handler)