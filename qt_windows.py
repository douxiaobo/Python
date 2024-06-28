import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt

app=QApplication(sys.argv)
w=QWidget()
w.setGeometry(100,100,500,500)
w.setWindowTitle("Hello World")
w.show()
print(w.x(), w.y(), w.width(), w.height())
print(w.pos(),w.size())
print(w.geometry())
sys.exit(app.exec())

# Last login: Fri Jun 28 21:05:31 on ttys002
# douxiaobo@192 Python % code .
# douxiaobo@192 Python % python3 qt_windows.py
# 100 72 500 500
# PyQt6.QtCore.QPoint(100, 72) PyQt6.QtCore.QSize(500, 500)
# PyQt6.QtCore.QRect(100, 100, 500, 500)
# douxiaobo@192 Python % 
