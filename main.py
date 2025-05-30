import sys

from main_window import MainWindow
from display import Display
from info import Info
from styles import setupTheme
from PySide6.QtWidgets import QApplication, QLineEdit
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info("2.0 ^ 10.0 = 1024.0")
    window.addToVLayout(info)
    

    # Display
    display = Display()
    display.setPlaceholderText("Digite aqui...")
    window.addToVLayout(display)


    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()