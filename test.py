import threading

from PySide6.QtCore import QSize
from infi.systray import SysTrayIcon
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication, QDialogButtonBox, QMainWindow, QWidget, \
    QPushButton

from time import sleep


class Message(QMainWindow):
    def __init__(self):
        super(Message, self).__init__()

        self.tray = None
        self.isclosed = False

        self.setWindowTitle('test')
        self.label = QLabel('Hola')
        self.button = QPushButton('Hide')
        self.button.clicked.connect(self.toggle_show)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def closeEvent(self, event):
        self.isclosed = True
        self.finish()
        event.accept()

    def toggle_show(self):
        self.hide()

    def set_tray(self, handler):
        self.tray = handler

    def finish(self):
        if self.tray.is_active():
            thread = threading.Thread(target=terminate, args=[self.tray])
            thread.start()

    def is_closed(self):
        return self.isclosed


def win_exec(win):
    if win.isHidden():
        win.show()
    else:
        win.hide()


def close_win(win):
    if not win.is_closed():
        win.close()


def terminate(handler):
    sleep(1)
    handler.shutdown()


if __name__ == '__main__':
    app = QApplication([])
    x = Message()
    menu_options = (('Test', None, win_exec, (x,)), ('Quit', None, close_win, (x,)))
    systray = SysTrayIcon('icon.ico', 'None', menu_options)
    x.set_tray(systray)
    systray.start()
    x.show()
    app.exec()
