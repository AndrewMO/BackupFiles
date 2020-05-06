# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading
import os


def upload(host, username, passwd, local, remote, file_type):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)

        if file_type == 1:
            print(' upload file on %s Start %s ' % (host, datetime.datetime.now()))
            sftp.put(local, remote)
            print('upload file on %s End %s ' % (host, datetime.datetime.now()))

        elif file_type == 2:

            files = os.listdir(local)
            for f in files:
                print(' upload file %s on %s Start %s ' % (str(f), host, datetime.datetime.now()))
                sftp.put(os.path.join(local, f), os.path.join(remote, f))
                print('upload file %s on %s End %s ' % (str(f), host, datetime.datetime.now()))
        else:
            raise Exception('invalid document type')





    except Exception as e:

        print('%s\t connect  error\n' % (host))
        print("-----------ExceptLog-----------")
        print(e)

    finally:
        trans.close()


def download(host, username, passwd, local, remote, file_type):
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
                print(' download file %s on %s Start %s ' % (str(f), host, datetime.datetime.now()))
                sftp.get(os.path.join(remote, f), os.path.join(local, f))
                print('download file %s on %s End %s ' % (str(f), host, datetime.datetime.now()))
        else:
            raise Exception('invalid document type')

    except Exception as e:

        print('%s\t connect  error\n' % (host))
        print("-----------ExceptLog-----------")
        print(e)

    finally:
        trans.close()


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    local_dir = '/Users/ajia/Documents/tmp/3000test/dump'
    remote_dir_servlet = '/opt/active/ActiveNet/perf/3000test/servlet'
    remote_dir_newcui = '/opt/active/ActiveNet/perf/3000test/newcui'


    print("Download dir......")

    for i in range(1, 2):
        # for i in range(20, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        print(host)

        download(host, username, passwd, local_dir, remote_dir_servlet, 2)
        download(host, username, passwd, local_dir, remote_dir_newcui, 2)
















