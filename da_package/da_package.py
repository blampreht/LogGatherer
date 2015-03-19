__author__ = 'Luka.Grah'

import paramiko
import sqlite3
import os

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
    cursor = db.execute('select id,version_file from linux_distro')
    all_rows = cursor.fetchall()
    for row in all_rows:
        if remote_file_exists(ssh, row[1]):
          return row[0]

def get_syslog_filename(ssh,db,distro):
    cursor = db.execute('select system_log_file from linux_distro where distro_name=?',(distro,))
    first_row=cursor.fetchone()
    return first_row[0]

def add_server(hostname,username,password,db):
    db.execute('insert into servers (hostname,username,password) values (?,?,?)',(hostname,username,password,))
    db.commit()
    cursor_select=db.execute('select id from servers where hostname=?',(hostname,))
    id=cursor_select.fetchone()
    return id

def delete_server(hostname,db):
    #set active_record to 0 for the host
    cursor = db.execute('update servers set active_record=0 where hostname=?',(hostname,))
    db.commit()

def register_host(hostname,db):
    cursor_get_host =db.execute('select username,password from servers_where hostname=?',(hostname,))
    row = cursor_get_host.fetchone()
    ssh = connect_ssh(row[0],row[1],hostname)
    distro_id= get_distro_type(ssh, db)
    cursor_select=db.execute('select id from servers_where hostname=?',(hostname,))
    id=cursor_select.fetchone()
    db.execute('update servers set discovered=1 where ID=?',(id,))
    db.execute('update servers set linx_distro_id=? where ID=?',(id,distro_id,))
    db.commit()

#def set_server_logs(hostname,db):
#    cursor_select=db.execute('select id from servers_where hostname=?',(hostname,))
#    id=cursor_select.fetchone()

    #cursor = db.execute('update servers set discovered=1 ID=?',(id,))


# TODO
# def write_logfile
# def add_log(lcation, server, distribution)
# def get_ logs (db,hostname)
# def discover
# def list_servers
# config_file

