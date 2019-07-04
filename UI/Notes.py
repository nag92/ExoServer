# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Notes(object):

    def setupUi(self, Dialog, file_name):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 487)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 40, 621, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtNotes = QtWidgets.QTextEdit(self.widget)
        self.txtNotes.setObjectName("txtNotes")
        self.verticalLayout.addWidget(self.txtNotes)
        self.btnSave = QtWidgets.QPushButton(self.widget)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect( lambda:self.save_callback(file_name) )
        self.verticalLayout.addWidget(self.btnSave)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def save_callback(self,file_name):
        print "saving"
        text = str( self.txtNotes.toPlainText() )
        file = open(file_name + "_notes.txt", "w")
        file.write(text)
        file.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnSave.setText(_translate("Dialog", "Save"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())

