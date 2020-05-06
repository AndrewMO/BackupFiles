# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading
import os

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

    # test_local = "/Users/ajia/Documents/tmp/FTPTest"
    # test_local_file = "/Users/ajia/Documents/tmp/FTPTest/test.txt"
    #
    # test_remote = "/opt/active/sites/perf03/ActiveNetServlet/logs"
    # test_remote_file = "/opt/active/ActiveNet/perf/test.txt"
    #
    #
    # local_file = "/Users/ajia/Documents/tmp/Settings/atmoic/ignite-cache.xml"
    # # remote_file = "/opt/active/sites/acm01vegas/ActiveNetServlet/config/ignite-cache.xml"
    # remote_file = "/opt/active/sites/ignite01/ActiveNetServlet/config/ignite-cache.xml"
    #
    #
    # local_dir_ignite = '/Users/ajia/Documents/tmp/init_log/ignite03'
    # local_dir_19 = '/Users/ajia/Documents/tmp/init_log/19'
    # local_dir_20 = '/Users/ajia/Documents/tmp/init_log/20'
    #
    # remote_dir_ignite = '/opt/active/sites/ignite01/ActiveNetServlet/logs'
    # remote_dir_19 = '/opt/active/sites/acm01vegas/ActiveNetServlet/logs'
    # remote_dir_20 = '/opt/active/sites/acm01vegas/ActiveNetServlet/logs'


    # threads = []  # 多线程

    print("Begin......")

    # for i in range(1, 3):
    #
    #     if i < 10:
    #         host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

    for i in range(1, 2):
    # for i in range(20, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        print(host)

        local_jettyxml = '/Users/ajia/Documents/tmp/3000test/pre/jetty.xml'
        remote_jettyxml = '/opt/active/sites/acm01vegasjetty/ActiveNetServlet/config/jetty.xml'

        local_serviceproperties = '/Users/ajia/Documents/tmp/3000test/pre/service.properties'
        remote_serviceproperties = '/opt/active/sites/acm01vegasjetty/ActiveNetServlet/config/service.properties'

        download(host, username, passwd,  local_jettyxml, remote_jettyxml, 1)
        download(host, username, passwd,  local_serviceproperties, remote_serviceproperties, 1)



        local_jettyxml_new = '/Users/ajia/Documents/tmp/3000test/new/jetty.xml'
        local_serviceproperties_new = '/Users/ajia/Documents/tmp/3000test/new/service.properties'





    # for i in range(3, 4):
    #
    #     if i < 10:
    #         host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

        #upload, file =1, folder = 2
        #file
        # a = threading.Thread(target=upload, args=(host, username, passwd,  test_local_file, test_remote_file, 1))
        #folder
        # a = threading.Thread(target=upload, args=(host, username, passwd, test_local, test_remote, 2))
        # a.start()
        # a.join()

        #download, file =1, folder = 2
        #file
        # b = threading.Thread(target=upload, args=(host, username, passwd,  local_file, remote_file, 1))
        #folder
        # b = threading.Thread(target=download, args=(host, username, passwd,  local_dir, remote_dir, 2))
        # b.start()
        # b.join()


