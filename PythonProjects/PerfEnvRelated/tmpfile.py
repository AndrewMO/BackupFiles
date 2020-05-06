# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading
import os




def get_current_orgname(host, username, passwd, cmd):
    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)

        for m in cmd:

            stdin, stdout, stderr = ssh.exec_command(m)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出

            for o in out:
                print("%s  : %s" % (host, o))
                # print("\033[0;37;40m%s\033[0m : %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except:

        print('%s\tError\n' %(host))

def upload(host, username, passwd,  local, remote, file_type):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)

        if file_type == 1:
            print(' upload file on %s Start %s ' % ( host, datetime.datetime.now()))
            sftp.put(local, remote)
            print('upload file on %s End %s ' % ( host, datetime.datetime.now()))

        elif file_type == 2:

            files = os.listdir(local)
            for f in files:
                print(' upload file %s on %s Start %s ' % (str(f), host, datetime.datetime.now()))
                sftp.put(os.path.join(local, f), os.path.join(remote, f))
                print('upload file %s on %s End %s ' % (str(f), host, datetime.datetime.now()))
        else:
            raise Exception('invalid document type')





    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)

    finally:
        trans.close()


def download(host, username, passwd,  local, remote, file_type):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)

        if file_type == 1:
            print(' download file on %s Start %s ' % (host, datetime.datetime.now()))
            sftp.get(remote, local)
            print('download file on %s End %s ' % (host, datetime.datetime.now()))

        elif file_type == 2:
            files = sftp.listdir(remote)

            for f in files:
                if '.log' in f:
                    print(' download file %s on %s Start %s ' % (str(f), host, datetime.datetime.now()))
                    sftp.get(os.path.join(remote, f), os.path.join(local, f))
                    print('download file %s on %s End %s ' % (str(f), host, datetime.datetime.now()))
        else:
            raise Exception('invalid document type')

    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)

    finally:
        trans.close()


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    cmd_getorgname = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1 | awk \'{print $13}\' | awk -F \'/\' \'{print $5}\'']

    local_dir_ignite = '/Users/ajia/Documents/tmp/error_logs/Cache_03W'
    local_dir_19 = '/Users/ajia/Documents/tmp/error_logs/AUI_19'
    local_dir_20 = '/Users/ajia/Documents/tmp/error_logs/AUI_20'

    remote_dir_ignite = '/opt/active/sites/ignite01/ActiveNetServlet/logs'



    # threads = []  # 多线程

    print("Begin......")
    print("AUI Server..")
    for i in range(19, 20):
        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        #download, file =1, folder = 2
        #folder
        if i == 19:
            orgname_19_list = get_current_orgname(host, username, passwd, cmd_getorgname)
            orgname_19 = ''.join(orgname_19_list).strip()
            remote_dir_19 = '/opt/active/sites/' + orgname_19 + '/ActiveNetServlet/logs'
            print(remote_dir_19)
            download(host, username, passwd,  local_dir_19, remote_dir_19, 2)
        elif i == 20:
            orgname_20_list = get_current_orgname(host, username, passwd, cmd_getorgname)
            orgname_20 = ''.join(orgname_20_list).strip()
            remote_dir_20 = '/opt/active/sites/' + orgname_20 + '/ActiveNetServlet/logs'
            print(remote_dir_20)
            download(host, username, passwd,  local_dir_20, remote_dir_20, 2)
        else:
            print("no host is found")

    # print("Cache Server..")
    #
    # for i in range(3, 4):
    #
    #     if i < 10:
    #         host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-ignite-' + str(i) + 'w.an.active.tan'
    #
    #     #download, file =1, folder = 2
    #     #folder
    #     download(host, username, passwd, local_dir_ignite, remote_dir_ignite, 2)

    print("End......")


