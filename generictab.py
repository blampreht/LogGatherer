# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generictab.ui'
#
# Created: Tue Feb 24 09:22:00 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

#############################################
#
# generictab: A class that holds definitions
#             for widgets for the generic tab
#
# Author: blaz.lampreht@gmail.com
#
#############################################

from PyQt4 import QtCore, QtGui
import WorkingClass

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

class Ui_genericTab(object):
    def setupUi(self, genericTab):
        genericTab.setObjectName(_fromUtf8("genericTab"))
        genericTab.resize(535, 380)
        genericTab.setMinimumSize(QtCore.QSize(535, 380))
        genericTab.setMaximumSize(QtCore.QSize(535, 380))
        self.groupBox_2 = QtGui.QGroupBox(genericTab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 180, 531, 201))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox { \n"
"    font:10pt \"URW Gothic L\";\n"
"    color: blue;\n"
"    border: 2px groove rgb(220,220,220); \n"
"    border-radius: 5px; \n"
"    margin-top: 7px; \n"
"    margin-bottom: 7px; \n"
"    padding: 0px\n"
"} \n"
"\n"
"QGroupBox::title {\n"
"    top:-7 ex;\n"
"    left: 10px; \n"
"    subcontrol-origin: border\n"
"}\n"
"\n"
""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.chkOracle = QtGui.QCheckBox(self.groupBox_2)
        self.chkOracle.setGeometry(QtCore.QRect(20, 50, 121, 21))
        self.chkOracle.setObjectName(_fromUtf8("chkOracle"))
        self.chkLinux = QtGui.QCheckBox(self.groupBox_2)
        self.chkLinux.setGeometry(QtCore.QRect(20, 100, 421, 21))
        self.chkLinux.setObjectName(_fromUtf8("chkLinux"))
        self.lblSaveLogs2 = QtGui.QLabel(self.groupBox_2)
        self.lblSaveLogs2.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.lblSaveLogs2.setObjectName(_fromUtf8("lblSaveLogs2"))
        self.leLogs = QtGui.QLineEdit(self.groupBox_2)
        self.leLogs.setGeometry(QtCore.QRect(110, 155, 301, 23))
        self.leLogs.setObjectName(_fromUtf8("leLogs"))
        self.btnBrowse = QtGui.QPushButton(self.groupBox_2)
        self.btnBrowse.setGeometry(QtCore.QRect(420, 155, 100, 24))
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.groupBox = QtGui.QGroupBox(genericTab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 531, 171))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox { \n"
"    font:10pt \"URW Gothic L\";\n"
"    color: blue;\n"
"    border: 2px groove rgb(220,220,220); \n"
"    border-radius: 5px; \n"
"    margin-top: 7px; \n"
"    margin-bottom: 7px; \n"
"    padding: 0px\n"
"} \n"
"\n"
"QGroupBox::title {\n"
"    top:-7 ex;\n"
"    left: 10px; \n"
"    subcontrol-origin: border\n"
"}\n"
"\n"
""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblhostname = QtGui.QLabel(self.groupBox)
        self.lblhostname.setGeometry(QtCore.QRect(20, 40, 151, 16))
        self.lblhostname.setObjectName(_fromUtf8("lblhostname"))
        self.lblUsername = QtGui.QLabel(self.groupBox)
        self.lblUsername.setGeometry(QtCore.QRect(20, 80, 151, 16))
        self.lblUsername.setObjectName(_fromUtf8("lblUsername"))
        self.lblPassword = QtGui.QLabel(self.groupBox)
        self.lblPassword.setGeometry(QtCore.QRect(20, 120, 151, 16))
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 35, 321, 23))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 75, 321, 23))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 115, 321, 23))
        self.lineEdit_4.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.retranslateUi(genericTab)
        QtCore.QMetaObject.connectSlotsByName(genericTab)

    def retranslateUi(self, genericTab):
        genericTab.setWindowTitle(_translate("genericTab", "Form", None))
        self.groupBox_2.setTitle(_translate("genericTab", "Log gathering", None))
        self.chkOracle.setText(_translate("genericTab", "Oracle logs", None))
        self.chkLinux.setText(_translate("genericTab", "Linux system logs (actually does a sosreport)", None))
        self.lblSaveLogs2.setText(_translate("genericTab", "Save logs to:", None))
        self.btnBrowse.setText(_translate("genericTab", "Browse...", None))
        self.groupBox.setTitle(_translate("genericTab", "Credentials", None))
        self.lblhostname.setText(_translate("genericTab", "Hostname/IP Address:", None))
        self.lblUsername.setText(_translate("genericTab", "Username:", None))
        self.lblPassword.setText(_translate("genericTab", "Password:", None))


class genericTab(QtGui.QWidget, Ui_genericTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags(), hostfile=""):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

        QtCore.QObject.connect(self.btnBrowse,QtCore.SIGNAL("clicked()"), self.browseFolder)

        ## Read the file

        wc = WorkingClass.WorkingClass()
        paramlist = wc.returnFileContents(hostfile)

        #
        # If parameter list is not empty, populate form
        #
        if paramlist:

            self.lineEdit_2.setText(str(paramlist[0]))
            self.lineEdit_3.setText(str(paramlist[1]))

            if str(paramlist[2])=="yes":
                self.chkLinux.setChecked(True)

            if str(paramlist[3])=="yes":
                self.chkOracle.setChecked(True)

            self.leLogs.setText(str(paramlist[4]))


    def browseFolder(self):
        fd = QtGui.QFileDialog(self)
        path2Logs = fd.getExistingDirectory()
        self.leLogs.setText(path2Logs)

