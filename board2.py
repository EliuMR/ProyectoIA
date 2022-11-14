# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 649)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.casilla = QtWidgets.QPushButton(self.centralwidget)
        self.casilla.setGeometry(QtCore.QRect(90, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla.setFont(font)
        self.casilla.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla.setObjectName("casilla")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 542, 146, 10))
        self.label_5.setStyleSheet("background-color:white\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(413, 542, 146, 10))
        self.label_7.setStyleSheet("background-color:white\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.Inicio = QtWidgets.QPushButton(self.centralwidget)
        self.Inicio.setGeometry(QtCore.QRect(480, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(15)
        self.Inicio.setFont(font)
        self.Inicio.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Inicio.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color:white")
        self.Inicio.setObjectName("Inicio")
        self.labelwin = QtWidgets.QLabel(self.centralwidget)
        self.labelwin.setGeometry(QtCore.QRect(80, 560, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.labelwin.setFont(font)
        self.labelwin.setStyleSheet("color:rgb(0, 0, 0)")
        self.labelwin.setText("")
        self.labelwin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelwin.setObjectName("labelwin")
        self.Tittle = QtWidgets.QLabel(self.centralwidget)
        self.Tittle.setGeometry(QtCore.QRect(90, 0, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Tittle.setFont(font)
        self.Tittle.setStyleSheet("")
        self.Tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.Tittle.setObjectName("Tittle")
        self.casilla_2 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_2.setGeometry(QtCore.QRect(140, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_2.setFont(font)
        self.casilla_2.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_2.setObjectName("casilla_2")
        self.casilla_3 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_3.setGeometry(QtCore.QRect(190, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_3.setFont(font)
        self.casilla_3.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_3.setObjectName("casilla_3")
        self.casilla_4 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_4.setGeometry(QtCore.QRect(90, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_4.setFont(font)
        self.casilla_4.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_4.setObjectName("casilla_4")
        self.casilla_5 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_5.setGeometry(QtCore.QRect(140, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_5.setFont(font)
        self.casilla_5.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_5.setObjectName("casilla_5")
        self.casilla_6 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_6.setGeometry(QtCore.QRect(190, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_6.setFont(font)
        self.casilla_6.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_6.setObjectName("casilla_6")
        self.casilla_7 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_7.setGeometry(QtCore.QRect(90, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_7.setFont(font)
        self.casilla_7.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_7.setObjectName("casilla_7")
        self.casilla_8 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_8.setGeometry(QtCore.QRect(140, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_8.setFont(font)
        self.casilla_8.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_8.setObjectName("casilla_8")
        self.casilla_9 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_9.setGeometry(QtCore.QRect(190, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_9.setFont(font)
        self.casilla_9.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_9.setObjectName("casilla_9")
        self.casilla_10 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_10.setGeometry(QtCore.QRect(250, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_10.setFont(font)
        self.casilla_10.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_10.setObjectName("casilla_10")
        self.casilla_11 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_11.setGeometry(QtCore.QRect(300, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_11.setFont(font)
        self.casilla_11.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_11.setObjectName("casilla_11")
        self.casilla_12 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_12.setGeometry(QtCore.QRect(350, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_12.setFont(font)
        self.casilla_12.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_12.setObjectName("casilla_12")
        self.casilla_13 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_13.setGeometry(QtCore.QRect(250, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_13.setFont(font)
        self.casilla_13.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_13.setObjectName("casilla_13")
        self.casilla_14 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_14.setGeometry(QtCore.QRect(300, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_14.setFont(font)
        self.casilla_14.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_14.setObjectName("casilla_14")
        self.casilla_15 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_15.setGeometry(QtCore.QRect(350, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_15.setFont(font)
        self.casilla_15.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_15.setObjectName("casilla_15")
        self.casilla_16 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_16.setGeometry(QtCore.QRect(250, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_16.setFont(font)
        self.casilla_16.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_16.setObjectName("casilla_16")
        self.casilla_17 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_17.setGeometry(QtCore.QRect(300, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_17.setFont(font)
        self.casilla_17.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_17.setObjectName("casilla_17")
        self.casilla_18 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_18.setGeometry(QtCore.QRect(350, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_18.setFont(font)
        self.casilla_18.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_18.setObjectName("casilla_18")
        self.casilla_19 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_19.setGeometry(QtCore.QRect(410, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_19.setFont(font)
        self.casilla_19.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_19.setObjectName("casilla_19")
        self.casilla_20 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_20.setGeometry(QtCore.QRect(460, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_20.setFont(font)
        self.casilla_20.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_20.setObjectName("casilla_20")
        self.casilla_21 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_21.setGeometry(QtCore.QRect(510, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_21.setFont(font)
        self.casilla_21.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_21.setObjectName("casilla_21")
        self.casilla_22 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_22.setGeometry(QtCore.QRect(410, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_22.setFont(font)
        self.casilla_22.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_22.setObjectName("casilla_22")
        self.casilla_23 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_23.setGeometry(QtCore.QRect(460, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_23.setFont(font)
        self.casilla_23.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_23.setObjectName("casilla_23")
        self.casilla_24 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_24.setGeometry(QtCore.QRect(510, 120, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_24.setFont(font)
        self.casilla_24.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_24.setObjectName("casilla_24")
        self.casilla_25 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_25.setGeometry(QtCore.QRect(410, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_25.setFont(font)
        self.casilla_25.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_25.setObjectName("casilla_25")
        self.casilla_26 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_26.setGeometry(QtCore.QRect(460, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_26.setFont(font)
        self.casilla_26.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_26.setObjectName("casilla_26")
        self.casilla_27 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_27.setGeometry(QtCore.QRect(510, 170, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_27.setFont(font)
        self.casilla_27.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_27.setObjectName("casilla_27")
        self.casilla_28 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_28.setGeometry(QtCore.QRect(90, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_28.setFont(font)
        self.casilla_28.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_28.setObjectName("casilla_28")
        self.casilla_29 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_29.setGeometry(QtCore.QRect(140, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_29.setFont(font)
        self.casilla_29.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_29.setObjectName("casilla_29")
        self.casilla_30 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_30.setGeometry(QtCore.QRect(190, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_30.setFont(font)
        self.casilla_30.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_30.setObjectName("casilla_30")
        self.casilla_31 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_31.setGeometry(QtCore.QRect(90, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_31.setFont(font)
        self.casilla_31.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_31.setObjectName("casilla_31")
        self.casilla_32 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_32.setGeometry(QtCore.QRect(140, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_32.setFont(font)
        self.casilla_32.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_32.setObjectName("casilla_32")
        self.casilla_33 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_33.setGeometry(QtCore.QRect(190, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_33.setFont(font)
        self.casilla_33.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_33.setObjectName("casilla_33")
        self.casilla_34 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_34.setGeometry(QtCore.QRect(90, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_34.setFont(font)
        self.casilla_34.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_34.setObjectName("casilla_34")
        self.casilla_35 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_35.setGeometry(QtCore.QRect(140, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_35.setFont(font)
        self.casilla_35.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_35.setObjectName("casilla_35")
        self.casilla_36 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_36.setGeometry(QtCore.QRect(190, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_36.setFont(font)
        self.casilla_36.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_36.setObjectName("casilla_36")
        self.casilla_37 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_37.setGeometry(QtCore.QRect(250, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_37.setFont(font)
        self.casilla_37.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_37.setObjectName("casilla_37")
        self.casilla_38 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_38.setGeometry(QtCore.QRect(300, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_38.setFont(font)
        self.casilla_38.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_38.setObjectName("casilla_38")
        self.casilla_39 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_39.setGeometry(QtCore.QRect(350, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_39.setFont(font)
        self.casilla_39.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_39.setObjectName("casilla_39")
        self.casilla_40 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_40.setGeometry(QtCore.QRect(250, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_40.setFont(font)
        self.casilla_40.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_40.setObjectName("casilla_40")
        self.casilla_41 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_41.setGeometry(QtCore.QRect(300, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_41.setFont(font)
        self.casilla_41.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_41.setObjectName("casilla_41")
        self.casilla_42 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_42.setGeometry(QtCore.QRect(350, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_42.setFont(font)
        self.casilla_42.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_42.setObjectName("casilla_42")
        self.casilla_43 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_43.setGeometry(QtCore.QRect(250, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_43.setFont(font)
        self.casilla_43.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_43.setObjectName("casilla_43")
        self.casilla_44 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_44.setGeometry(QtCore.QRect(300, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_44.setFont(font)
        self.casilla_44.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_44.setObjectName("casilla_44")
        self.casilla_45 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_45.setGeometry(QtCore.QRect(350, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_45.setFont(font)
        self.casilla_45.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_45.setObjectName("casilla_45")
        self.casilla_46 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_46.setGeometry(QtCore.QRect(410, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_46.setFont(font)
        self.casilla_46.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_46.setObjectName("casilla_46")
        self.casilla_47 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_47.setGeometry(QtCore.QRect(460, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_47.setFont(font)
        self.casilla_47.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_47.setObjectName("casilla_47")
        self.casilla_48 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_48.setGeometry(QtCore.QRect(510, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_48.setFont(font)
        self.casilla_48.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_48.setObjectName("casilla_48")
        self.casilla_49 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_49.setGeometry(QtCore.QRect(410, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_49.setFont(font)
        self.casilla_49.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_49.setObjectName("casilla_49")
        self.casilla_50 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_50.setGeometry(QtCore.QRect(460, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_50.setFont(font)
        self.casilla_50.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_50.setObjectName("casilla_50")
        self.casilla_51 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_51.setGeometry(QtCore.QRect(510, 280, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_51.setFont(font)
        self.casilla_51.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_51.setObjectName("casilla_51")
        self.casilla_52 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_52.setGeometry(QtCore.QRect(410, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_52.setFont(font)
        self.casilla_52.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_52.setObjectName("casilla_52")
        self.casilla_53 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_53.setGeometry(QtCore.QRect(460, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_53.setFont(font)
        self.casilla_53.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_53.setObjectName("casilla_53")
        self.casilla_54 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_54.setGeometry(QtCore.QRect(510, 330, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_54.setFont(font)
        self.casilla_54.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_54.setObjectName("casilla_54")
        self.casilla_55 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_55.setGeometry(QtCore.QRect(90, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_55.setFont(font)
        self.casilla_55.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_55.setObjectName("casilla_55")
        self.casilla_56 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_56.setGeometry(QtCore.QRect(140, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_56.setFont(font)
        self.casilla_56.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_56.setObjectName("casilla_56")
        self.casilla_57 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_57.setGeometry(QtCore.QRect(190, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_57.setFont(font)
        self.casilla_57.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_57.setObjectName("casilla_57")
        self.casilla_58 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_58.setGeometry(QtCore.QRect(90, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_58.setFont(font)
        self.casilla_58.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_58.setObjectName("casilla_58")
        self.casilla_59 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_59.setGeometry(QtCore.QRect(140, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_59.setFont(font)
        self.casilla_59.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_59.setObjectName("casilla_59")
        self.casilla_60 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_60.setGeometry(QtCore.QRect(190, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_60.setFont(font)
        self.casilla_60.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_60.setObjectName("casilla_60")
        self.casilla_61 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_61.setGeometry(QtCore.QRect(90, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_61.setFont(font)
        self.casilla_61.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_61.setObjectName("casilla_61")
        self.casilla_62 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_62.setGeometry(QtCore.QRect(140, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_62.setFont(font)
        self.casilla_62.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_62.setObjectName("casilla_62")
        self.casilla_63 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_63.setGeometry(QtCore.QRect(190, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_63.setFont(font)
        self.casilla_63.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_63.setObjectName("casilla_63")
        self.casilla_64 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_64.setGeometry(QtCore.QRect(250, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_64.setFont(font)
        self.casilla_64.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_64.setObjectName("casilla_64")
        self.casilla_65 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_65.setGeometry(QtCore.QRect(300, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_65.setFont(font)
        self.casilla_65.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_65.setObjectName("casilla_65")
        self.casilla_66 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_66.setGeometry(QtCore.QRect(350, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_66.setFont(font)
        self.casilla_66.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_66.setObjectName("casilla_66")
        self.casilla_67 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_67.setGeometry(QtCore.QRect(250, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_67.setFont(font)
        self.casilla_67.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_67.setObjectName("casilla_67")
        self.casilla_68 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_68.setGeometry(QtCore.QRect(300, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_68.setFont(font)
        self.casilla_68.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_68.setObjectName("casilla_68")
        self.casilla_69 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_69.setGeometry(QtCore.QRect(350, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_69.setFont(font)
        self.casilla_69.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_69.setObjectName("casilla_69")
        self.casilla_70 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_70.setGeometry(QtCore.QRect(250, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_70.setFont(font)
        self.casilla_70.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_70.setObjectName("casilla_70")
        self.casilla_71 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_71.setGeometry(QtCore.QRect(300, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_71.setFont(font)
        self.casilla_71.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_71.setObjectName("casilla_71")
        self.casilla_72 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_72.setGeometry(QtCore.QRect(350, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_72.setFont(font)
        self.casilla_72.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_72.setObjectName("casilla_72")
        self.casilla_73 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_73.setGeometry(QtCore.QRect(410, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_73.setFont(font)
        self.casilla_73.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_73.setObjectName("casilla_73")
        self.casilla_74 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_74.setGeometry(QtCore.QRect(460, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_74.setFont(font)
        self.casilla_74.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_74.setObjectName("casilla_74")
        self.casilla_75 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_75.setGeometry(QtCore.QRect(510, 390, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_75.setFont(font)
        self.casilla_75.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_75.setObjectName("casilla_75")
        self.casilla_76 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_76.setGeometry(QtCore.QRect(410, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_76.setFont(font)
        self.casilla_76.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_76.setObjectName("casilla_76")
        self.casilla_77 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_77.setGeometry(QtCore.QRect(460, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_77.setFont(font)
        self.casilla_77.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_77.setObjectName("casilla_77")
        self.casilla_78 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_78.setGeometry(QtCore.QRect(510, 440, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_78.setFont(font)
        self.casilla_78.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_78.setObjectName("casilla_78")
        self.casilla_79 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_79.setGeometry(QtCore.QRect(410, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_79.setFont(font)
        self.casilla_79.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_79.setObjectName("casilla_79")
        self.casilla_80 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_80.setGeometry(QtCore.QRect(460, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_80.setFont(font)
        self.casilla_80.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_80.setObjectName("casilla_80")
        self.casilla_81 = QtWidgets.QPushButton(self.centralwidget)
        self.casilla_81.setGeometry(QtCore.QRect(510, 490, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.casilla_81.setFont(font)
        self.casilla_81.setStyleSheet("background-color:white;\n"
"color:blue;")
        self.casilla_81.setObjectName("casilla_81")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 217, 511, 15))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:black")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 378, 511, 15))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:black")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(237, 50, 15, 511))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:black")
        self.label_13.setObjectName("label_13")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(397, 50, 15, 511))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:black")
        self.label_4.setObjectName("label_4")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(558, 65, 20, 151))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:white\n"
"")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(558, 232, 20, 146))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:white\n"
"")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(558, 393, 20, 151))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:white\n"
"")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(412, 537, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color:white\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(55, 538, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("background-color:white\n"
"")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(252, 537, 145, 21))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color:white\n"
"")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        MainWindow.setCentralWidget(self.centralwidget)
        
        #Función limpiar con el boton inicio
        self.Inicio.clicked.connect(self.limpiar)
        #Agregamos una lista de las casillas
        self.casillas=[self.casilla,self.casilla_2,self.casilla_3,self.casilla_4,self.casilla_5,self.casilla_6,self.casilla_7,self.casilla_8,self.casilla_9,self.casilla_10,self.casilla_11,self.casilla_12,self.casilla_13,self.casilla_14,self.casilla_15,self.casilla_16,self.casilla_17,self.casilla_18,self.casilla_19,self.casilla_20,self.casilla_21,self.casilla_22,self.casilla_23,self.casilla_24,self.casilla_25,self.casilla_26,self.casilla_27,self.casilla_28,self.casilla_29,self.casilla_30,self.casilla_31,self.casilla_32,self.casilla_33,self.casilla_34,self.casilla_35,self.casilla_36,self.casilla_37,self.casilla_38,self.casilla_39,self.casilla_40,self.casilla_41,self.casilla_42,self.casilla_43,self.casilla_44,self.casilla_45,self.casilla_46,self.casilla_47,self.casilla_48,self.casilla_49,self.casilla_50,self.casilla_51,self.casilla_52,self.casilla_53,self.casilla_54,self.casilla_55,self.casilla_56,self.casilla_57,self.casilla_58,self.casilla_59,self.casilla_60,self.casilla_61,self.casilla_62,self.casilla_63,self.casilla_64,self.casilla_65,self.casilla_66,self.casilla_67,self.casilla_68,self.casilla_69,self.casilla_70,self.casilla_71,self.casilla_72,self.casilla_73,self.casilla_74,self.casilla_75,self.casilla_76,self.casilla_77,self.casilla_78,self.casilla_79,self.casilla_80,self.casilla_81]
        #Para crear la matriz de datos
        self.tablero=np.zeros((9,3,3),dtype=int)
        #Poner como por defecto la marca
        self.marca="x"
        #Guardará la posición previa a la tirada
        self.checa=[-1,-1,-1]
        #Matriz para ganar
        self.matrizprincipal=np.zeros(9,dtype=int)
        #Para marcar casilla
        self.casilla.clicked.connect(lambda: self.marcar(self.casilla,[0,0,0]))
        self.casilla_2.clicked.connect(lambda: self.marcar(self.casilla_2,[0,0,1]))
        self.casilla_3.clicked.connect(lambda: self.marcar(self.casilla_3,[0,0,2]))
        self.casilla_4.clicked.connect(lambda: self.marcar(self.casilla_4,[0,1,0]))
        self.casilla_5.clicked.connect(lambda: self.marcar(self.casilla_5,[0,1,1]))
        self.casilla_6.clicked.connect(lambda: self.marcar(self.casilla_6,[0,1,2]))
        self.casilla_7.clicked.connect(lambda: self.marcar(self.casilla_7,[0,2,0]))
        self.casilla_8.clicked.connect(lambda: self.marcar(self.casilla_8,[0,2,1]))        
        self.casilla_9.clicked.connect(lambda: self.marcar(self.casilla_9,[0,2,2]))
        self.casilla_10.clicked.connect(lambda: self.marcar(self.casilla_10,[1,0,0]))
        self.casilla_11.clicked.connect(lambda: self.marcar(self.casilla_11,[1,0,1]))
        self.casilla_12.clicked.connect(lambda: self.marcar(self.casilla_12,[1,0,2]))
        self.casilla_13.clicked.connect(lambda: self.marcar(self.casilla_13,[1,1,0]))
        self.casilla_14.clicked.connect(lambda: self.marcar(self.casilla_14,[1,1,1]))
        self.casilla_15.clicked.connect(lambda: self.marcar(self.casilla_15,[1,1,2]))
        self.casilla_16.clicked.connect(lambda: self.marcar(self.casilla_16,[1,2,0]))
        self.casilla_17.clicked.connect(lambda: self.marcar(self.casilla_17,[1,2,1]))        
        self.casilla_18.clicked.connect(lambda: self.marcar(self.casilla_18,[1,2,2]))
        self.casilla_19.clicked.connect(lambda: self.marcar(self.casilla_19,[2,0,0]))
        self.casilla_20.clicked.connect(lambda: self.marcar(self.casilla_20,[2,0,1]))
        self.casilla_21.clicked.connect(lambda: self.marcar(self.casilla_21,[2,0,2]))
        self.casilla_22.clicked.connect(lambda: self.marcar(self.casilla_22,[2,1,0]))
        self.casilla_23.clicked.connect(lambda: self.marcar(self.casilla_23,[2,1,1]))
        self.casilla_24.clicked.connect(lambda: self.marcar(self.casilla_24,[2,1,2]))
        self.casilla_25.clicked.connect(lambda: self.marcar(self.casilla_25,[2,2,0]))
        self.casilla_26.clicked.connect(lambda: self.marcar(self.casilla_26,[2,2,1]))        
        self.casilla_27.clicked.connect(lambda: self.marcar(self.casilla_27,[2,2,2]))
        self.casilla_28.clicked.connect(lambda: self.marcar(self.casilla_28,[3,0,0]))
        self.casilla_29.clicked.connect(lambda: self.marcar(self.casilla_29,[3,0,1]))
        self.casilla_30.clicked.connect(lambda: self.marcar(self.casilla_30,[3,0,2]))
        self.casilla_31.clicked.connect(lambda: self.marcar(self.casilla_31,[3,1,0]))
        self.casilla_32.clicked.connect(lambda: self.marcar(self.casilla_32,[3,1,1]))
        self.casilla_33.clicked.connect(lambda: self.marcar(self.casilla_33,[3,1,2]))
        self.casilla_34.clicked.connect(lambda: self.marcar(self.casilla_34,[3,2,0]))
        self.casilla_35.clicked.connect(lambda: self.marcar(self.casilla_35,[3,2,1]))        
        self.casilla_36.clicked.connect(lambda: self.marcar(self.casilla_36,[3,2,2]))
        self.casilla_37.clicked.connect(lambda: self.marcar(self.casilla_37,[4,0,0]))
        self.casilla_38.clicked.connect(lambda: self.marcar(self.casilla_38,[4,0,1]))
        self.casilla_39.clicked.connect(lambda: self.marcar(self.casilla_39,[4,0,2]))
        self.casilla_40.clicked.connect(lambda: self.marcar(self.casilla_40,[4,1,0]))
        self.casilla_41.clicked.connect(lambda: self.marcar(self.casilla_41,[4,1,1]))
        self.casilla_42.clicked.connect(lambda: self.marcar(self.casilla_42,[4,1,2]))
        self.casilla_43.clicked.connect(lambda: self.marcar(self.casilla_43,[4,2,0]))
        self.casilla_44.clicked.connect(lambda: self.marcar(self.casilla_44,[4,2,1]))        
        self.casilla_45.clicked.connect(lambda: self.marcar(self.casilla_45,[4,2,2]))
        self.casilla_46.clicked.connect(lambda: self.marcar(self.casilla_46,[5,0,0]))
        self.casilla_47.clicked.connect(lambda: self.marcar(self.casilla_47,[5,0,1]))
        self.casilla_48.clicked.connect(lambda: self.marcar(self.casilla_48,[5,0,2]))
        self.casilla_49.clicked.connect(lambda: self.marcar(self.casilla_49,[5,1,0]))
        self.casilla_50.clicked.connect(lambda: self.marcar(self.casilla_50,[5,1,1]))
        self.casilla_51.clicked.connect(lambda: self.marcar(self.casilla_51,[5,1,2]))
        self.casilla_52.clicked.connect(lambda: self.marcar(self.casilla_52,[5,2,0]))
        self.casilla_53.clicked.connect(lambda: self.marcar(self.casilla_53,[5,2,1]))        
        self.casilla_54.clicked.connect(lambda: self.marcar(self.casilla_54,[5,2,2]))
        self.casilla_55.clicked.connect(lambda: self.marcar(self.casilla_55,[6,0,0]))
        self.casilla_56.clicked.connect(lambda: self.marcar(self.casilla_56,[6,0,1]))
        self.casilla_57.clicked.connect(lambda: self.marcar(self.casilla_57,[6,0,2]))
        self.casilla_58.clicked.connect(lambda: self.marcar(self.casilla_58,[6,1,0]))
        self.casilla_59.clicked.connect(lambda: self.marcar(self.casilla_59,[6,1,1]))
        self.casilla_60.clicked.connect(lambda: self.marcar(self.casilla_60,[6,1,2]))
        self.casilla_61.clicked.connect(lambda: self.marcar(self.casilla_61,[6,2,0]))
        self.casilla_62.clicked.connect(lambda: self.marcar(self.casilla_62,[6,2,1]))        
        self.casilla_63.clicked.connect(lambda: self.marcar(self.casilla_63,[6,2,2]))
        self.casilla_64.clicked.connect(lambda: self.marcar(self.casilla_64,[7,0,0]))
        self.casilla_65.clicked.connect(lambda: self.marcar(self.casilla_65,[7,0,1]))
        self.casilla_66.clicked.connect(lambda: self.marcar(self.casilla_66,[7,0,2]))
        self.casilla_67.clicked.connect(lambda: self.marcar(self.casilla_67,[7,1,0]))
        self.casilla_68.clicked.connect(lambda: self.marcar(self.casilla_68,[7,1,1]))
        self.casilla_69.clicked.connect(lambda: self.marcar(self.casilla_69,[7,1,2]))
        self.casilla_70.clicked.connect(lambda: self.marcar(self.casilla_70,[7,2,0]))
        self.casilla_71.clicked.connect(lambda: self.marcar(self.casilla_71,[7,2,1]))        
        self.casilla_72.clicked.connect(lambda: self.marcar(self.casilla_72,[7,2,2]))
        self.casilla_73.clicked.connect(lambda: self.marcar(self.casilla_73,[8,0,0]))
        self.casilla_74.clicked.connect(lambda: self.marcar(self.casilla_74,[8,0,1]))
        self.casilla_75.clicked.connect(lambda: self.marcar(self.casilla_75,[8,0,2]))
        self.casilla_76.clicked.connect(lambda: self.marcar(self.casilla_76,[8,1,0]))
        self.casilla_77.clicked.connect(lambda: self.marcar(self.casilla_77,[8,1,1]))
        self.casilla_78.clicked.connect(lambda: self.marcar(self.casilla_78,[8,1,2]))
        self.casilla_79.clicked.connect(lambda: self.marcar(self.casilla_79,[8,2,0]))
        self.casilla_80.clicked.connect(lambda: self.marcar(self.casilla_80,[8,2,1]))        
        self.casilla_81.clicked.connect(lambda: self.marcar(self.casilla_81,[8,2,2]))
        



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.casilla.setText(_translate("MainWindow", "x"))
        self.Inicio.setText(_translate("MainWindow", "Inicia el juego"))
        self.Tittle.setText(_translate("MainWindow", "Gato x Gato"))
        self.casilla_2.setText(_translate("MainWindow", "x"))
        self.casilla_3.setText(_translate("MainWindow", "x"))
        self.casilla_4.setText(_translate("MainWindow", "x"))
        self.casilla_5.setText(_translate("MainWindow", "x"))
        self.casilla_6.setText(_translate("MainWindow", "x"))
        self.casilla_7.setText(_translate("MainWindow", "x"))
        self.casilla_8.setText(_translate("MainWindow", "x"))
        self.casilla_9.setText(_translate("MainWindow", "x"))
        self.casilla_10.setText(_translate("MainWindow", "x"))
        self.casilla_11.setText(_translate("MainWindow", "x"))
        self.casilla_12.setText(_translate("MainWindow", "x"))
        self.casilla_13.setText(_translate("MainWindow", "x"))
        self.casilla_14.setText(_translate("MainWindow", "x"))
        self.casilla_15.setText(_translate("MainWindow", "x"))
        self.casilla_16.setText(_translate("MainWindow", "x"))
        self.casilla_17.setText(_translate("MainWindow", "x"))
        self.casilla_18.setText(_translate("MainWindow", "x"))
        self.casilla_19.setText(_translate("MainWindow", "x"))
        self.casilla_20.setText(_translate("MainWindow", "x"))
        self.casilla_21.setText(_translate("MainWindow", "x"))
        self.casilla_22.setText(_translate("MainWindow", "x"))
        self.casilla_23.setText(_translate("MainWindow", "x"))
        self.casilla_24.setText(_translate("MainWindow", "x"))
        self.casilla_25.setText(_translate("MainWindow", "x"))
        self.casilla_26.setText(_translate("MainWindow", "x"))
        self.casilla_27.setText(_translate("MainWindow", "x"))
        self.casilla_28.setText(_translate("MainWindow", "x"))
        self.casilla_29.setText(_translate("MainWindow", "x"))
        self.casilla_30.setText(_translate("MainWindow", "x"))
        self.casilla_31.setText(_translate("MainWindow", "x"))
        self.casilla_32.setText(_translate("MainWindow", "x"))
        self.casilla_33.setText(_translate("MainWindow", "x"))
        self.casilla_34.setText(_translate("MainWindow", "x"))
        self.casilla_35.setText(_translate("MainWindow", "x"))
        self.casilla_36.setText(_translate("MainWindow", "x"))
        self.casilla_37.setText(_translate("MainWindow", "x"))
        self.casilla_38.setText(_translate("MainWindow", "x"))
        self.casilla_39.setText(_translate("MainWindow", "x"))
        self.casilla_40.setText(_translate("MainWindow", "x"))
        self.casilla_41.setText(_translate("MainWindow", "x"))
        self.casilla_42.setText(_translate("MainWindow", "x"))
        self.casilla_43.setText(_translate("MainWindow", "x"))
        self.casilla_44.setText(_translate("MainWindow", "x"))
        self.casilla_45.setText(_translate("MainWindow", "x"))
        self.casilla_46.setText(_translate("MainWindow", "x"))
        self.casilla_47.setText(_translate("MainWindow", "x"))
        self.casilla_48.setText(_translate("MainWindow", "x"))
        self.casilla_49.setText(_translate("MainWindow", "x"))
        self.casilla_50.setText(_translate("MainWindow", "x"))
        self.casilla_51.setText(_translate("MainWindow", "x"))
        self.casilla_52.setText(_translate("MainWindow", "x"))
        self.casilla_53.setText(_translate("MainWindow", "x"))
        self.casilla_54.setText(_translate("MainWindow", "x"))
        self.casilla_55.setText(_translate("MainWindow", "x"))
        self.casilla_56.setText(_translate("MainWindow", "x"))
        self.casilla_57.setText(_translate("MainWindow", "x"))
        self.casilla_58.setText(_translate("MainWindow", "x"))
        self.casilla_59.setText(_translate("MainWindow", "x"))
        self.casilla_60.setText(_translate("MainWindow", "x"))
        self.casilla_61.setText(_translate("MainWindow", "x"))
        self.casilla_62.setText(_translate("MainWindow", "x"))
        self.casilla_63.setText(_translate("MainWindow", "x"))
        self.casilla_64.setText(_translate("MainWindow", "x"))
        self.casilla_65.setText(_translate("MainWindow", "x"))
        self.casilla_66.setText(_translate("MainWindow", "x"))
        self.casilla_67.setText(_translate("MainWindow", "x"))
        self.casilla_68.setText(_translate("MainWindow", "x"))
        self.casilla_69.setText(_translate("MainWindow", "x"))
        self.casilla_70.setText(_translate("MainWindow", "x"))
        self.casilla_71.setText(_translate("MainWindow", "x"))
        self.casilla_72.setText(_translate("MainWindow", "x"))
        self.casilla_73.setText(_translate("MainWindow", "x"))
        self.casilla_74.setText(_translate("MainWindow", "x"))
        self.casilla_75.setText(_translate("MainWindow", "x"))
        self.casilla_76.setText(_translate("MainWindow", "x"))
        self.casilla_77.setText(_translate("MainWindow", "x"))
        self.casilla_78.setText(_translate("MainWindow", "x"))
        self.casilla_79.setText(_translate("MainWindow", "x"))
        self.casilla_80.setText(_translate("MainWindow", "x"))
        self.casilla_81.setText(_translate("MainWindow", "x"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
    #Método que comprueba si hay ganadores
    def comprobar(self):
        for i in range(9):
            if np.sum(self.tablero[i][0,:])==3 or np.sum(self.tablero[i][1,:])==3 or np.sum(self.tablero[i][2,:])==3:
                    self.matrizprincipal[i]=1
            elif np.sum(self.tablero[i][:,0])==3 or np.sum(self.tablero[i][:,1])==3 or np.sum(self.tablero[i][:,2])==3:
                    self.matrizprincipal[i]=1
            elif np.sum(np.trace(self.tablero[i]))==3 or np.sum(np.trace(np.fliplr( self.tablero[i])))==3 :
                    self.matrizprincipal[i]=1
            elif np.sum(self.tablero[i][0,:])==-3 or np.sum(self.tablero[i][1,:])==-3 or np.sum(self.tablero[i][2,:])==-3:
                    self.matrizprincipal[i]=-1
            elif np.sum(self.tablero[i][:,0])==-3 or np.sum(self.tablero[i][:,1])==-3 or np.sum(self.tablero[i][:,2])==-3:
                    self.matrizprincipal[i]=-1
            elif np.sum(np.trace(self.tablero[i]))==-3 or np.sum(np.trace(np.fliplr( self.tablero[i])))==-3 :
                    self.matrizprincipal[i]=-1
        if self.matrizprincipal[0]+self.matrizprincipal[1]+self.matrizprincipal[2]==3 or self.matrizprincipal[3]+self.matrizprincipal[4]+self.matrizprincipal[5]==3 or self.matrizprincipal[6]+self.matrizprincipal[7]+self.matrizprincipal[8]==3 or self.matrizprincipal[0]+self.matrizprincipal[3]+self.matrizprincipal[6]==3 or self.matrizprincipal[1]+self.matrizprincipal[4]+self.matrizprincipal[7]==3 or self.matrizprincipal[2]+self.matrizprincipal[5]+self.matrizprincipal[8]==3 or self.matrizprincipal[0]+self.matrizprincipal[4]+self.matrizprincipal[8]==3 or self.matrizprincipal[2]+self.matrizprincipal[4]+self.matrizprincipal[6]==3:
            return True
        elif  self.matrizprincipal[0]+self.matrizprincipal[1]+self.matrizprincipal[2]==-3 or self.matrizprincipal[3]+self.matrizprincipal[4]+self.matrizprincipal[5]==-3 or self.matrizprincipal[6]+self.matrizprincipal[7]+self.matrizprincipal[8]==-3 or self.matrizprincipal[0]+self.matrizprincipal[3]+self.matrizprincipal[6]==-3 or self.matrizprincipal[1]+self.matrizprincipal[4]+self.matrizprincipal[7]==-3 or self.matrizprincipal[2]+self.matrizprincipal[5]+self.matrizprincipal[8]==-3 or self.matrizprincipal[0]+self.matrizprincipal[4]+self.matrizprincipal[8]==-3 or self.matrizprincipal[2]+self.matrizprincipal[4]+self.matrizprincipal[6]==-3:
            return True
        return False
        pass 


    #Para marcar una jugada en el tablero y respeta la regla de posición
    def marcar(self,casilla,coordenadas):
        self.labelwin.setText("")
        if self.checa[0]==-1 and self.checa[1]==-1 and self.checa[2]==-1:
            casilla.setText('x')
            self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
            self.marca='o'
            for i in range (3):
                self.checa[i]=coordenadas[i]
                
        elif self.checa[1]==0 and self.checa[2]==0:
            if coordenadas[0]==0:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(1)
                self.labelwin.setText("Tira en el minigato " + suma)
                    
        elif self.checa[1]==0 and self.checa[2]==1:
            if coordenadas[0]==1:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(2)
                self.labelwin.setText("Tira en el minigato "+suma)
                    
        elif self.checa[1]==0 and self.checa[2]==2:
            if coordenadas[0]==2:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(3)
                self.labelwin.setText("Tira en el minigato "+suma)
                    
        elif self.checa[1]==1 and self.checa[2]==0:
            if coordenadas[0]==3:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(4)
                self.labelwin.setText("Tira en el minigato "+suma)
                    
        elif self.checa[1]==1 and self.checa[2]==1:
            if coordenadas[0]==4:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(5)
                self.labelwin.setText("Tira en el minigato "+suma)
        
        elif self.checa[1]==1 and self.checa[2]==2:
            if coordenadas[0]==5:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(6)
                self.labelwin.setText("Tira en el minigato "+suma)

        elif self.checa[1]==2 and self.checa[2]==0:
            
            if coordenadas[0]==6:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(7)
                self.labelwin.setText("Tira en el minigato "+suma)
                    
        elif self.checa[1]==2 and self.checa[2]==1:
            
            if coordenadas[0]==7:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(8)
                self.labelwin.setText("Tira en el minigato "+suma)
                
        elif self.checa[1]==2 and self.checa[2]==2:
            if coordenadas[0]==8:
                if self.marca=='x':
                    casilla.setText('x')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='o'
                else:
                    casilla.setText('o')
                    self.tablero[coordenadas[0],coordenadas[1],coordenadas[2]]=-1
                    if self.comprobar():
                        self.labelwin.setText("Ganó "+self.marca)
                        for c in self.casillas:
                                c.setDisabled(True)
                    self.marca='x'
                for i in range (3):
                    self.checa[i]=coordenadas[i]
            else:
                suma=str(9)
                self.labelwin.setText("Tira en el minigato "+suma)
        
    #Lo que se ejecuta en el boton reinicio
    def limpiar(self):
        self.marca='x'
        self.checa=[-1,-1,-1]
        self.tablero=np.zeros((9,3,3),dtype=int)#Matriz que almacena los datos del tablero x´s y o´s
        for c in self.casillas: #Borra marcas en el tablero
            c.setText("")
            c.setDisabled(False)
        self.labelwin.clear()
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

