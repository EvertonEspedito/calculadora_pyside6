import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 150px;')
    window.vLayout.addWidget(label1)
    window.adjustFixedSize()
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()