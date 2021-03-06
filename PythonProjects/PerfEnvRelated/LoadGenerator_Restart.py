# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import logging
import threading
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def ssh2(host, username, passwd, cmd):
    try:
        logger.debug("start sub ssh")
        logger.debug("current host: %r" %(host))

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

    cmd = ['sudo /opt/neoload/bin/LoadGeneratorAgentService stop;sudo /opt/neoload/bin/LoadGeneratorAgentService start']  # 你要执行的命令列表

    username = "ajia"  # 用户名

    passwd = "Nwy7frxy@anet01"  # 密码

    threads = []  # 多线程

    print("Begin......")
    logger.debug("Start Main")

    # for i in range(1, 41):
    for i in range(27, 41):

        if i < 10:
            host = 'qaneolglin0' + str(i) + '.dev.activenetwork.com'
        else:
            host = 'qaneolglin' + str(i) + '.dev.activenetwork.com'

        a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd))
        a.start()
