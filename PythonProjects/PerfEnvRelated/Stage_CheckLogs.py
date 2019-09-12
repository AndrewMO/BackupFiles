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
                print(o)
                # print("%s service status : %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except Exception as e:

        print('%s\tError\n:' %(host))
        print(e)


if __name__ == '__main__':



    orgname = ['lstgapachejunction', 'lstgbreckenridgerec', 'lstgcampbellrecreation', 'lstgchandleraz',
               'lstgchesterfieldparksrec', 'lstgcityofcarlsbad', 'lstgcityofcorona', 'lstgcityofdowney',
               'lstgculpepercopandr', 'lstgdenver', 'lstgebparks', 'lstgencinitasparksandrec',
               'lstgfalmouthcommunityprog', 'lstgfpdccrecreation', 'lstggepark', 'lstggjparksandrec', 'lstgindymca',
               'lstgkansascityymca', 'lstglanguagestars', 'lstglbparks', 'lstgmesaaz', 'lstgminneapolisparks',
               'lstgmontgomerycounty', 'lstgmrurecreation', 'lstgnaparec', 'lstgnms', 'lstgnorthshoreymca',
               'lstgomahaconservatory', 'lstgoneteamkids', 'lstgportlandparks', 'lstgrightatschool',
               'lstgsanjoseparksandrec', 'lstgsdparkandrec', 'lstgsfcmprep', 'lstgymcagreaterbrandywine',
               'lstgymcasatx']



    # orgname = ['lstgapachejunction']




    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码

    host1 = "stage-activenet-01w.an.dev.activenetwork.com"

    print("Begin......Servlet")

    for org in orgname:
        print(org)
        cmd = []
        # cmd_line = "cd /opt/active/ActiveNet/stage/" + org +  "/19.08.0.049/stage-activenet-01w.an.dev.activenetwork.com/ActiveNetServlet/logs;ls -l "
        cmd_line = "cd /opt/active/ActiveNet/stage/" + org + "/19.08.0.049/stage-activenet-01w.an.dev.activenetwork.com/ActiveNetServlet/logs;ls -l| grep total |awk \'{print $2}\' "

        # print(cmd_line)
        cmd.append(cmd_line)

        ssh2(host1, username, passwd, cmd)







