# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading

def upload(host, username, passwd,  local, remote):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)
        print(' upload file on %s Start %s ' %( host, datetime.datetime.now()))
        # files = os.listdir(src)
        # for f in files:
        #         sftp.put(os.path.join(src,f),os.path.join(des,f))

        sftp.put(local, remote)

        print('upload file on %s End %s ' % (host, datetime.datetime.now()))


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
        print(' download file on %s Start %s ' %( host, datetime.datetime.now()))
        # files = os.listdir(src)
        # for f in files:
        #         sftp.put(os.path.join(src,f),os.path.join(des,f))

        sftp.get(remote, local)

        print('download file on %s End %s ' % (host, datetime.datetime.now()))


        trans.close()

    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    # IgnitecacheXml_localfile = "D:\\tmp\\ANE89789\\Cache\\ignite-cache.xml"
    #
    # IgnitecacheXml_remotefile = "/opt/active/sites/ignite01/ActiveNetServlet/config/ignite-cache.xml"

    ServiceProperties_localfile = "/Users/ajia/Documents/tmp/Settings/ftptest/service.properties"

    ServiceProperties_remotefile = "/opt/active/sites/perf03/ActiveNetServlet/config/service.properties"


    threads = []  # 多线程

    print("Begin......")

    # for i in range(1, 3):
    #
    #     if i < 10:
    #         host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

    for i in range(19, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        # a = threading.Thread(target=upload, args=(host, username, passwd,  IgnitecacheXml_srcfile, IgnitecacheXml_desfile))
        b = threading.Thread(target=upload, args=(host, username, passwd,  ServiceProperties_localfile, ServiceProperties_remotefile))
        # b = threading.Thread(target=download, args=(host, username, passwd,  ServiceProperties_localfile, ServiceProperties_remotefile))
        # a.start()
        b.start()
