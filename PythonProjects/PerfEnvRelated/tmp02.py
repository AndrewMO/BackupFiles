# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading
import os

def upload(host, username, passwd,  local, remote):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)

        files = os.listdir(local)
        for f in files:
            print(' upload file %s on %s Start %s ' % ( str(f), host, datetime.datetime.now()))
            sftp.put(os.path.join(local, f), os.path.join(remote, f))
            print('upload file %s on %s End %s ' % (str(f), host, datetime.datetime.now()))

        # sftp.put(local, remote)

        trans.close()

    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)


def download(host, username, passwd,  local, remote):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)

        files = sftp.listdir(remote)

        for f in files:
            print(' download file %s on %s Start %s ' % (str(f), host, datetime.datetime.now()))
            sftp.get(os.path.join(remote, f), os.path.join(local, f))
            print('download file %s on %s End %s ' % (str(f), host, datetime.datetime.now()))

        # sftp.get(remote, local)

        trans.close()

    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    # IgnitecacheXml_localfile = "/Users/ajia/Documents/tmp/Settings/ftptest/service.properties"
    #
    # IgnitecacheXml_remotefile = "/opt/active/sites/ignite01/ActiveNetServlet/config/ignite-cache.xml"

    # ServiceProperties_localfile = "/Users/ajia/Documents/tmp/Settings/codecache/new/service.properties"
    ServiceProperties_localfile = "/Users/ajia/Documents/tmp/Settings/codecache/origin/service.properties"

    ServiceProperties_remotefile = "/opt/active/sites/perf03/ActiveNetServlet/config/service.properties"

    test_local = "/Users/ajia/Documents/tmp/FTPTest"

    test_remote = "/opt/active/sites/acm01vegas/ActiveNetServlet/logs"
    test_remote2 = "/opt/active/ActiveNet/perf"


    threads = []  # 多线程

    print("Begin......")


    for i in range(19, 20):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        # a = threading.Thread(target=upload, args=(host, username, passwd,  IgnitecacheXml_srcfile, IgnitecacheXml_desfile))
        # b = threading.Thread(target=upload, args=(host, username, passwd,  ServiceProperties_localfile, ServiceProperties_remotefile))
        # b = threading.Thread(target=download, args=(host, username, passwd,  test_local, test_remote))
        # # a.start()
        # b.start()



        # download(host, username, passwd,  test_local, test_remote)
        upload(host, username, passwd,  test_local, test_remote2)
