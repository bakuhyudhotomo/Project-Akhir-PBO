# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bakuh.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(435, 295)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 70, 282, 114))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.inputbilangan = QtWidgets.QLineEdit(self.widget)
        self.inputbilangan.setObjectName("inputbilangan")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.inputbilangan)
        self.inputbilanganproses = QtWidgets.QLineEdit(self.widget)
        self.inputbilanganproses.setObjectName("inputbilanganproses")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputbilanganproses)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Kali = QtWidgets.QPushButton(self.widget)
        self.Kali.setObjectName("Kali")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Kali)
        self.Bagi = QtWidgets.QPushButton(self.widget)
        self.Bagi.setObjectName("Bagi")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Bagi)
        self.Jumlah = QtWidgets.QPushButton(self.widget)
        self.Jumlah.setObjectName("Jumlah")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Jumlah)
        self.Kurang = QtWidgets.QPushButton(self.widget)
        self.Kurang.setObjectName("Kurang")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Kurang)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hasil :"))
        self.Kali.setText(_translate("Dialog", "Kali"))
        self.Bagi.setText(_translate("Dialog", "Bagi"))
        self.Jumlah.setText(_translate("Dialog", "Tambah"))
        self.Kurang.setText(_translate("Dialog", "Kurang"))
