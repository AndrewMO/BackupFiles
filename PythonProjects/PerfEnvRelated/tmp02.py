# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import re
import requests
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
                print("%s service status :  %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except:

        print('%s\tError\n' %(host))


def getMode(url):
    requests.adapters.DEFAULT_RETRIES = 3

    response = requests.get(url)
    response.raise_for_status()

    mode = re.search( r"This Org CacheMode -> \[(.*?)\]",response.text).group(1)

    return mode


def main():

    org_name = "acm01vegasjetty"

    org_url = "https://anperf01.active.com/" + org_name + "/servlet/ignitemetrics.sdi"

    org_mode = getMode(org_url)

    print("org name : %s ; org_mode : %s" %(org_name, org_mode))

    cmd_Servlet = ['pwd']  # 你要执行的命令列表
    cmd_Cache = ['pwd']  # 你要执行的命令列表


    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    if ( org_mode == 'REMOTE'):

        print("Cache......")

        for i in range(1, 3):

            if i < 10:
                host = 'perf-ignite-0' + str(i) + 'w.an.active.tan'
            else:
                host = 'perf-ignite-' + str(i) + 'w.an.active.tan'

            cache_thread = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_Cache))
            threads.append(cache_thread)


        print("Servlet......")
        for i in range(1, 19):

            if i < 10:
                host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
            else:
                host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

            servlet_thread = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_Servlet))
            threads.append(servlet_thread)


        for t in threads:
            t.start()

        for t in threads:
            t.join()


    elif (org_mode == 'LOCAL'):
        print("Begin......")

        for i in range(1, 19):

            if i < 10:
                host = 'perf-activenet-0' + str(i) + 'w.an.active.tan'
            else:
                host = 'perf-activenet-' + str(i) + 'w.an.active.tan'

            a = threading.Thread(target=ssh2, args=(host, username, passwd, cmd_Servlet))
            a.start()

    else:
        print("No vaild org mode found!")









if __name__ == '__main__':
    main()



