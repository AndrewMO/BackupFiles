# -*- coding: utf-8 -*-

# !/usr/bin/python

import paramiko
import threading


def threaddump(host, username, passwd, getJavaPid, JavaHome, threadfilepath):
    try:

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, 22, username, passwd, timeout=5)
        ServerNo = host[19:21]
        JavaPid = -1

        for m1 in getJavaPid:

            stdin, stdout, stderr = ssh.exec_command(m1)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出
            for o in out:
                print(" Java process PID of ' %s ' :  %s" % (host, o))
            JavaPid = ''.join(out).rstrip('\n')

        threaddumpcmd = []
        threaddumpcmd.append('cd ' + JavaHome +';'+'./jstack -l ' + JavaPid + ' >' + threadfilepath + '/03_1800_NewCart_' + ServerNo +'w_threaddump.txt' )
        # ./jstack -l 9672  >/opt/active/ActiveNet/perf/perf08wthreaddump.txt

        for m2 in threaddumpcmd:
            stdin, stdout, stderr = ssh.exec_command(m2)

            # stdin.write("Y")   #简单交互，输入 ‘Y’

            out = stdout.readlines()

            # 屏幕输出
            for o in out:
                print(" threaddump of ' %s ' :  %s" % (host, o))



        print(threaddumpcmd)


        ssh.close()

    except:

        print('%s\tError\n' %(host))


if __name__ == '__main__':

    getJavaPid = ['ps -ef|grep java|grep -v grep|grep ActiveNetCUI|awk \'{print $2}\'']  # 获取JavaPid的命令
    threadfilepath = "/opt/active/ActiveNet/perf/3000test/newcui" #dump文件存放路径
    JavaHome = "/usr/java/jdk8_192-1.8_192/bin" # 进入java路径

    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    threads = []  # 多线程

    # ./jstack -l 9672  >/opt/active/ActiveNet/perf/perf08wthreaddump.txt

    print("Begin......")

    for i in range(1, 9):
        # perf-activenet-cui-01w.an.active.tan

        if i < 10:
            host1 = 'perf-activenet-cui-0' + str(i) + 'w.an.active.tan'
        else:
            host1 = 'perf-activenet-cui-' + str(i) + 'w.an.active.tan'



        a = threading.Thread(target=threaddump, args=(host1, username, passwd, getJavaPid, JavaHome, threadfilepath))
        a.start()


