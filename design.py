# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(5, 1, 501, 541))
        self.textEdit.setObjectName("textEdit")
        self.dateLine = QtWidgets.QLineEdit(self.centralwidget)
        self.dateLine.setGeometry(QtCore.QRect(510, 60, 241, 20))
        self.dateLine.setObjectName("dateLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 30, 241, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 10, 241, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 80, 241, 20))
        self.label_3.setObjectName("label_3")
        self.timeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.timeLine.setGeometry(QtCore.QRect(510, 110, 241, 21))
        self.timeLine.setObjectName("timeLine")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 130, 241, 20))
        self.label_4.setObjectName("label_4")
        self.locationText = QtWidgets.QTextEdit(self.centralwidget)
        self.locationText.setGeometry(QtCore.QRect(510, 160, 241, 91))
        self.locationText.setObjectName("locationText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.closeAction = QtWidgets.QAction(MainWindow)
        self.closeAction.setObjectName("closeAction")
        self.newAction = QtWidgets.QAction(MainWindow)
        self.newAction.setObjectName("newAction")
        self.menu.addAction(self.newAction)
        self.menu.addAction(self.saveAction)
        self.menu.addAction(self.openAction)
        self.menu.addSeparator()
        self.menu.addAction(self.closeAction)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Дата последней записи:"))
        self.label_2.setText(_translate("MainWindow", "Последняя запись:"))
        self.label_3.setText(_translate("MainWindow", "Время последней записи:"))
        self.label_4.setText(_translate("MainWindow", "Местоположение во время последней записи:"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.saveAction.setText(_translate("MainWindow", "Сохранить"))
        self.openAction.setText(_translate("MainWindow", "Открыть"))
        self.closeAction.setText(_translate("MainWindow", "Закрыть"))
        self.newAction.setText(_translate("MainWindow", "Новая запись"))

