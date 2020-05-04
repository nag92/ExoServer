# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Subject_Tester.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 295)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 10, 911, 213))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.boxSession = QtWidgets.QVBoxLayout()
        self.boxSession.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.boxSession.setContentsMargins(0, -1, 0, -1)
        self.boxSession.setObjectName("boxSession")
        self.btnStartSession = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartSession.sizePolicy().hasHeightForWidth())
        self.btnStartSession.setSizePolicy(sizePolicy)
        self.btnStartSession.setObjectName("btnStartSession")
        self.boxSession.addWidget(self.btnStartSession)
        self.OpenMonitor = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenMonitor.sizePolicy().hasHeightForWidth())
        self.OpenMonitor.setSizePolicy(sizePolicy)
        self.OpenMonitor.setObjectName("OpenMonitor")
        self.boxSession.addWidget(self.OpenMonitor)
        self.lblTrialNumber = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTrialNumber.sizePolicy().hasHeightForWidth())
        self.lblTrialNumber.setSizePolicy(sizePolicy)
        self.lblTrialNumber.setObjectName("lblTrialNumber")
        self.boxSession.addWidget(self.lblTrialNumber)
        self.gridLayout.addLayout(self.boxSession, 0, 1, 1, 1)
        self.boxTrial = QtWidgets.QVBoxLayout()
        self.boxTrial.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.boxTrial.setObjectName("boxTrial")
        self.btnStartTrial = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartTrial.sizePolicy().hasHeightForWidth())
        self.btnStartTrial.setSizePolicy(sizePolicy)
        self.btnStartTrial.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnStartTrial.setObjectName("btnStartTrial")
        self.boxTrial.addWidget(self.btnStartTrial)
        self.btnStop = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStop.sizePolicy().hasHeightForWidth())
        self.btnStop.setSizePolicy(sizePolicy)
        self.btnStop.setMaximumSize(QtCore.QSize(600, 16777215))
        self.btnStop.setObjectName("btnStop")
        self.boxTrial.addWidget(self.btnStop)
        self.gridLayout.addLayout(self.boxTrial, 0, 2, 1, 1)
        self.boxInfo = QtWidgets.QFormLayout()
        self.boxInfo.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.boxInfo.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.boxInfo.setObjectName("boxInfo")
        self.lblSubject = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblSubject.setObjectName("lblSubject")
        self.boxInfo.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblSubject)
        self.txtSubject = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtSubject.sizePolicy().hasHeightForWidth())
        self.txtSubject.setSizePolicy(sizePolicy)
        self.txtSubject.setMaximumSize(QtCore.QSize(500, 16777215))
        self.txtSubject.setObjectName("txtSubject")
        self.boxInfo.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtSubject)
        self.lblAge = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblAge.setObjectName("lblAge")
        self.boxInfo.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblAge)
        self.txtAge = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtAge.sizePolicy().hasHeightForWidth())
        self.txtAge.setSizePolicy(sizePolicy)
        self.txtAge.setMaximumSize(QtCore.QSize(500, 16777215))
        self.txtAge.setObjectName("txtAge")
        self.boxInfo.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtAge)
        self.lblGender = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblGender.setObjectName("lblGender")
        self.boxInfo.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblGender)
        self.txtGender = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtGender.sizePolicy().hasHeightForWidth())
        self.txtGender.setSizePolicy(sizePolicy)
        self.txtGender.setMaximumSize(QtCore.QSize(500, 16777215))
        self.txtGender.setObjectName("txtGender")
        self.boxInfo.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtGender)
        self.lblMass = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblMass.setObjectName("lblMass")
        self.boxInfo.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblMass)
        self.txtMass = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtMass.sizePolicy().hasHeightForWidth())
        self.txtMass.setSizePolicy(sizePolicy)
        self.txtMass.setMaximumSize(QtCore.QSize(500, 16777215))
        self.txtMass.setObjectName("txtMass")
        self.boxInfo.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtMass)
        self.xtxHeight = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xtxHeight.sizePolicy().hasHeightForWidth())
        self.xtxHeight.setSizePolicy(sizePolicy)
        self.xtxHeight.setMaximumSize(QtCore.QSize(500, 16777215))
        self.xtxHeight.setObjectName("xtxHeight")
        self.boxInfo.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.xtxHeight)
        self.lblLegLength = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblLegLength.setObjectName("lblLegLength")
        self.boxInfo.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.lblLegLength)
        self.txtLegLength = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtLegLength.sizePolicy().hasHeightForWidth())
        self.txtLegLength.setSizePolicy(sizePolicy)
        self.txtLegLength.setMaximumSize(QtCore.QSize(500, 16777215))
        self.txtLegLength.setObjectName("txtLegLength")
        self.boxInfo.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.txtLegLength)
        self.lblheight = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lblheight.setObjectName("lblheight")
        self.boxInfo.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.lblheight)
        self.gridLayout.addLayout(self.boxInfo, 0, 0, 1, 1)
        self.gridLayoutWidget.raise_()
        self.lblSubject.raise_()
        self.txtSubject.raise_()
        self.txtAge.raise_()
        self.lblAge.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 27))
        self.menubar.setObjectName("menubar")
        self.menuSubject = QtWidgets.QMenu(self.menubar)
        self.menuSubject.setObjectName("menuSubject")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSubject.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnStartSession.setText(_translate("MainWindow", "Start Session"))
        self.OpenMonitor.setText(_translate("MainWindow", "open monitor"))
        self.lblTrialNumber.setText(_translate("MainWindow", "Trial 00"))
        self.btnStartTrial.setText(_translate("MainWindow", "Record"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.lblSubject.setText(_translate("MainWindow", "Subject number"))
        self.lblAge.setText(_translate("MainWindow", "Age"))
        self.lblGender.setText(_translate("MainWindow", "Gender"))
        self.lblMass.setText(_translate("MainWindow", "Mass"))
        self.lblLegLength.setText(_translate("MainWindow", "Leg Length"))
        self.lblheight.setText(_translate("MainWindow", "Height"))
        self.menuSubject.setTitle(_translate("MainWindow", "Subject "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
