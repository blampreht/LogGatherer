__author__ = 'Luka.Grah'

import paramiko
import sqlite3
import os
import time

def connect_database(database):
    if os.path.exists(database):
        db = sqlite3.connect(database)
        return db
    else:
        return None


def connect_ssh(username,password,hostname):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    return ssh


def transfer_file(ssh, path,localfile):
     if remote_file_exists(ssh,path):
         try:
            sftp = ssh.open_sftp()
            sftp.get(path,localfile)
         except IOError, e:
            if e[0] == 2:
                return False
            raise
         else:
            return True
     return False

def remote_file_exists(ssh, path):
    try:
        sftp = ssh.open_sftp()
        sftp.stat(path)
    except IOError, e:
        if e[0] == 2:
            return False
        raise
    else:
        return True

def get_os_type(ssh):
    stdin, stdout, stderr = ssh.exec_command('uname')
    stdin.close()
    os_type= stdout.read().splitlines()
    return os_type[0]

def get_distro_type(ssh, db):
    cursor = db.execute('select distro_name,version_file from linux_distro')
    all_rows = cursor.fetchall()
    for row in all_rows:
        if remote_file_exists(ssh, row[1]):
          return row[0]

def get_syslog_filename(ssh,db,distro):
    cursor = db.execute('select system_log_file from linux_distro where distro_name=?',(distro,))
    first_row=cursor.fetchone()
    return first_row[0]

def get_aix_version(ssh):
    stdin, stdout, stderr = ssh.exec_command('oslevel -r')
    stdin.close()
    os_type= stdout.read().splitlines()
    return os_type[0]

def get_sunos_version(ssh):
    stdin, stdout, stderr = ssh.exec_command('uname -v')
    stdin.close()
    os_type= stdout.read().splitlines()
    return os_type[0]

def remote_execute(ssh,command):
    stdin, stdout, stderr = ssh.exec_command(command)
    stdin.close()
    sshdata = stdout.readlines()
    return sshdata

def get_distro_version(ssh,distro_type):
    if distro_type == 'RedHat':
        os_version= remote_execute(ssh,'cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//')
        return os_version[0]
    if distro_type == 'SUSE':
        os_version= remote_execute(ssh,'cat /etc/SuSE-release | tr "\n" ' ' | sed s/.*=\ //')
        return os_version[0]
    if distro_type =='Debian':
        os_version= remote_execute(ssh,'cat /etc/debian_version')
        return os_version[0]


#http://www.unix.com/unix-for-advanced-and-expert-users/21468-machine.html#post83185
def host_discovery(username,password,hostname,db):
    ssh_connection = connect_ssh(username,password,hostname)
    os_type = get_os_type(ssh_connection)
    if os_type == 'Linux':
        distro_type = get_distro_type(ssh_connection,db)
        os_version = get_distro_version(ssh_connection,distro_type)
        return os_type,distro_type,os_version
    if os_type =='AIX':
        os_version= get_aix_version(ssh_connection)
        distro_type = os_type
        return os_type,distro_type,os_version
    if os_type=='SunOS':
        os_version = get_sunos_version(ssh_connection)
        distro_type= os_type
        return os_type,distro_type,os_version


def get_log(ssh,remote_logfile,local_destination):
    if transfer_file(ssh,remote_logfile,local_destination):
        return True
    else:
        return False

def get_command(ssh,command,local_output):
    command_output=remote_execute(ssh,command)
    output_file = open(local_output,'w')
    output_file.write("Command: "+command + " \n")
    output_file.write("Date & Time: "+time.strftime("%c")+ " \n")
    for line in command_output:
        output_file.write(line)
    output_file.close()


