#!/usr/bin/python
# coding=utf-8

############################################
#
# LogGatherer: main class
#
#
# Author: blaz.lampreht@gmail.com
#
############################################

## imports ##

import sys
from PyQt4 import QtCore, QtGui
from sceleton import Ui_sceleton
from generictab import genericTab
import WorkingClass
import error

## Class ##

class StartQT4(QtGui.QMainWindow):
    ## Main init function

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_sceleton()
        self.ui.setupUi(self)

        # Move to center screen:

        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Signals and slots

        QtCore.QObject.connect(self.ui.actionE_xit, QtCore.SIGNAL("triggered()"), self.AppExit)
        QtCore.QObject.connect(self.ui.action_New_logger, QtCore.SIGNAL("triggered()"), self.NewLogger)
        QtCore.QObject.connect(self.ui.tabWidget, QtCore.SIGNAL("tabCloseRequested(int)"), self.CloseTab)
        QtCore.QObject.connect(self.ui.action_Open, QtCore.SIGNAL("triggered()"), self.OpenLogger)
        QtCore.QObject.connect(self.ui.action_Save_logger, QtCore.SIGNAL("triggered()"), self.SaveLogger)

        QtCore.QObject.connect(self.ui.btnGetLogs,QtCore.SIGNAL("clicked()"), self.GetLogs)



    ## Slot function for File->New Logger: Opens a new tab

    def NewLogger(self):

        currentTabWidgetSize = self.ui.tabWidget.count();

        tab = genericTab(None, QtCore.Qt.WindowFlags(), "")

        currentTabWidgetSize = self.ui.tabWidget.count();

        if currentTabWidgetSize < 10:
            self.ui.tabWidget.addTab(tab, QtCore.QString('NewTab_0' + str(currentTabWidgetSize)))
        else:
            self.ui.tabWidget.addTab(tab, QtCore.QString('NewTab_' + str(currentTabWidgetSize)))

        self.ui.tabWidget.setCurrentIndex(currentTabWidgetSize)


    def AppExit(self):
        sys.exit(0)


    ## Slot function for File->Open Logger:

    def OpenLogger(self):

        path2hostfile = ""

        filedialog = QtGui.QFileDialog(self)
        path2hostfile = filedialog.getOpenFileName(caption="Open logger file", filter="Logger files [*.lhost](*.lhost)")


        tab = genericTab(None, QtCore.Qt.WindowFlags(), path2hostfile)

        currentTabWidgetSize = self.ui.tabWidget.count();

        if path2hostfile:
            title = path2hostfile.split("/")

        self.ui.tabWidget.addTab(tab, QtCore.QString(title[len(title)-1]))
        self.ui.tabWidget.setCurrentIndex(currentTabWidgetSize)


    def SaveLogger(self):

        path2savefile = ""

        wc = WorkingClass.WorkingClass()

        filedialog = QtGui.QFileDialog(self)
        path2savefile = filedialog.getSaveFileName(caption="Enter logger filename", filter="Logger files [*.lhost](*.lhost)")


        if path2savefile:

            fileparts = path2savefile.split(".")
            title     = path2savefile.split("/")

            if fileparts[len(fileparts)-1] != "lhost":
                path2savefile = path2savefile + ".lhost"

            if wc.saveContentsToFile(path2savefile, self.ui.tabWidget.currentWidget()) == error.NO_ERROR:
                self.ui.tabWidget.setTabText(self.ui.tabWidget.currentIndex(), title[len(title)-1])
            else:
                QtGui.QMessageBox.warning(self, "Error saving file", "There was an error saving file !")

    ## Slot function that closes a tab

    def CloseTab(self, tabIdx):

        removedWidget = self.ui.tabWidget.widget(tabIdx)
        self.ui.tabWidget.removeTab(tabIdx)

        removedWidget.close()
        removedWidget.deleteLater()

    def GetLogs(self):
        wc = WorkingClass.WorkingClass()
        retval = wc.getLogs(self.ui.tabWidget)

        #print "Return value: " + str(retval[1])

        if retval[1] != error.NO_ERROR:
            QtGui.QMessageBox.warning(self, "Error getting logs.", "Error doing as requested on tab: " + str(retval[0]+1))
        else:
            QtGui.QMessageBox.warning(self,"Success","All logs successfully gathered.")


## Main function - application start

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
