# -*- coding: utf-8 -*-

# !/usr/bin/python
import sys

import paramiko

import threading
import time


def ssh2(host, username, passwd, cmd):
    try:

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
                print("%s service status :  %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except:

        print('%s\tError\n' %(host))


if __name__ == '__main__':

    orgnames = ["acm01vegasjetty", "acm01vegas", "perf01", "perf02", "perf01jetty", "ignite01", "share" ]

    versionString = "20.02.0.069"



    for orgname in orgnames:

        cmdString = "cd /opt/active/ActiveNet/perf/" + orgname + ";rm -rf " + versionString
		
        cmd =[]

        cmd.append(cmdString)  # 你要执行的命令列表
        print(orgname)
        print(cmd)

        username = "deploy"  # 用户名

        passwd = "123!deploy"  # 密码


        print("Begin......")
        time1 = time.time()

        for i in range(1, 2):

            if i < 10:
                host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
            else:
                host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

            ssh2(host, username, passwd, cmd)

        time2 = time.time()
        totalTime = time2 - time1
        print("Total time :" + str(totalTime))
        print("Finish......")

