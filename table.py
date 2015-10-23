# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputTable_UI.ui'
#
# Created: Fri Oct 23 13:18:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(707, 426)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.insert_row = QtGui.QPushButton(Form)
        self.insert_row.setObjectName(_fromUtf8("insert_row"))
        self.horizontalLayout.addWidget(self.insert_row)
        self.DeleteCurrentRow = QtGui.QPushButton(Form)
        self.DeleteCurrentRow.setObjectName(_fromUtf8("DeleteCurrentRow"))
        self.horizontalLayout.addWidget(self.DeleteCurrentRow)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtGui.QFrame.Box)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setMidLineWidth(2)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.insert_row.setText(_translate("Form", "Insert Row at Bottom", None))
        self.DeleteCurrentRow.setText(_translate("Form", "Delete Selected Row", None))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Obj", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "STO", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Img", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Surface", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Radius", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Thickness", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Glass", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Semi-Diameter", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Conic", None))

