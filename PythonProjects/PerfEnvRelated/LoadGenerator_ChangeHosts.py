# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import logging
import threading
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def ssh2(host, username, passwd, cmd):
    try:

        logger.debug("current server : %r" %(host))

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)

        for m in cmd:

            stdin, stdout, stderr = ssh.exec_command(m)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出

            for o in out:
                #print(o)
                print("%s  :  %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except:

        print('%s\tError\n' %(host))


if __name__ == '__main__':

    cmd_ATSOff = ["sudo sed -i 's/10.230.49.33/#10.230.49.33/' /etc/hosts;sudo cat /etc/hosts | grep '10.230.49.33' "]  # 关闭ATS
    cmd_ATSOn = ["sudo sed -i 's/#10.230.49.33/10.230.49.33/' /etc/hosts;sudo cat /etc/hosts | grep '10.230.49.33' "]  # 打开ATS
    cmd_CheckATS = ["sudo less /etc/hosts | grep '10.230.49.33' "]

    username = "ajia"  # 用户名

    passwd = "Nwy7frxy@anet01"  # 密码

    threads = []  # 多线程

    print("Begin......")
    logger.debug("Process Start")

    # for i in range(27, 28):
    for i in range(27, 41):
        if i < 10:
            host = 'qaneolglin0' + str(i) + '.dev.activenetwork.com'
        else:
            host = 'qaneolglin' + str(i) + '.dev.activenetwork.com'

        # a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_ATSOff))
        # a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_ATSOn))
        a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_CheckATS))
        a.start()

    logger.debug("Process End")
