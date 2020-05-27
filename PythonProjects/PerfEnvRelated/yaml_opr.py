import threading

import paramiko
import yaml
import os
import logging
logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def yaml_opr():
    #open yaml file
    with open("env_properties.yaml", "r", encoding="utf-8") as file:
        yaml_data = yaml.load(file.read(), Loader=yaml.FullLoader)
        print(type(yaml_data))
        # print(yaml_data)
        print(yaml_data['ENV']['perf_rushpool_AUI']['NODES'])


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


def check_JVM(env):
    # perf_rushpool_AUI
    # perf_standardpool_AUI
    # perf_NewCUI
    # perf_ignite

    with open("env_properties.yaml", "r", encoding="utf-8") as file:
        yaml_data = yaml.load(file.read(), Loader=yaml.FullLoader)
        nodes_amount = yaml_data['ENV'][env]['NODES']
        logger.debug("nodes amount : %r"  %(nodes_amount))
        username = "deploy"  # 用户名
        passwd = "123!deploy"  # 密码

        if env == 'perf_rushpool_AUI':
            cmd_jvm = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1']  # 你要执行的命令列表
            for i in range(1, (nodes_amount+1)):
                if i < 10:
                    host_name =  yaml_data['ENV'][env]['PREHOST'] + '0' + str(i) + yaml_data['ENV'][env]['DOMAIN']
                else:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + str(i) + yaml_data['ENV'][env]['DOMAIN']

                logger.debug("host name : %s " %(host_name))
                a = threading.Thread(target=ssh2, args=(host_name, username, passwd, cmd_jvm))
                a.start()
        elif env == 'perf_standardpool_AUI':
            cmd_jvm = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1']  # 你要执行的命令列表
            for i in range(19, (19 + nodes_amount)):
                if i < 10:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + '0' + str(i) + yaml_data['ENV'][env]['DOMAIN']
                else:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + str(i) + yaml_data['ENV'][env]['DOMAIN']

                logger.debug("host name : %s " % (host_name))
                a = threading.Thread(target=ssh2, args=(host_name, username, passwd, cmd_jvm))
                a.start()
        elif env == 'perf_NewCUI':
            cmd_jvm = ['ps -ef|grep java|grep -v grep|grep ActiveNetCUI']  # 你要执行的命令列表
            for i in range(1, (nodes_amount+1)):
                if i < 10:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + '0' + str(i) + yaml_data['ENV'][env]['DOMAIN']
                else:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + str(i) + yaml_data['ENV'][env]['DOMAIN']

                logger.debug("host name : %s " % (host_name))
                a = threading.Thread(target=ssh2, args=(host_name, username, passwd, cmd_jvm))
                a.start()
        elif env == 'perf_ignite':
            cmd_jvm = ['ps -ef|grep java|grep -v grep|grep ActiveNetServlet1']  # 你要执行的命令列表
            for i in range(1, (nodes_amount+1)):
                if i < 10:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + '0' + str(i) + yaml_data['ENV'][env]['DOMAIN']
                else:
                    host_name = yaml_data['ENV'][env]['PREHOST'] + str(i) + yaml_data['ENV'][env]['DOMAIN']

                logger.debug("host name : %s " % (host_name))
                a = threading.Thread(target=ssh2, args=(host_name, username, passwd, cmd_jvm))
                a.start()
        else:
            print("error env found")



if __name__ == '__main__':
    # perf_rushpool_AUI
    # perf_standardpool_AUI
    # perf_NewCUI
    # perf_ignite


    # check_JVM('perf_rushpool_AUI')
    # check_JVM('perf_standardpool_AUI')
    # check_JVM('perf_NewCUI')
    check_JVM('perf_ignite')
