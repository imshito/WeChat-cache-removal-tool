﻿# -*- coding: utf-8 -*-

import os

from PyQt5 import QtCore, QtGui, QtWidgets
# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QMessageBox


def mk(self):

    os.system('tool.bat')
def mk2(self):
    os.system('help.txt')



def mk3(self):
    os.system('lingbaago.url')
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("WeChat cacheremoval tool V2.00")
        MainWindow.resize(237, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setToolTipDuration(1)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 237, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(mk)
        self.pushButton_2.clicked.connect(mk2)

        self.pushButton_3.clicked.connect(mk3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WeChat-cache-removal-tool"))
        self.label.setText(_translate("MainWindow", "微信缓存删除工具 作者：零捌啊狗"))
        self.pushButton.setText(_translate("MainWindow", "删除"))
        self.pushButton_2.setText(_translate("MainWindow", "帮助"))

        self.pushButton_3.setText(_translate("MainWindow", "关于"))
