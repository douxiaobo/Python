from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QDialog, QPushButton

import sys

class CircleCal(QDialog):
    def __init__(self):
        super().__init__()  # 初始化函数
        self.initUi()

    def initUi(self):
        QLabel('半径=',self).setGeometry(80,40,71,21)   # 控件大小 width=71,height=21
        self.leRadius=QLineEdit(self)
        self.leRadius.setGeometry(140,40,113,21)
        self.leRadius.returnPressed.connect(self.calculate)

        QLabel('周长=',self).setGeometry(80,80,71,21)
        self.leLength=QLineEdit(self)
        self.leLength.setGeometry(140,80,113,21)
        self.leLength.setEnabled(False)

        QLabel('面积=',self).setGeometry(80,120,71,21)
        self.leArea=QLineEdit(self)
        self.leArea.setGeometry(140,120,113,21)
        self.leArea.setEnabled(False)

        self.pbCal=QPushButton('计算',self)
        self.pbCal.setGeometry(140,160,93,28)
        self.pbCal.clicked.connect(self.calculate)

        self.resize(350,200)
        self.move(300,300)
        self.setWindowTitle('计算圆的周长和面积')

    def calculate(self):
        try:
            r=float(self.leRadius.text())
            if r>=0:
                length=2*3.14159*r
                area=3.14159*r*r
                self.leLength.setText(str(length))
                self.leArea.setText(str(area))
        except:
            QMessageBox.warning(self,'错误','请输入数字！')
    
app=QApplication(sys.argv)
dlg=CircleCal()
dlg.show()
sys.exit(app.exec())


# Last login: Wed Jun 26 19:55:18 on ttys000
# douxiaobo@192 Python % code .
# douxiaobo@192 Python % python3 pyqt_calculate_area_of_circle.py
# Traceback (most recent call last):
#   File "/Users/douxiaobo/Documents/Practice in Coding/Python/pyqt_calculate_area_of_circle.py", line 1, in <module>
#     from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QDialog, QQPushButton
# ImportError: cannot import name 'QQPushButton' from 'PyQt6.QtWidgets' (/opt/homebrew/lib/python3.12/site-packages/PyQt6/QtWidgets.abi3.so). Did you mean: 'QPushButton'?
# douxiaobo@192 Python % python3 pyqt_calculate_area_of_circle.py
# 2024-06-26 20:30:35.262 Python[6185:249098] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit
# douxiaobo@192 Python % python3 pyqt_calculate_area_of_circle.py
# 2024-06-26 20:31:01.163 Python[6194:249562] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit
# douxiaobo@192 Python % python3 pyqt_calculate_area_of_circle.py
# 2024-06-26 20:32:02.994 Python[6207:250462] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit
# douxiaobo@192 Python %        