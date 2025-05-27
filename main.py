import sys

from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display()
    window.addToVLayout(display)# 3:20

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()