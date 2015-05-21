# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sceleton.ui'
#
# Created: Fri Mar 20 14:46:49 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_sceleton(object):
    def setupUi(self, sceleton):
        sceleton.setObjectName(_fromUtf8("sceleton"))
        sceleton.resize(567, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sceleton.sizePolicy().hasHeightForWidth())
        sceleton.setSizePolicy(sizePolicy)
        sceleton.setMinimumSize(QtCore.QSize(567, 600))
        sceleton.setMaximumSize(QtCore.QSize(567, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        sceleton.setPalette(palette)
        self.centralwidget = QtGui.QWidget(sceleton)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnGetLogs = QtGui.QPushButton(self.centralwidget)
        self.btnGetLogs.setGeometry(QtCore.QRect(470, 530, 91, 23))
        self.btnGetLogs.setObjectName(_fromUtf8("btnGetLogs"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 9, 554, 500))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(554, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(554, 500))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        sceleton.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(sceleton)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        sceleton.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(sceleton)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        sceleton.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(sceleton)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.actionE_xit = QtGui.QAction(sceleton)
        self.actionE_xit.setObjectName(_fromUtf8("actionE_xit"))
        self.action_New_logger = QtGui.QAction(sceleton)
        self.action_New_logger.setObjectName(_fromUtf8("action_New_logger"))
        self.action_Save_logger = QtGui.QAction(sceleton)
        self.action_Save_logger.setObjectName(_fromUtf8("action_Save_logger"))
        self.menu_File.addAction(self.action_New_logger)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save_logger)
        self.menu_File.addAction(self.actionE_xit)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(sceleton)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(sceleton)

    def retranslateUi(self, sceleton):
        sceleton.setWindowTitle(_translate("sceleton", "Log Gatherer", None))
        self.btnGetLogs.setText(_translate("sceleton", "Get Logs !", None))
        self.menu_File.setTitle(_translate("sceleton", "&File", None))
        self.action_Open.setText(_translate("sceleton", "&Open logger", None))
        self.actionE_xit.setText(_translate("sceleton", "E&xit", None))
        self.action_New_logger.setText(_translate("sceleton", "&New logger", None))
        self.action_Save_logger.setText(_translate("sceleton", "&Save logger", None))

