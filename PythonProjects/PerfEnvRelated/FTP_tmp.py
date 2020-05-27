# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import datetime
import threading
import logging
import os
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def upload(host, username, passwd,  local, remote, file_type):
    try:

        trans = paramiko.Transport((host, 22))
        trans.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(trans)

        if file_type == 1:
            logger.debug()
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
                if ".log" in f:
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



    print("Begin......")

    # for i in range(1, 3):
    #
    #     if i < 10:
    #         host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

    remote_log_path = '/opt/active/sites/acm01vegasjetty/ActiveNetCUI/logs'
    local_log_path = '/Users/ajia/Documents/tmp/newcuilog'

    for i in range(1, 2):
    # for i in range(20, 21):

        # if i < 10:
        #     host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        # else:
        #     host = 'perf-activenet-' + str(i) + 'w.an.active.tan'
    # perf-activenet-cui-01w.an.active.tan
        if i < 10:
            host = 'perf-activenet-cui-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-cui-' + str(i) + 'w.an.active.tan'

        # print(host)

        download(host, username, passwd,  local_log_path, remote_log_path, 2)


