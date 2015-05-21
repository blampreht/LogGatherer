############################################
#
# WorkingClass: A class that holds all
#               return codes used
#
# Author: blaz.lampreht@gmail.com
#
############################################

NO_ERROR      =  0
IO_ERROR      = -1
NO_PATH_ERROR = -2

MISSING_DB_ERROR   = -3
MISSING_INFO_ERROR = -4
SSH_ERROR          = -5
NO_SYSLOG_NAME     = -6
SYSLOG_NOTEXIST    = -7
ERROR_GETING_LOG   = -8


def returnErrorMessage(error_code):

    message = ""

    if error_code == NO_ERROR:
        message = "No error"
    elif error_code == IO_ERROR:
        message = "Error: There was a problem with input/output."
    elif error_code == NO_PATH_ERROR:
        message = "Error: The path specified is missing."
    elif error_code == MISSING_DB_ERROR:
        message = "Error: The specified database file cannot be read."
    elif error_code == MISSING_INFO_ERROR:
        message = "Error: The info about a server is missing or unknown."
    elif error_code == SSH_ERROR:
        message = "Error: There was an error connecting via SSH."
    elif error_code == NO_SYSLOG_NAME:
        message = "Error: No syslog name returned."
    elif error_code == SYSLOG_NOTEXIST:
        message = "Error: The specified syslog does not exist or cannot be found."
    elif error_code == ERROR_GETING_LOG:
        message = "Error: There was an error getting the log."
    else:   # default
        message = "Error: Unknown error."
    return message
