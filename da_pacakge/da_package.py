__author__ = 'Luka.Grah'

import paramiko
import sqlite3

def connect_database(database):
    db = sqlite3.connect(database)
    return db

def ssh(username,password,hostname):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    return ssh


def transfer_file(ssh, path,localpath):
     if remote_exists(ssh,path):
         try:
            sftp = ssh.open_sftp()
            sftp.get(path,localpath)
         except IOError, e:
            if e[0] == 2:
                return False
            raise
         else:
            return True
     return False

def remote_exists(ssh, path):
    try:
        sftp = ssh.open_sftp()
        sftp.stat(path)
    except IOError, e:
        if e[0] == 2:
            return False
        raise
    else:
        return True

def get_os_type (ssh):
    stdin, stdout, stderr = ssh.exec_command('uname')
    stdin.close()
    os_type= stdout.read().splitlines()
    return os_type[0]

def check_distro(ssh, db):
    cursor = db.execute('select distro_name,version_file from linux_distro')
    all_rows = cursor.fetchall()
    for row in all_rows:
        if remote_exists(ssh, row[1]):
          return row[0]

def get_syslog(ssh,db,distro):
    cursor = db.execute('select system_log_file from linux_distro where distro_name=?',(distro,))
    first_row=cursor.fetchone()
    return first_row[0]

