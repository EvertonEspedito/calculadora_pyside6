from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton
from utils import isEmpty, isNumOrDot, isValidNumber
from variables import MEDIUM_FONT_SIZE

if TYPE_CHECKING:
    from main_window import MainWindow
    from display import Display
    from info import Info


#CLASSES
class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):   
    def __init__(self, display: 'Display',info: 'Info', window: 'MainWindow',*args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = '0'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()
        

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if not isNumOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot( self._insertButtonTextToDisplay, button)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect( slot )

    def _configSpecialButton(self, button):
        text = button.text()
        if text == 'C':
           self._connectButtonClicked(button, self._clear)

        if text in 'D':
           self._connectButtonClicked(button, self.display.backspace)

        if text in '+-/*^':
           self._connectButtonClicked(
               button, 
               self._makeSlot(self._operatorClicked, button)
            )

        if text in '=':
           self._connectButtonClicked(button, self._eq)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self,button):
        buttonText = button.text()
        newDisplayValue = self.display.text() + buttonText

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(buttonText)

    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()

    def _operatorClicked(self, button):
        buttonText = button.text() # pega o texto do botão +-/*
        displayText = self.display.text()# pega o texto do display da esquerda 
        self.display.clear() # limpa o display

        # Verifica se o display está vazio ou se o texto é inválido
        if not isValidNumber(displayText) and self._left is None:
            self._showError("Entrada inválida, por favor, digite um número.")
            return
        # Se o display estiver vazio, não faz nada
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText # armazena o operador
        self.equation = f'{self._left} {self._op} ??' # atualiza a equação na info

    def _eq(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            self._showError("Entrada inválida, por favor, digite um número.")
            return
        
        self._right = float(displayText) # armazena o número da direita
        self.equation = f'{self._left} {self._op} {self._right}' # atualiza a equação na info
        result = 'Error'
        try:
            if '^' in self.equation:
                base, exponent = self.equation.split('^')
                result = float(base) ** float(exponent)
            else:
                result = eval(self.equation) # evalua a equação
        except ZeroDivisionError:
            self._showError("Erro: Divisão por zero.")
        except OverflowError:
            self._showError("Erro: Resultado muito grande.")
        except Exception as e:
            self._showError(f"Erro ao calcular a equação: {e}")
            return

        self.display.clear() # limpa o display
        self.info.setText(f'{self.equation} = {result}') # atualiza a info com o resultado
        self._left = result # armazena o resultado como o novo número da esquerda
        self._right = None # limpa o número da direita             

        if result == 'Error':
             self._left = None
             
    def _showError(self, message):
        msgBox = self.window.makeMsgBox("Erro", message)
        msgBox.setText(message)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()