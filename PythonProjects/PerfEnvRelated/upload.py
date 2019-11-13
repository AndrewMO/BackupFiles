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

    ServiceProperties_servlet_desfile = "/opt/active/sites/acm01vegas/ActiveNetServlet/config/service.properties"


    threads = []  # 多线程


    for i in range(20, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'


        b = threading.Thread(target=upload, args=(host, username, passwd,  ServiceProperties_servlet_srcfile, ServiceProperties_servlet_desfile))
        b.start()

    print("servlet service properties done -- ")


    print("servlet service properties -- ")


    SdiIni_servlet_srcfile = "/Users/ajia/Documents/tmp/Settings/ServletSettings/sdi.ini"

    SdiIni_servlet_desfile = "/opt/active/sites/acm01vegas/ActiveNetServlet/config/sdi.ini"


    threads = []  # 多线程


    for i in range(20, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'


        b = threading.Thread(target=upload, args=(host, username, passwd,  SdiIni_servlet_srcfile, SdiIni_servlet_desfile))
        b.start()

    print("servlet service properties done -- ")



