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

    local_jettyxml = '/Users/ajia/Documents/tmp/3000test/pre/jetty.xml'
    remote_jettyxml = '/opt/active/sites/acm01vegasjetty/ActiveNetServlet/config/jetty.xml'

    local_serviceproperties = '/Users/ajia/Documents/tmp/3000test/pre/service.properties'
    remote_serviceproperties = '/opt/active/sites/acm01vegasjetty/ActiveNetServlet/config/service.properties'


    local_newcui_serviceproperties = '/Users/ajia/Documents/tmp/3000test/newcui/service.properties'
    remote_newcui_serviceproperties = '/opt/active/sites/acm01vegasjetty/ActiveNetCUI/config/service.properties'

    local_jettyxml_new = '/Users/ajia/Documents/tmp/3000test/new/jetty.xml'
    local_serviceproperties_new = '/Users/ajia/Documents/tmp/3000test/new/service.properties'

    # print("Download files......")
    #
    # for i in range(1, 2):
    #     # for i in range(20, 21):
    #
    #     if i < 10:
    #         host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-activenet-' + str(i) + 'w.an.active.tan'
    #
    #     print(host)
    #
    #     download(host, username, passwd, local_jettyxml, remote_jettyxml, 1)
    #     download(host, username, passwd, local_serviceproperties, remote_serviceproperties, 1)


    # for i in range(1, 2):
    #     # for i in range(20, 21):
    #
    #     if i < 10:
    #         host_newcui = 'perf-activenet-cui-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host_newcui = 'perf-activenet-cui-' + str(i) + 'w.an.active.tan'
    #
    #     print(host_newcui)
    #
    #     # download(host_newcui, username, passwd, local_jettyxml, remote_jettyxml, 1)
    #     download(host_newcui, username, passwd, local_newcui_serviceproperties, remote_newcui_serviceproperties, 1)


    #
    # print("Upload files......")
    # for i in range(1, 19):
    #     # for i in range(20, 21):
    #
    #     if i < 10:
    #         host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-activenet-' + str(i) + 'w.an.active.tan'
    #
    #     print(host)
    #
    #     upload(host, username, passwd, local_jettyxml_new, remote_jettyxml, 1)
    #     upload(host, username, passwd, local_serviceproperties_new, remote_serviceproperties, 1)
    #
    #
    for i in range(1, 9):
        # for i in range(20, 21):

        if i < 10:
            host_newcui = 'perf-activenet-cui-0' + str(i) + 'w.an.active.tan'
        else:
            host_newcui = 'perf-activenet-cui-' + str(i) + 'w.an.active.tan'

        print(host_newcui)

        # upload(host_newcui, username, passwd, local_jettyxml_new, remote_jettyxml, 1)
        upload(host_newcui, username, passwd, local_newcui_serviceproperties, remote_newcui_serviceproperties, 1)













