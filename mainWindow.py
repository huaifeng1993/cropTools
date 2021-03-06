# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from canvas import myLabel
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 720)
        MainWindow.setMinimumSize(QtCore.QSize(50, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/cloud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(620, 70, 42, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.startBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.startBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startBtn.setIcon(icon1)
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout.addWidget(self.startBtn)
        self.rightBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.rightBtn.setEnabled(False)
        self.rightBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rightBtn.setIcon(icon2)
        self.rightBtn.setObjectName("rightBtn")
        self.verticalLayout.addWidget(self.rightBtn)
        self.leftBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.leftBtn.setEnabled(False)
        self.leftBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.leftBtn.setIcon(icon3)
        self.leftBtn.setObjectName("leftBtn")
        self.verticalLayout.addWidget(self.leftBtn)
        self.deletBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.deletBtn.setEnabled(False)
        self.deletBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deletBtn.setIcon(icon4)
        self.deletBtn.setObjectName("deletBtn")
        self.verticalLayout.addWidget(self.deletBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 312, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.iamgeLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.iamgeLabel.setObjectName("iamgeLabel")
        self.horizontalLayout_2.addWidget(self.iamgeLabel)
        self.imageOpenToolBtn = QtWidgets.QToolButton(self.layoutWidget1)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageOpenToolBtn.setIcon(icon5)
        self.imageOpenToolBtn.setObjectName("imageOpenToolBtn")
        self.horizontalLayout_2.addWidget(self.imageOpenToolBtn)
        self.imageLineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.imageLineEdit.setObjectName("imageLineEdit")
        self.horizontalLayout_2.addWidget(self.imageLineEdit)
        self.imageCandvas = QtWidgets.QWidget(self.centralwidget)
        self.imageCandvas.setGeometry(QtCore.QRect(10, 70, 600, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCandvas.sizePolicy().hasHeightForWidth())
        self.imageCandvas.setSizePolicy(sizePolicy)
        self.imageCandvas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imageCandvas.setObjectName("imageCandvas")
        self.imageQLb = myLabel(self.imageCandvas)
        self.imageQLb.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.imageQLb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.imageQLb.setText("")
        self.imageQLb.setObjectName("imageQLb")
        self.classListView = QtWidgets.QListView(self.centralwidget)
        self.classListView.setGeometry(QtCore.QRect(670, 70, 121, 271))
        self.classListView.setObjectName("classListView")
        self.classCountListView = QtWidgets.QListView(self.centralwidget)
        self.classCountListView.setGeometry(QtCore.QRect(670, 400, 121, 271))
        self.classCountListView.setObjectName("classCountListView")
        self.addClassBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addClassBtn.setGeometry(QtCore.QRect(670, 350, 61, 30))
        self.addClassBtn.setObjectName("addClassBtn")
        self.classLabel = QtWidgets.QLabel(self.centralwidget)
        self.classLabel.setGeometry(QtCore.QRect(670, 50, 54, 18))
        self.classLabel.setObjectName("classLabel")
        self.classDeletBtn = QtWidgets.QPushButton(self.centralwidget)
        self.classDeletBtn.setEnabled(False)
        self.classDeletBtn.setGeometry(QtCore.QRect(730, 350, 61, 30))
        self.classDeletBtn.setObjectName("classDeletBtn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(340, 30, 231, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cropToolBtn = QtWidgets.QToolButton(self.widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/crop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cropToolBtn.setIcon(icon6)
        self.cropToolBtn.setObjectName("cropToolBtn")
        self.horizontalLayout.addWidget(self.cropToolBtn)
        self.widthLabel = QtWidgets.QLabel(self.widget)
        self.widthLabel.setObjectName("widthLabel")
        self.horizontalLayout.addWidget(self.widthLabel)
        self.widthSpinBox = QtWidgets.QSpinBox(self.widget)
        self.widthSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.widthSpinBox.setMaximum(1000)
        self.widthSpinBox.setObjectName("widthSpinBox")
        self.horizontalLayout.addWidget(self.widthSpinBox)
        self.lengthLabel = QtWidgets.QLabel(self.widget)
        self.lengthLabel.setObjectName("lengthLabel")
        self.horizontalLayout.addWidget(self.lengthLabel)
        self.lengthSpinBox = QtWidgets.QSpinBox(self.widget)
        self.lengthSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.lengthSpinBox.setMaximum(1000)
        self.lengthSpinBox.setObjectName("lengthSpinBox")
        self.horizontalLayout.addWidget(self.lengthSpinBox)
        self.cropStopToolBtn = QtWidgets.QToolButton(self.widget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/stoo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cropStopToolBtn.setIcon(icon7)
        self.cropStopToolBtn.setObjectName("cropStopToolBtn")
        self.horizontalLayout.addWidget(self.cropStopToolBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.iamgeLabel.setText(_translate("MainWindow", "图片："))
        self.imageOpenToolBtn.setText(_translate("MainWindow", "..."))
        self.addClassBtn.setText(_translate("MainWindow", "增加类别"))
        self.classLabel.setText(_translate("MainWindow", "类别："))
        self.classDeletBtn.setText(_translate("MainWindow", "删除类别"))
        self.cropToolBtn.setText(_translate("MainWindow", "..."))
        self.widthLabel.setText(_translate("MainWindow", "宽："))
        self.lengthLabel.setText(_translate("MainWindow", "长："))
        self.cropStopToolBtn.setText(_translate("MainWindow", "..."))

