# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                       PRIMARY_COLOR)

qss = f"""
    QPushButton[cssClass="specialButton"]  {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""

def setupTheme(app=None):
    # Recebe QApplication como argumento
    if app is not None:
        app.setStyleSheet(qss)