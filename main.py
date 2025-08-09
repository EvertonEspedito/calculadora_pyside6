import sys

from main_window import MainWindow
from display import Display
from info import Info
from buttons import ButtonsGrid


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
    info = Info("0")
    window.addWidgetToVLayout(info)
    

    # Display
    display = Display()
    display.setPlaceholderText("Digite aqui...")
    window.addWidgetToVLayout(display)

    #Grid 
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()