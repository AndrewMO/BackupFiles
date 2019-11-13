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
                print("%s : %s" % (host, o))

        #print('%s\t start service OK\n' %(host))

        ssh.close()

    except Exception as e:

        print('%s\tError\n:' %(host))
        print(e)


if __name__ == '__main__':


    # perf orgs
    orgname = ['lstgapachejunction', 'lstgbreckenridgerec', 'lstgcampbellrecreation', 'lstgchandleraz',
               'lstgchesterfieldparksrec', 'lstgcityofcarlsbad', 'lstgcityofcorona', 'lstgcityofdowney',
               'lstgculpepercopandr', 'lstgdenver', 'lstgebparks', 'lstgencinitasparksandrec',
               'lstgfalmouthcommunityprog', 'lstgfpdccrecreation', 'lstggepark', 'lstggjparksandrec', 'lstgindymca',
               'lstgkansascityymca', 'lstglanguagestars', 'lstglbparks', 'lstgmesaaz', 'lstgminneapolisparks',
               'lstgmontgomerycounty', 'lstgmrurecreation', 'lstgnaparec', 'lstgnms', 'lstgnorthshoreymca',
               'lstgomahaconservatory', 'lstgoneteamkids', 'lstgportlandparks', 'lstgrightatschool',
               'lstgsanjoseparksandrec', 'lstgsdparkandrec', 'lstgsfcmprep', 'lstgymcagreaterbrandywine',
               'lstgymcasatx']

    # auto orgs
    # orgname = ['automt01','automt02', 'automt03', 'automt04', 'automt05', 'automt06',
    #            'automt07', 'automt08', 'automt09', 'automt10', 'automt11',
    #            'automt12', 'automt13', 'automt14', 'automt15', 'automt16',
    #            'automt17', 'automt18','anetdev01','anetdev02', 'anetdev03', 'anetdev04',
    #            'jettytest01','jettytest02', 'jettytest03', 'jettytest04', 'jettytest05', 'jettytest06',
    #            'jettytest07', 'jettytest08', 'jettytest09', 'jettytest10', 'jettytest11',
    #            'jettytest12', 'jettytest13', 'jettytest14', 'linux01', 'linux02', 'linux03', 'linux04',
    #            'linux05', 'linux06', 'linux07', 'linux08', 'linux09', 'linux10', 'linux11', 'linux12',
    #            'linux13', 'linux14', 'linux15', 'linux16', 'linux17', 'linux18', 'linux19', 'linux21']

    # function orgs

    # orgname = ['lstgymcasatx','lstgsanjoseparksandrec']


    username = "deploy"  # 用户名

    passwd = "123!deploy"  # 密码
    cmd = []


    for org in orgname:
        cmdString = "ls -l  /opt/active/ActiveNet/stage/" + org


        cmd.append(cmdString)
        print("\033[0;37;40m %s \033[0m" %(org))
        host1 = 'stage-activenet-02w.an.dev.activenetwork.com'
        ssh2(host1, username, passwd, cmd)
        print("\033[0;32;43m %s \033[0m" % ("finish"))
        cmd.clear()




