import paramiko
import sys
import os
import sqlite3


distro_list ={}

#variable list
cmd_uname="uname"
linux_distro_list="linux_distro.txt"
localpath="C:/razvoj/loggetter/discovery/test.txt"

def connect_database():
    db = sqlite3.connect('disco.db')
    return db

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

def prepare_distro_table(file,distro_list):
    file_name= open(file, 'r')
    for line in file_name:
        distro,distro_file = line.split(':')
        distro_list[distro]=distro_file
    return distro_list

def prepare_ssh(username,password,hostname):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    return ssh

def transfer_file(ssh, path,localpath):
     try:
        sftp = ssh.open_sftp()
        sftp.get(path,localpath)
     except IOError, e:
        if e[0] == 2:
            return False
        raise
     else:
        return True
# predelaj kot remote_exists
def prepare_sftp(username,password,hostname):
    transport = paramiko.Transport((hostname, 22))
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    return sftp

def get_os (ssh):
    stdin, stdout, stderr = ssh.exec_command(cmd_uname)
    stdin.close()
    os_type= stdout.read().splitlines()
    return os_type[0]

def getfile_content(ssh,file):
    get_file ="cat "+file
    #sprint get_file
    stdin, stdout, stderr = ssh.exec_command(get_file)
    stdin.close()
    return stdout.read().splitlines()[0]

def get_remote_file(sftp, file,localpath):
    sftp.get(file, localpath)

def check_distro(ssh, db):
    cursor = db.execute('select distro_name,version_file from linux_distro')
    all_rows = cursor.fetchall()
    for row in all_rows:
        if remote_exists(ssh, row[1]):
          return row[0]


def main():
    host_ssh =prepare_ssh("root","","")
    sftp = prepare_sftp("root","","")
    db =connect_database()
    os_type = get_os(host_ssh)
    if os_type == 'Linux':
        distro = check_distro(host_ssh,db)
        #get syslog
        syslog =get_syslog(host_ssh,db,distro)
        #get_remote_file(sftp, syslog,localpath)
        ##run sosreport
        # oracle discovery
        transfer_file(host_ssh,syslog,localpath)

if __name__ == '__main__':
    main()