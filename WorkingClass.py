import os.path
from PyQt4 import QtGui

#
# Class that contains worker functions
#
class WorkingClass(object):


    #
    # Constructor
    #

    def __init__(self):
        nothing=0


    #
    # Function that returns file parameters
    #
    def returnFileContents(self, hostfile):

        params = []
        paramlist = []

        if os.path.exists(hostfile):


            with open(hostfile, "r") as lhostfile:

                for i in lhostfile:
                    params.append(i.strip())

            ##
            #
            # Host parameters array:
            # paramlist[0] = ip_hostname
            # paramlist[1] = username
            # paramlist[2] = sosreport (yes/no)
            # paramlist[3] = oralogs (yes/no)
            # paramlist[4] = Path for log files
            #
            ##


            for i in range(0, len(params), 1):
                tmp = params[i].split("=")
                paramlist.append(tmp[1])

        return paramlist

    #
    # Function that saves parameters to file
    #
    def saveContentsToFile(self, filename, currentTab=QtGui.QTabWidget):

        NO_ERROR = 0
        ERROR    = -1

        retval = NO_ERROR

        hostname  = ""
        username  = ""
        oralogs   = ""
        linuxlogs = ""
        path2save = ""

        if currentTab:
            hostname  = currentTab.lineEdit_2.text()
            username  = currentTab.lineEdit_3.text()

            if currentTab.chkOracle.isChecked():
                oralogs   = "yes"
            else:
                oralogs   = "no"

            if currentTab.chkLinux.isChecked():
                linuxlogs   = "yes"
            else:
                linuxlogs   = "no"

            path2save = currentTab.leLogs.text()

        try:

            write_file = open(filename, "w")
            write_file.write("iphostname=" + str(hostname) + "\nusername="+str(username)+"\nsosreport=" + str(linuxlogs) + "\noralogs=" + str(oralogs) + "\npath2logs=" + str(path2save) + "\n")

            write_file.close()

        except IOError:
            retval = ERROR

        return retval

    #
    # Function that does all the work: it finally gets the damn logs :)
    #
    def getLogs(self, tabWidget = QtGui.QTabWidget):

        print "Getting logs .... all " + str(tabWidget.count()) + " of them :)"

        for i in range(0, tabWidget.count(), 1):
            print "Username " + str(i) + ": " + str(tabWidget.widget(i).lineEdit_2.text()) + "\n"
