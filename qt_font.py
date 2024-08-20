import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
app=QApplication(sys.argv)
w=QWidget()
w.setGeometry(260,240,300,200)
w.setWindowTitle("字体测试")
lb=QLabel("Hello World!",w)
lb.move(60,20)
lb.resize(160,30)
font=QFont()
font.setPointSize(16)
font.setFamily("Arial")
font.setBold(True)
lb.setFont(font)
#lb.setFont(QFont('Times',14))
w.show()
app.exec()