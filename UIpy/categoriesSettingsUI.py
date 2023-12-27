# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoriesSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(450, 350))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #fff\n"
"}\n"
"\n"
"QPushButton[big=\'true\'] {\n"
"    background-color: #54ad54;\n"
"    border: none;\n"
"    border-radius: 0.25em;\n"
"    color: #fff;\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"QPushButton[small=\'true\'] {\n"
"    background-color: #999;\n"
"    border: none;\n"
"    border-radius: 0.25em;\n"
"    color: #fff;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QPushButton[big=\'true\']:hover {\n"
"    background-color: #288b28;\n"
"}\n"
"\n"
"QPushButton[small=\'true\']:hover {\n"
"    background-color: #777;\n"
"}\n"
"\n"
"QPushButton[big=\'true\']:pressed {\n"
"    background-color: #246024;\n"
"}\n"
"\n"
"QPushButton[small=\'true\']:pressed {\n"
"    background-color: #555;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setMinimumSize(QtCore.QSize(300, 60))
        self.addBtn.setMaximumSize(QtCore.QSize(300, 60))
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setProperty("big", True)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setMinimumSize(QtCore.QSize(300, 60))
        self.editBtn.setMaximumSize(QtCore.QSize(300, 60))
        self.editBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editBtn.setProperty("big", True)
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout_3.addWidget(self.editBtn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setMinimumSize(QtCore.QSize(300, 60))
        self.deleteBtn.setMaximumSize(QtCore.QSize(300, 60))
        self.deleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteBtn.setProperty("big", True)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_2.addWidget(self.deleteBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.cancelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.cancelBtn.setMaximumSize(QtCore.QSize(100, 30))
        self.cancelBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelBtn.setProperty("small", True)
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_4.addWidget(self.cancelBtn)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Настроить категории"))
        self.addBtn.setText(_translate("MainWindow", "Добавить"))
        self.editBtn.setText(_translate("MainWindow", "Изменить"))
        self.deleteBtn.setText(_translate("MainWindow", "Удалить"))
        self.cancelBtn.setText(_translate("MainWindow", "Отмена"))