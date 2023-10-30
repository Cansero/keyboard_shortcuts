from random import randint

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QGroupBox, QApplication, QMenu, \
    QSystemTrayIcon

from test2 import add_to
from utils import *


class Win(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shortcuts and Abbreviations')

        self.shortcuts, self.abbreviations = load_file('config.json')

        self.short_grb = QGroupBox('Shortcuts')
        self.short_grb_lay = QVBoxLayout()
        self.short_grb_lay.setAlignment(Qt.AlignTop)
        self.short_grb.setLayout(self.short_grb_lay)
        self.addShort = QPushButton('Add new shortcut')
        add_to(self.short_grb_lay, self.addShort)

        self.shorts = {}
        self.make_shortcuts_menu()

        self.abbre_grb = QGroupBox('Abbreviations')
        self.abbre_grb_lay = QVBoxLayout()
        self.abbre_grb_lay.setAlignment(Qt.AlignTop)
        self.abbre_grb.setLayout(self.abbre_grb_lay)
        self.addAbbre = QPushButton('Add new abbreviation')
        add_to(self.abbre_grb_lay, self.addAbbre)

        self.abbre = {}
        self.make_abbre_menu()

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon_menu = QMenu(self)
        self.opt_show = QAction()
        self.opt_quit = QAction()
        self.make_tray_menu()

        icon = QIcon('systray/images/heart.png')
        self.tray_icon.setIcon(icon)
        self.setWindowIcon(icon)
        self.tray_icon.show()

        layout = QVBoxLayout()
        add_to(layout, self.short_grb, self.abbre_grb)
        self.setLayout(layout)

    def make_shortcuts_menu(self):
        n = randint(0, 10000)
        for key, handler in self.shortcuts.items():
            lay = QHBoxLayout()
            lab = QLabel(key)
            btn = QPushButton('Remove')
            btn.clicked.connect(lambda: self.rmv_short(n))
            add_to(lay, lab, btn)
            add_to(self.short_grb_lay, lay, is_layout=True)
            self.shorts[n] = [handler, lay, [lab, btn]]

    def make_abbre_menu(self):
        n = randint(0, 10000)
        for key, abbre in self.abbre.items():
            lay = QHBoxLayout()
            lab = QLabel(key)
            lab2 = QLabel(abbre)
            btn = QPushButton('Remove')
            btn.clicked.connect(lambda: self.rmv_abbre(n))
            add_to(lay, lab, lab2, btn)
            add_to(self.abbre_grb_lay, lay, is_layout=True)
            self.abbre[n] = [key, lay, [lab, lab2, btn]]

    def rmv_short(self, index):
        rmv = self.shorts.pop(index)
        keyboard.remove_hotkey(rmv[0])
        self.short_grb_lay.removeItem(rmv[1])
        for item in rmv[2]:
            item.hide()

    def rmv_abbre(self, index):
        rmv = self.abbre.pop(index)
        keyboard.remove_abbreviation(rmv[0])
        self.abbre_grb_lay.removeItem(rmv[1])
        for item in rmv[2]:
            item.hide()

    def make_tray_menu(self):
        self.opt_show = QAction('Restore', self)
        self.opt_show.triggered.connect(self.showNormal)
        self.opt_quit = QAction('Quit', self)
        self.opt_quit.triggered.connect(qApp.quit)

        self.tray_icon_menu.addAction(self.opt_show)
        self.tray_icon_menu.addSeparator()
        self.tray_icon_menu.addAction(self.opt_quit)

        self.tray_icon.setContextMenu(self.tray_icon_menu)


if __name__ == '__main__':
    app = QApplication([])
    QApplication.setQuitOnLastWindowClosed(False)
    w = Win()
    w.show()
    app.exec()
