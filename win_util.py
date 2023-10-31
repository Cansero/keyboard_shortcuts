import keyboard
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QDialogButtonBox, \
    QApplication, QCheckBox


def add_to(layout, *args, is_layout=False):
    for arg in args:
        if is_layout:
            layout.addLayout(arg)
        else:
            layout.addWidget(arg)


class AddShort(QDialog):
    def __init__(self):
        super().__init__()

        self.input = None
        self.macro = None

        self.setWindowTitle('Add shortcut')
        layout = QVBoxLayout()

        lay1 = QHBoxLayout()
        self.short_input = QLineEdit()
        listen_btn = QPushButton('Listen')
        listen_btn.clicked.connect(self.listen)
        add_to(lay1, self.short_input, listen_btn)
        add_to(layout, lay1, is_layout=True)

        lay2 = QHBoxLayout()
        self.macro_check = QCheckBox()
        self.macro_check.setEnabled(False)
        lab = QLabel('Record macro:')
        self.start_macro = QPushButton('Start')
        self.start_macro.clicked.connect(self.start_record)
        self.stop_macro = QPushButton('Stop')
        self.stop_macro.setEnabled(False)
        self.stop_macro.clicked.connect(self.stop_record)

        add_to(lay2, self.macro_check, lab, self.start_macro, self.stop_macro)
        add_to(layout, lay2, is_layout=True)

        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(btn)
        button_box.accepted.connect(self.save_input)
        button_box.rejected.connect(self.reject)

        add_to(layout, button_box)

        self.setLayout(layout)

    def listen(self):
        hk = keyboard.read_hotkey()
        self.short_input.setText(hk)

    def save_input(self):
        inp = self.short_input.text()
        if inp and self.macro_check.isChecked():
            self.input = inp
            self.accept()

    @property
    def get_input(self):
        return self.input

    @property
    def get_macro(self):
        return self.macro

    def start_record(self):
        keyboard.start_recording()
        self.start_macro.setEnabled(False)
        self.stop_macro.setEnabled(True)

    def stop_record(self):
        mcr = keyboard.stop_recording()
        mcr.pop()
        self.macro = mcr
        self.macro_check.setChecked(True)
        self.start_macro.setEnabled(True)
        self.stop_macro.setEnabled(False)


class AddAbbre(QDialog):
    def __init__(self):
        super().__init__()

        self.short = None
        self.abbre = None

        self.setWindowTitle('Add Abbreviation')
        layout = QVBoxLayout()

        lay = QHBoxLayout()
        short_lab = QLabel('Short:')
        self.short_input = QLineEdit()
        add_to(lay, short_lab, self.short_input)
        add_to(layout, lay, is_layout=True)

        lay = QHBoxLayout()
        abbre_lab = QLabel('Replace with:')
        self.abbre_input = QLineEdit()
        add_to(lay, abbre_lab, self.abbre_input)
        add_to(layout, lay, is_layout=True)

        short_lab.setMinimumWidth(abbre_lab.sizeHint().width())

        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        button_box = QDialogButtonBox(btn)
        button_box.accepted.connect(self.save)
        button_box.rejected.connect(self.reject)
        add_to(layout, button_box)

        self.setLayout(layout)

    def save(self):
        srt = self.short_input.text()
        abr = self.abbre_input.text()

        if srt and abr:
            self.short = srt
            self.abbre = abr
            self.accept()

    @property
    def get_short(self):
        return self.short

    @property
    def get_abbre(self):
        return self.abbre


# For testing
if __name__ == '__main__':
    app = QApplication([])
    w = AddAbbre()
    w.show()
    app.exec()
