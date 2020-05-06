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
                #print(o)
                print("%s  :  %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except Exception as e:

        print('%s\tError\n %r' %(host, e))


if __name__ == '__main__':

    cmd_servlet = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1'] # 你要执行的命令列表
    cmd_cache = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1'] # 你要执行的命令列表
    cmd_getorgname = [
        'ps -ef|grep java|grep -v grep|grep ActiveNetServlet1 | awk \'{print $13}\' | awk -F \'/\' \'{print $5}\'']




    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    print("Begin......Servlet")

    for i in range(19, 21):

        if i < 10:
            host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

        # a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_getorgname))
        a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_servlet))
        a.start()



    # for i in range(1, 3):
    #
    #     if i < 10:
    #         host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
    #     else:
    #         host = 'perf-activenet-' + str(i) + 'w.an.active.tan'
    #
    #     c = threading.Thread(target=ssh2, args=(host, username, passwd, cmd))
    #     c.start()

    print("Begin......Cache")




    for i in range(3, 4):

        if i < 10:
            host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
        else:
            host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

        b = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_cache))
        b.start()
