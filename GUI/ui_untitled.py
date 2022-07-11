# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledsUOdal.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_CarDashBoard(object):
    def setupUi(self, CarDashBoard):
        if not CarDashBoard.objectName():
        CarDashBoard.setObjectName(u"CarDashBoard")
        CarDashBoard.resize(800, 480)
        CarDashBoard.setMinimumSize(QSize(800, 480))
        CarDashBoard.setMaximumSize(QSize(800, 480))
        self.centralwidget = QWidget(CarDashBoard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 110, 151, 101))
        self.label_2.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 260, 171, 111))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(570, 100, 171, 111))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(570, 260, 171, 111))
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

        self.retranslateUi(CarDashBoard)

        QMetaObject.connectSlotsByName(CarDashBoard)
    # setupUi

    def retranslateUi(self, CarDashBoard):
        CarDashBoard.setWindowTitle(QCoreApplication.translate("CarDashBoard", u"Car DashBoard", None))
        self.label_2.setText(QCoreApplication.translate("CarDashBoard", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("CarDashBoard", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("CarDashBoard", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("CarDashBoard", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("CarDashBoard", u"Temperature :", None))
        self.label_7.setText(QCoreApplication.translate("CarDashBoard", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("CarDashBoard", u"Speed :", None))
        self.label_9.setText(QCoreApplication.translate("CarDashBoard", u"TextLabel", None))
    # retranslateUi

