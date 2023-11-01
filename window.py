from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QGroupBox, QMenu, QSystemTrayIcon
)

from win_util import *
from utils import *


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shortcuts and Abbreviations')

        self.file = 'config.json'
        self.options = load_file(self.file)

        self.short_grb = QGroupBox('Shortcuts')
        self.short_grb_lay = QVBoxLayout()
        self.short_grb_lay.setAlignment(Qt.AlignTop)
        self.short_grb.setLayout(self.short_grb_lay)
        self.add_short = QPushButton('Add new shortcut')
        self.add_short.clicked.connect(self.add_shortcut)
        add_to(self.short_grb_lay, self.add_short)

        self.shorts = {}
        self.make_short_menu()

        self.abbre_grb = QGroupBox('Abbreviations')
        self.abbre_grb_lay = QVBoxLayout()
        self.abbre_grb_lay.setAlignment(Qt.AlignTop)
        self.abbre_grb.setLayout(self.abbre_grb_lay)
        self.addAbbre = QPushButton('Add new abbreviation')
        self.addAbbre.clicked.connect(self.add_abbreviation)
        add_to(self.abbre_grb_lay, self.addAbbre)

        self.abbres = {}
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

    def make_short_menu(self):
        for short, macro in self.options['Shortcut'].items():
            events = []
            for event in macro:
                events.append(json_to_event(json.loads(event)))
            self.options['Shortcut'][short] = events
            handler = keyboard.add_hotkey(short, play_macro, (events,))
            self.add_short_to_menu(short, handler, do_save=False)

    def make_abbre_menu(self):
        for short, abbre in self.options['Abbreviation'].items():
            keyboard.add_abbreviation(short, abbre)
            self.add_abbre_to_menu(short, abbre, do_save=False)

    def add_shortcut(self):
        x = AddShort()
        if x.exec():
            inp = x.get_input
            macro = x.get_macro
            handler = keyboard.add_hotkey(inp, play_macro, (macro,))
            self.options['Shortcut'][inp] = macro
            self.add_short_to_menu(inp, handler)

    def add_abbreviation(self):
        x = AddAbbre()
        if x.exec():
            short = x.get_short
            abbre = x.get_abbre
            keyboard.add_abbreviation(short, abbre)
            self.options['Abbreviation'][short] = abbre
            self.add_abbre_to_menu(short, abbre)

    def add_short_to_menu(self, inp, handler, do_save=True):
        lay = QHBoxLayout()
        lab = QLabel(inp)
        btn = QPushButton('Remove')
        btn.clicked.connect(lambda: self.rmv_short(inp))
        add_to(lay, lab, btn)
        add_to(self.short_grb_lay, lay, is_layout=True)
        self.shorts[inp] = [handler, lay, [lab, btn]]

        if do_save:
            self.save()

    def add_abbre_to_menu(self, short, abbre, do_save=True):
        lay = QHBoxLayout()
        lab = QLabel(short + ':')
        abb = QLabel(abbre)
        btn = QPushButton('Remove')
        btn.clicked.connect(lambda: self.rmv_abbre(short))
        add_to(lay, lab, abb, btn)
        add_to(self.abbre_grb_lay, lay, is_layout=True)
        self.abbres[short] = [lay, [lab, abb, btn]]

        if do_save:
            self.save()

    def rmv_short(self, i):
        self.options['Shortcut'].pop(i)
        rmv = self.shorts.pop(i)
        keyboard.remove_hotkey(rmv[0])
        self.short_grb_lay.removeItem(rmv[1])
        for item in rmv[2]:
            item.hide()

        self.save()

    def rmv_abbre(self, i):
        self.options['Abbreviation'].pop(i)
        rmv = self.abbres.pop(i)
        keyboard.remove_abbreviation(i)
        self.abbre_grb_lay.removeItem(rmv[0])
        for item in rmv[1]:
            item.hide()

        self.save()

    def make_tray_menu(self):
        self.opt_show = QAction('Restore', self)
        self.opt_show.triggered.connect(self.showNormal)
        self.opt_quit = QAction('Quit', self)
        self.opt_quit.triggered.connect(self.quit)

        self.tray_icon_menu.addAction(self.opt_show)
        self.tray_icon_menu.addSeparator()
        self.tray_icon_menu.addAction(self.opt_quit)

        self.tray_icon.setContextMenu(self.tray_icon_menu)

    def save(self):
        save_file(self.file, self.options)

    def quit(self):
        if self.shorts or self.abbres:
            keyboard.remove_all_hotkeys()
        qApp.quit()
