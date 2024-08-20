from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt,QEvent
from PyQt6.QtWidgets import QWidget
import sys

class myLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(myLabel, self).__init__(parent)
        font=QFont("楷体",16)
        self.setFont(font)
    def mousePressEvent(self,event):
        if event.buttons()==Qt.MouseButton.LeftButton:
            self.setText("鼠标左键按下")
        elif event.buttons()==Qt.MouseButton.RightButton:
            self.setText("鼠标右键按下")
        elif event.buttons()==Qt.MouseButton.MiddleButton:
            self.setText("鼠标中键按下")
        elif event.buttons()==Qt.MouseButton.LeftButton | \
        Qt.MouseButton.RightButton:
            self.setText("鼠标左右键同时按下")
    def wheelEvent(self,event):
        angle=event.angleDelta()/8
        angleX=angle.x()
        angleY=angle.y()
        if angleY>0:
            self.setText("滚轮向上")
            print("滚轮向上")
        else:
            self.setText("滚轮向下")
            print("滚轮向下")
    def mouseDoubleClickEvent(self,event):
        self.setText("鼠标双击")
        print("鼠标双击")
    def mouseReleaseEvent(self,event):
        self.setText("鼠标按键释放")
        print("鼠标按键释放")
class myWidget(QtWidgets.QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        self.setWindowTitle('事件测试')
        self.resize(300,120)
        self.lb=myLabel(self)
        self.lb.setText("--------------")
        self.lb.setGeometry(60,40,160,50)
    def mouseMoveEvent(self,event):
        print("鼠标移动",self.x(),self.y())
    def resizeEvent(self, event):
        message = "窗口大小调整为：QSize({0},{1})".format(event.size().width(), event.size().height())
        print(message)
    def keyPressEvent(self,event):
        print('Key')
        if event.key()==Qt.Key.Key_Escape:
            self.close()
    def event(self,event):
        if (event.type()==QEvent.Type.KeyPress and event.key() == \
        Qt.Key.Key_Q):
            print("A Key")
            self.close()
            return True
        return QWidget.event(self,event)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w=myWidget()
    w.show()
    sys.exit(app.exec())