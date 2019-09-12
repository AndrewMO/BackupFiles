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

    StartServiceSH_srcfile = "/Users/ajia/Documents/tmp/Settings/CMS/Servlet/start_service.sh"

    StartServiceSH_desfile = "/opt/active/sites/acm01vegasjetty/ActiveNetServlet/config/start_service.sh"



    threads = []  # 多线程

    print("Begin......")

    for i in range(1, 19):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        a = threading.Thread(target=upload, args=(host, username, passwd,  StartServiceSH_srcfile, StartServiceSH_desfile))
        a.start()

