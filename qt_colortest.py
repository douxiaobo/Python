import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog, QLabel, QTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette, QBrush

app=QApplication(sys.argv)
w=QWidget()
w.setGeometry(260,240,300,200)
w.setWindowTitle("Color Test")
palette=QPalette()
palette.setColor(QPalette.ColorRole.Window,Qt.GlobalColor.red)
lb=QLabel("This is a label",w)
lb.move(100,20)
lb.resize(100,20)
lb.setAutoFillBackground(True)
lb.setPalette(palette)
color=QColor(10,50,255)
te=QTextEdit(w)
te.move(100,60)
te.resize(100,20)
te.setTextColor(color)
te.setText("This is a text")
w.show()
app.exec()