from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal
 

class MyQLabel(QLabel):
    clicked = Signal()

    def __int__(self):
        super(MyQLabel, self).__init__()
 
    def mousePressEvent(self, e):
        print("Mouse clicked")
        self.clicked.emit()
 
    def leaveEvent(self, e):
        print("Mouse moves out logo")
    
    def enterEvent(self, e):
        print("Mouse moves in logo")