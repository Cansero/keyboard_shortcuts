from PySide6.QtWidgets import QApplication
from window import Window

if __name__ == '__main__':
    app = QApplication([])
    QApplication.setQuitOnLastWindowClosed(True)  # Changer to False when ready
    w = Window()
    w.show()
    app.exec()
