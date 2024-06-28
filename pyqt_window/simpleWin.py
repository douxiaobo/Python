from PyQt6.QtWidgets import QApplication, QWidget,QPushButton
import sys

def btnfunc():
    pass

app = QApplication(sys.argv)
window = QWidget()
window.resize(300,200)
window.move(260,240)
window.setWindowTitle("Simple Window")

btn=QPushButton(window)
btn.setText("Click me")
btn.move(120,150)
btn.clicked.connect(btnfunc)

window.show()
sys.exit(app.exec())

# Last login: Mon Jun 24 14:19:02 on ttys000
# douxiaobo@192 pyqt_window % code .
# douxiaobo@192 pyqt_window % python3 simpleWin.py
# douxiaobo@192 pyqt_window % 

