# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'todo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Todo(object):
    def setupUi(self, Todo):
        Todo.setObjectName("Todo")
        Todo.resize(1025, 725)
        Todo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Todo.setStyleSheet("#centralwidget {\n"
"    padding: 20px;\n"
"}\n"
"\n"
"#planLabel {\n"
"    font-size: 50px;\n"
"}\n"
"\n"
"#taskName {\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background-color: #fff\n"
"}\n"
"\n"
"QPushButton[plan=\'true\'] {\n"
"    background-color: #54ad54;\n"
"    border: none;\n"
"    border-radius: 0.25em;\n"
"    color: #fff;\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"QPushButton[small=\'true\'] {\n"
"    background-color: #999;\n"
"    border: none;\n"
"    border-radius: 0.25em;\n"
"    color: #fff;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton[plan=\'true\']:hover {\n"
"    background-color: #288b28;\n"
"}\n"
"\n"
"QPushButton[small=\'true\']:hover {\n"
"    background-color: #777;\n"
"}\n"
"\n"
"QPushButton[plan=\'true\']:pressed {\n"
"    background-color: #246024;\n"
"}\n"
"\n"
"QPushButton[small=\'true\']:pressed {\n"
"    background-color: #555;\n"
"}\n"
"\n"
"#deleteBtn {\n"
"    border: none;/* 1px solid red;*/\n"
"/*    background-color: #F34235;*/\n"
"    background-color: #DC3545;\n"
"    border-radius: 0.25em;\n"
"    /*background-image: url(bin.png);*/\n"
"}\n"
"\n"
"#deleteBtn:hover {\n"
"    background-color: #BB2D3B;\n"
"}\n"
"\n"
"#editBtn {\n"
"    border: none;/* 1px solid red;*/\n"
"    background-color: #0D6EFD;\n"
"    border-radius: 0.25em;\n"
"    /*background-image: url(bin.png);*/\n"
"}\n"
"\n"
"#editBtn:hover {\n"
"    background-color: #0B5ED7;\n"
"}\n"
"\n"
"#viewImageBtn {\n"
"    border: none;/* 1px solid red;*/\n"
"    background-color: #0D6EFD;\n"
"    border-radius: 0.25em;\n"
"    /*background-image: url(bin.png);*/\n"
"}\n"
"\n"
"#viewImageBtn:hover {\n"
"    background-color: #0B5ED7;\n"
"}\n"
"\n"
"#markAsDoneBtn {\n"
"    border: none;/* 1px solid red;*/\n"
"    background-color: #FFC107;\n"
"    border-radius: 0.25em;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"#markAsDoneBtn:hover {\n"
"    background-color: #FFCA2C\n"
"}\n"
"\n"
"#addBtn {\n"
"    background-color: #FFFFFF;\n"
"    color: #0DCAF0;\n"
"    font-size: 15px;\n"
"    border: 1px solid #0DCAF0;\n"
"    border-radius: 0.4em;\n"
"}\n"
"\n"
"#addBtn:hover {\n"
"    background-color: #3DD5F3;\n"
"    color: #000000;\n"
"    font-size: 15px;\n"
"    border: 1px solid #3DD5F3;\n"
"    border-radius: 0.4em;\n"
"}\n"
"\n"
"#tasksList {\n"
"    border: 1px solid #0DCAF0;\n"
"}\n"
"\n"
"#title, #category, #repeat, #deadline, #description {\n"
"    border: 1px solid #ccc;\n"
"    border-bottom: 1px solid #54ad54;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#titleLabel, #categoryLabel, #repeatLabel, #deadlineLabel, #descriptionLabel {\n"
"    font-size: 15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Todo)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.categoriesSettingsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.categoriesSettingsBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.categoriesSettingsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.categoriesSettingsBtn.setProperty("small", True)
        self.categoriesSettingsBtn.setObjectName("categoriesSettingsBtn")
        self.horizontalLayout_5.addWidget(self.categoriesSettingsBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.reminderBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reminderBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.reminderBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reminderBtn.setProperty("small", True)
        self.reminderBtn.setObjectName("reminderBtn")
        self.horizontalLayout_5.addWidget(self.reminderBtn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.intoCsvBtn = QtWidgets.QPushButton(self.centralwidget)
        self.intoCsvBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.intoCsvBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.intoCsvBtn.setProperty("small", True)
        self.intoCsvBtn.setObjectName("intoCsvBtn")
        self.horizontalLayout_5.addWidget(self.intoCsvBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.allDaysBtn = QtWidgets.QPushButton(self.centralwidget)
        self.allDaysBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.allDaysBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.allDaysBtn.setProperty("small", True)
        self.allDaysBtn.setObjectName("allDaysBtn")
        self.horizontalLayout_5.addWidget(self.allDaysBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.today = QtWidgets.QPushButton(self.frame)
        self.today.setMinimumSize(QtCore.QSize(200, 60))
        self.today.setMaximumSize(QtCore.QSize(200, 60))
        self.today.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.today.setStyleSheet("")
        self.today.setProperty("plan", True)
        self.today.setObjectName("today")
        self.horizontalLayout.addWidget(self.today)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.tomorrow = QtWidgets.QPushButton(self.frame)
        self.tomorrow.setMinimumSize(QtCore.QSize(200, 60))
        self.tomorrow.setMaximumSize(QtCore.QSize(200, 60))
        self.tomorrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tomorrow.setStyleSheet("")
        self.tomorrow.setProperty("plan", True)
        self.tomorrow.setObjectName("tomorrow")
        self.horizontalLayout.addWidget(self.tomorrow)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.daily = QtWidgets.QPushButton(self.frame)
        self.daily.setMinimumSize(QtCore.QSize(200, 60))
        self.daily.setMaximumSize(QtCore.QSize(200, 60))
        self.daily.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.daily.setProperty("plan", True)
        self.daily.setObjectName("daily")
        self.horizontalLayout.addWidget(self.daily)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.week = QtWidgets.QPushButton(self.frame)
        self.week.setMinimumSize(QtCore.QSize(200, 60))
        self.week.setMaximumSize(QtCore.QSize(200, 60))
        self.week.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.week.setStyleSheet("")
        self.week.setProperty("plan", True)
        self.week.setObjectName("week")
        self.horizontalLayout_7.addWidget(self.week)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.month = QtWidgets.QPushButton(self.frame)
        self.month.setMinimumSize(QtCore.QSize(200, 60))
        self.month.setMaximumSize(QtCore.QSize(200, 60))
        self.month.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.month.setStyleSheet("")
        self.month.setProperty("plan", True)
        self.month.setObjectName("month")
        self.horizontalLayout_7.addWidget(self.month)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.planLabel = QtWidgets.QLabel(self.centralwidget)
        self.planLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.planLabel.setStyleSheet("")
        self.planLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.planLabel.setIndent(0)
        self.planLabel.setObjectName("planLabel")
        self.verticalLayout_3.addWidget(self.planLabel)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setMinimumSize(QtCore.QSize(200, 30))
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addBtn.setStyleSheet("")
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_2.addWidget(self.addBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tasksList = QtWidgets.QListWidget(self.centralwidget)
        self.tasksList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tasksList.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.tasksList.setStyleSheet("b")
        self.tasksList.setObjectName("tasksList")
        self.verticalLayout_2.addWidget(self.tasksList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setIndent(5)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.title = QtWidgets.QTextEdit(self.centralwidget)
        self.title.setMaximumSize(QtCore.QSize(16777215, 40))
        self.title.setStyleSheet("b")
        self.title.setReadOnly(True)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.categoryLabel.setIndent(5)
        self.categoryLabel.setObjectName("categoryLabel")
        self.verticalLayout.addWidget(self.categoryLabel)
        self.category = QtWidgets.QTextEdit(self.centralwidget)
        self.category.setMaximumSize(QtCore.QSize(16777215, 30))
        self.category.setStyleSheet("b")
        self.category.setReadOnly(True)
        self.category.setObjectName("category")
        self.verticalLayout.addWidget(self.category)
        self.repeatLabel = QtWidgets.QLabel(self.centralwidget)
        self.repeatLabel.setIndent(5)
        self.repeatLabel.setObjectName("repeatLabel")
        self.verticalLayout.addWidget(self.repeatLabel)
        self.repeat = QtWidgets.QTextEdit(self.centralwidget)
        self.repeat.setMaximumSize(QtCore.QSize(16777215, 30))
        self.repeat.setStyleSheet("b")
        self.repeat.setObjectName("repeat")
        self.verticalLayout.addWidget(self.repeat)
        self.deadlineLabel = QtWidgets.QLabel(self.centralwidget)
        self.deadlineLabel.setIndent(5)
        self.deadlineLabel.setObjectName("deadlineLabel")
        self.verticalLayout.addWidget(self.deadlineLabel)
        self.deadline = QtWidgets.QDateEdit(self.centralwidget)
        self.deadline.setFrame(True)
        self.deadline.setReadOnly(True)
        self.deadline.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.deadline.setObjectName("deadline")
        self.verticalLayout.addWidget(self.deadline)
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setIndent(5)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.verticalLayout.addWidget(self.descriptionLabel)
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.description.setStyleSheet("b")
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.verticalLayout.addWidget(self.description)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.deleteBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.deleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteBtn.setText("")
        self.deleteBtn.setIconSize(QtCore.QSize(20, 20))
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_3.addWidget(self.deleteBtn)
        self.markAsDoneBtn = QtWidgets.QPushButton(self.centralwidget)
        self.markAsDoneBtn.setMinimumSize(QtCore.QSize(250, 30))
        self.markAsDoneBtn.setMaximumSize(QtCore.QSize(250, 30))
        self.markAsDoneBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.markAsDoneBtn.setObjectName("markAsDoneBtn")
        self.horizontalLayout_3.addWidget(self.markAsDoneBtn)
        self.viewImageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.viewImageBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.viewImageBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.viewImageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.viewImageBtn.setText("")
        self.viewImageBtn.setIconSize(QtCore.QSize(20, 20))
        self.viewImageBtn.setObjectName("viewImageBtn")
        self.horizontalLayout_3.addWidget(self.viewImageBtn)
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.editBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.editBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editBtn.setText("")
        self.editBtn.setIconSize(QtCore.QSize(20, 20))
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout_3.addWidget(self.editBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        Todo.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Todo)
        self.statusbar.setObjectName("statusbar")
        Todo.setStatusBar(self.statusbar)

        self.retranslateUi(Todo)
        QtCore.QMetaObject.connectSlotsByName(Todo)

    def retranslateUi(self, Todo):
        _translate = QtCore.QCoreApplication.translate
        Todo.setWindowTitle(_translate("Todo", "Планировщик дел"))
        self.categoriesSettingsBtn.setText(_translate("Todo", "Настроить категории"))
        self.reminderBtn.setText(_translate("Todo", "Поставить напоминание"))
        self.intoCsvBtn.setText(_translate("Todo", "План в csv"))
        self.allDaysBtn.setText(_translate("Todo", "Все запланированые дела"))
        self.today.setText(_translate("Todo", "План на сегодня"))
        self.tomorrow.setText(_translate("Todo", "План на завтра"))
        self.daily.setText(_translate("Todo", "Ежедневные дела"))
        self.week.setText(_translate("Todo", "План на неделю"))
        self.month.setText(_translate("Todo", "План на месяц"))
        self.planLabel.setText(_translate("Todo", "План на сегодня"))
        self.addBtn.setText(_translate("Todo", "Добавить дело"))
        self.titleLabel.setText(_translate("Todo", "Название:"))
        self.title.setHtml(_translate("Todo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Сделать зарядку Сделать зарядку Сделать зарядку Сделать зарядку</span></p></body></html>"))
        self.categoryLabel.setText(_translate("Todo", "Категория:"))
        self.category.setHtml(_translate("Todo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">Важное</span></p></body></html>"))
        self.repeatLabel.setText(_translate("Todo", "Повтор:"))
        self.repeat.setHtml(_translate("Todo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">ПН, ВТ, СР, ЧТ, ПТ</span></p></body></html>"))
        self.deadlineLabel.setText(_translate("Todo", "Дедлайн"))
        self.descriptionLabel.setText(_translate("Todo", "Описание:"))
        self.description.setHtml(_translate("Todo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:15px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">апдловалдповлапдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">вдлаплдваопдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">долвоапдлвоапдло</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">апдловалдповлапдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">вдлаплдваопдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">долвоапдлвоапдло</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">апдловалдповлапдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">вдлаплдваопдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">долвоапдлвоапдло</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">апдловалдповлапдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">вдлаплдваопдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">долвоапдлвоапдло</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">апдловалдповлапдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">вдлаплдваопдл</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">долвоапдлвоапдло</span></p></body></html>"))
        self.markAsDoneBtn.setText(_translate("Todo", "Пометить как сделанное"))
