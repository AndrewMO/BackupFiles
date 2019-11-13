# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading

def upload(host, username, passwd,  src, des):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)
        print(' upload file on %s Start %s ' %( host, datetime.datetime.now()))
        # files = os.listdir(src)
        # for f in files:
        #         sftp.put(os.path.join(src,f),os.path.join(des,f))

        sftp.put(src,des)

        print('upload file on %s End %s ' % (host, datetime.datetime.now()))


        trans.close()

    except Exception as e:

        print('%s\t connect  error\n' %(host))
        print("-----------ExceptLog-----------")
        print(e)


if __name__ == '__main__':

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    IgnitecacheXml_servlet_srcfile = "/Users/ajia/Documents/tmp/Settings/ANE98095/Servlet/ignite-cache.xml"

    IgnitecacheXml_servlet_desfile = "/opt/active/sites/acm01vegasjetty/ActiveNetServlet/config/ignite-cache.xml"

    IgnitecacheXml_cache_srcfile = "/Users/ajia/Documents/tmp/Settings/ANE98095/Cache/ignite-cache.xml"

    IgnitecacheXml_cache_desfile = "/opt/active/sites/ignite01/ActiveNetServlet/config/ignite-cache.xml"



    # threads = []  # 多线程

    print("Begin......")

    # for i in range(1, 2):
    for i in range(1, 19):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'


        b = threading.Thread(target=upload, args=(host, username, passwd,  IgnitecacheXml_servlet_srcfile, IgnitecacheXml_servlet_desfile))
        b.start()




    for i in range(1, 3):

        if i < 10:
            host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

        c = threading.Thread(target=upload, args=(host, username, passwd,  IgnitecacheXml_cache_srcfile, IgnitecacheXml_cache_desfile))
        c.start()
