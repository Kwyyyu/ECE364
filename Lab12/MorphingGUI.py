# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MorphingGUI.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_ending = QtWidgets.QLabel(self.centralwidget)
        self.label_ending.setGeometry(QtCore.QRect(450, 260, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ending.setFont(font)
        self.label_ending.setObjectName("label_ending")
        self.tbsStart = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbsStart.setGeometry(QtCore.QRect(20, 40, 288, 216))
        self.tbsStart.setObjectName("tbsStart")
        self.lineEdit_alpha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_alpha.setGeometry(QtCore.QRect(600, 300, 51, 27))
        self.lineEdit_alpha.setObjectName("lineEdit_alpha")
        self.tbsResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbsResult.setGeometry(QtCore.QRect(190, 330, 288, 216))
        self.tbsResult.setObjectName("tbsResult")
        self.Slider = QtWidgets.QSlider(self.centralwidget)
        self.Slider.setGeometry(QtCore.QRect(70, 300, 521, 20))
        self.Slider.setMouseTracking(True)
        self.Slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Slider.setObjectName("Slider")
        self.tbsEnding = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbsEnding.setGeometry(QtCore.QRect(360, 40, 288, 216))
        self.tbsEnding.setObjectName("tbsEnding")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(570, 320, 31, 17))
        self.label_1.setObjectName("label_1")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(20, 10, 161, 27))
        self.btnStart.setObjectName("btnStart")
        self.label_start = QtWidgets.QLabel(self.centralwidget)
        self.label_start.setGeometry(QtCore.QRect(100, 260, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_start.setFont(font)
        self.label_start.setObjectName("label_start")
        self.chbShow = QtWidgets.QCheckBox(self.centralwidget)
        self.chbShow.setGeometry(QtCore.QRect(270, 270, 131, 22))
        self.chbShow.setObjectName("chbShow")
        self.label_alpha = QtWidgets.QLabel(self.centralwidget)
        self.label_alpha.setGeometry(QtCore.QRect(20, 300, 62, 17))
        self.label_alpha.setObjectName("label_alpha")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(70, 320, 31, 17))
        self.label_0.setObjectName("label_0")
        self.btnEnding = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnding.setGeometry(QtCore.QRect(360, 10, 161, 27))
        self.btnEnding.setObjectName("btnEnding")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(280, 550, 121, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.btnBlend = QtWidgets.QPushButton(self.centralwidget)
        self.btnBlend.setGeometry(QtCore.QRect(290, 580, 92, 27))
        self.btnBlend.setObjectName("btnBlend")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_ending.setText(_translate("MainWindow", "Ending Image"))
        self.label_1.setText(_translate("MainWindow", "1.0"))
        self.btnStart.setText(_translate("MainWindow", "Load Starting Image ..."))
        self.label_start.setText(_translate("MainWindow", "Starting Image"))
        self.chbShow.setText(_translate("MainWindow", "Show Triangles"))
        self.label_alpha.setText(_translate("MainWindow", "Alpha"))
        self.label_0.setText(_translate("MainWindow", "0.0"))
        self.btnEnding.setText(_translate("MainWindow", "Load Ending Image ..."))
        self.label_result.setText(_translate("MainWindow", "Blending Result"))
        self.btnBlend.setText(_translate("MainWindow", "Blend"))

