from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import *
from PySide6.QtCore import Qt
from utils import isEmpty, isNumOrDot

def isNumOrDot(text: str) -> bool:
    return text.isdigit() or text == '.'

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range (4)] # top, right, bottom, left em um só for
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')    
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
            
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
            self.parent().buttonsGrid._eq()
        elif isNumOrDot(event.text()):
            self.insert(event.text())
        elif event.key() == Qt.Key.Key_Backspace:
            self.backspace()
        elif event.key() == Qt.Key.Key_Enter:
            self.parent().buttonsGrid._eq()
        elif event.key() == Qt.Key.Key_Delete:
            self.clear()
        else:
            # Ignora outras teclas
            if event.key() not in [Qt.Key.Key_Left, Qt.Key.Key_Right, Qt.Key.Key_Home, Qt.Key.Key_End]:
                return None
            
        if isNumOrDot(event.text()):
            self.insert(event.text())
        return super().keyPressEvent(event) if event.key() in ALLOWED_KEYS else None
    
        
    