from PyQt6.QtWidgets import *
import sys
class myWidget(QWidget):
    def __init__(self):
        super(myWidget, self).__init__()
        self.setWindowTitle("Style Sheet")
        pb1=QPushButton("Button 1")
        pb2=QPushButton("Button 2")
        pb3=QPushButton("Button 3")
        lb=QLabel("Label")
        vLay=QVBoxLayout()
        vLay.addWidget(pb1)
        vLay.addWidget(pb2)
        vLay.addWidget(pb3)
        vLay.addWidget(lb)
        self.setLayout(vLay)
        self.setStyleSheet("color:rgb(20,20,255);font-size:24px;font-weight:bold;font-family:Courier New;")

if __name__=="__main__":
    app=QApplication(sys.argv)
    pbSytle="""
    QPushButton{
        background-color:red;
        fireground-color:blue;
        font-family:Arial;
        font-size:18px;
    }
    """
    w=myWidget()
    w.setStyleSheet(pbSytle)
    w.show()
    sys.exit(app.exec())