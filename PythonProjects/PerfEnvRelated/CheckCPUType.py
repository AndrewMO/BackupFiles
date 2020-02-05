# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import threading


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
                print("%s  : %s" % (host, o))
                # print("\033[0;37;40m%s\033[0m : %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except:

        print('%s\tError\n' %(host))


if __name__ == '__main__':

    # cmd = ['pwd']  # 你要执行的命令列表

    cmd1 = ['cat /proc/cpuinfo | grep "processor" | sort | uniq | wc -l']  # CPU核心数
    cmd3 = ['cat /proc/cpuinfo | grep name | sort | uniq']  # 查看CPU型号
    cmd2 = ['cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l;cat /proc/cpuinfo | grep "core id" | sort | uniq | wc -l;cat /proc/cpuinfo | grep "processor" | sort | uniq | wc -l']  # 你要执行的命令列表

    # cat /proc/cpuinfo | grep name | sort | uniq  查看CPU型号
    # cat /proc/cpuinfo | grep "physical id"  查看物理CPU数目1
    # cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l 查看物理CPU数目2（推荐）
    ###
    # cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l  物理CPU个数
    # cat /proc/cpuinfo | grep "core id" | sort | uniq | wc -l  CPU核数
    # cat /proc/cpuinfo | grep "processor" | sort | uniq | wc -l CPU核心数
    ###




    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    print("Start Checking......")

    for i in range(1, 19):

        if i < 10:
            host1 = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host1 = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        a = threading.Thread(target=ssh2, args=(host1, username, passwd, cmd1))
        a.start()


