import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QEvent

class myWidget(QWidget):
    def __init__(self,parent=None)->None:
        super().__init__(parent)
        self.resize(400,300)
        self.setWindowTitle("Event Filter")

        self.lb1=QLabel(self)
        self.lb1.setGeometry(20,20,300,60)
        self.lb1.setText("This is a label")
        font=self.lb1.font()
        font.setPointSize(16)
        font.setBold(True)
        self.lb1.setFont(font)
        self.lb1.installEventFilter(self)

        self.lb2=QLabel(self)
        self.lb2.setGeometry(20,100,300,60)
        self.lb2.setText('This is another label')
        self.lb2.setFont(font)
        self.lb2.installEventFilter(self)

    def eventFilter(self,lb,event)->bool:
        if lb==self.lb1:
            if event.type()==QEvent.Type.Enter:
                self.lb1.setStyleSheet(\
                    'background-color:rgb(170,255,255);')
            if event.type()==QEvent.Type.Leave:
                self.lb1.setStyleSheet('')
        if lb==self.lb2:
            if event.type()==QEvent.Type.Enter:
                self.lb2.setStyleSheet(\
                    'background-color:rgb(255,0,0);')
            if event.type()==QEvent.Type.MouseButtonPress:
                self.lb2.setStyleSheet(\
                    'background-color:rgb(0,255,0);')
            if event.type()==QEvent.Type.MouseButtonRelease:
                self.lb2.setStyleSheet(\
                    'background-color:rgb(0,0,255);')
            if event.type()==QEvent.Type.Leave:
                self.lb2.setStyleSheet('')
        return super().eventFilter(lb,event)

app=QApplication(sys.argv)
w=myWidget()
w.show()
sys.exit(app.exec())