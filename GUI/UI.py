import serial
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
import asyncio
from PySide6.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtSerialPort



wbl ='' 
wbr ='' 
wfl ='' 
wfr =''
temp ='' 
speed =''      
   

        
class Ui_CarDashBoard(object):
 
    def setupUi(self, CarDashBoard):
        if not CarDashBoard.objectName():
            CarDashBoard.setObjectName(u"CarDashBoard")
        CarDashBoard.resize(800, 480)
        CarDashBoard.setMinimumSize(QSize(800, 480))
        CarDashBoard.setMaximumSize(QSize(800, 480))
        self.centralwidget = QWidget(CarDashBoard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 800, 480))
        self.label.setMouseTracking(False)
        self.label.setAutoFillBackground(True)
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"./car-interface.jpg"))
        self.label = QLabel()
        
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 100, 171, 121))
        self.label_2.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 260, 171, 121))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(580, 100, 171, 121))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 250, 171, 121))
        self.label_5.setTabletTracking(False)
        self.label_5.setAcceptDrops(False)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 410, 101, 41))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 410, 81, 41))
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(580, 410, 61, 41))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(650, 415, 61, 31))
        
        CarDashBoard.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()

        self.retranslateUi(CarDashBoard)

        QMetaObject.connectSlotsByName(CarDashBoard)
        
        
        self.serial = QtSerialPort.QSerialPort(
            'COM10',
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.receive
        )
            
    @QtCore.pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            
            line = self.serial.readLine().data().decode('utf-8').rstrip()
            wbl,wbr,wfl,wfr = line.split(':')
            #line0 = line.split("temp",1)[1]
            #line1 = line.split("air",1)[1]
            #line2 = line.split("air2",1)[1]
           
            print(wbl)

    # setupUi

    
    def retranslateUi(self, CarDashBoard):
        
       
        

        CarDashBoard.setWindowTitle(QCoreApplication.translate("CarDashBoard", u"Car DashBoard", None))
        self.label_2.setText(QCoreApplication.translate("CarDashBoard", str(wfl), None))
        self.label_3.setText(QCoreApplication.translate("CarDashBoard", str(wbl), None))
        self.label_4.setText(QCoreApplication.translate("CarDashBoard", str(wfr), None))
        self.label_5.setText(QCoreApplication.translate("CarDashBoard", str(wbr), None))
        self.label_6.setText(QCoreApplication.translate("CarDashBoard", u"Temperature :", None))
        self.label_7.setText(QCoreApplication.translate("CarDashBoard", str(temp), None))
        self.label_8.setText(QCoreApplication.translate("CarDashBoard", u"Speed :", None))
        self.label_9.setText(QCoreApplication.translate("CarDashBoard", str(speed), None))
        self.label.setText("")
    # retranslateUi
    
class MainWindow(QMainWindow):
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.ui = Ui_CarDashBoard()
        self.ui.setupUi(self)
        
        
        
if __name__ == '__main__':

    app = QApplication(sys.argv) 
    window = MainWindow()
    window.show()
    
    
    sys.exit(app.exec_())