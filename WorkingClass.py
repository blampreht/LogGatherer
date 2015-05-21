############################################
#
# WorkingClass: A class that holds all
#               main worker functions
#
# Author: blaz.lampreht@gmail.com
#
############################################

import os.path
import da_package.da_package
import error
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

        retval = error.NO_ERROR

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
            retval = error.IO_ERROR

        return retval

    #
    # Function that does all the work: it finally gets the damn logs :)
    #
    def getLogs(self, tabWidget = QtGui.QTabWidget):

        retval = error.NO_ERROR
        tabnum = 0
        pathexists = error.NO_ERROR


        for i in range(0, tabWidget.count(), 1):

            tabnum = i+1
            taberror = 0

            ip_hostname = str(tabWidget.widget(i).lineEdit_2.text())
            username    = str(tabWidget.widget(i).lineEdit_3.text())
            password    = str(tabWidget.widget(i).lineEdit_4.text())

            oralogs   = False
            linuxlogs = False

            if tabWidget.widget(i).chkOracle.isChecked():
                oralogs = True

            if  tabWidget.widget(i).chkLinux.isChecked():
                linuxlogs = True

            savelogs2 = str(tabWidget.widget(i).leLogs.text())

            if not os.path.exists(savelogs2):
                pathexists = error.NO_PATH_ERROR
                taberror = tabnum
                break


            if pathexists == error.NO_ERROR:

                db = da_package.da_package.connect_database("disco.db")

                if db:

                    ssh = da_package.da_package.connect_ssh(username, password, ip_hostname)

                    if ssh:

                        distro = da_package.da_package.get_distro_type(ssh, db)
                        syslog = da_package.da_package.get_syslog_filename(ssh,db,distro)

                        syslog_filename = syslog.split('/')
                        syslog_filename = syslog_filename[-1]


                        if syslog:

                            if da_package.da_package.remote_file_exists(ssh,syslog):

                                if da_package.da_package.get_log(ssh, syslog, str(savelogs2+"/"+syslog_filename)):   # Prej je blo le savelogs2
                                    retval = error.NO_ERROR
                                else:
                                    retval = error.ERROR_GETING_LOG
                                    break

                            else:
                                retval = error.SYSLOG_NOTEXIST
                                break

                        else:
                            retval = error.NO_SYSLOG_NAME
                            break

                    else:
                        retval = error.SSH_ERROR
                        break

                else:
                    retval = error.MISSING_DB_ERROR
                    break


        return taberror, retval

    #
    # Function that does server discovery
    #
    def returnServerInfo(self, username, password, hostname):

        db = da_package.da_package.connect_database("disco.db")
        if not db:
            return error.MISSING_DB_ERROR

        serverinfo = da_package.da_package.host_discovery(username,password,hostname,db)

        #da_package.da_package.oracle_discovery(da_package.da_package.connect_ssh(username, password, hostname))

        return serverinfo
#
#        if serverinfo:
#            return serverinfo
#        else:
#            return error.MISSING_INFO_ERROR
