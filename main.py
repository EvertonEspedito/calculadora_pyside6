from main_window import MainWindow 
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout,QLabel
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()

    app.exec()