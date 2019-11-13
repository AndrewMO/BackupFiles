# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading
import os

def upload(host, username, passwd,  src, des):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)
        print('upload file on %s start %s ' %( host, datetime.datetime.now()))
        sftp.put(src,des)
        print('upload file on %s end %s ' % (host, datetime.datetime.now()))


        trans.close()


    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ErrorLog-----------")
        print(e)


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码


    print("servlet service properties -- ")


    ServiceProperties_servlet_srcfile = "/Users/ajia/Documents/tmp/Settings/ServletSettings/service.properties"

    ServiceProperties_servlet_desfile = "/opt/active/sites/perf02/ActiveNetServlet/config/service.properties"


    threads = []  # 多线程

    print("Begin......")

    for i in range(19, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'


        b = threading.Thread(target=upload, args=(host, username, passwd,  ServiceProperties_servlet_srcfile, ServiceProperties_servlet_desfile))
        b.start()

    print("servlet service properties done -- ")


    print("cache service properties -- ")


    ServiceProperties_ignite_srcfile = "/Users/ajia/Documents/tmp/Settings/IgniteSettings/service.properties"

    ServiceProperties_ignite_desfile = "/opt/active/sites/ignite01/ActiveNetServlet/config/service.properties"


    print("Begin......")

    for i in range(1, 4, 2):

        if i < 10:
            host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-ignite-' + str(i) + 'w.an.active.tan'


        c = threading.Thread(target=upload, args=(host, username, passwd,  ServiceProperties_ignite_srcfile, ServiceProperties_ignite_desfile))
        c.start()

    print("cache service properties done -- ")
