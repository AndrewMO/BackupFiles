# -*- coding: utf-8 -*-

# !/usr/bin/python

from pypsexec.client import Client
import threading
import time


def clear_version_pkg_on_remote(server, username, password, executable, remote_path):
    # set encrypt=False for Windows 7, Server 2008
    c = Client(server, username=username, password=password, encrypt=False)
    # print("\033[0;37;40m%s\033[0m" %(server))

    c.connect()
    try:
        c.create_service()
        # get current server's version(except for latest one)
        version_list = c.run_executable(executable, arguments="/c \"dir " + remote_path + " /b /ad\"")
        # print(type(version_list[0].decode('utf-8')))
        # print(version_list[0].decode('utf-8'))
        versions = []
        version_tmp = ""
        for item in version_list[0].decode('utf-8'):
            if item not in ('\r', '\n'):
                version_tmp = version_tmp + item
                continue
            elif item == '\r':
                continue
            elif item == '\n':
                versions.append(version_tmp)
                version_tmp = ""
                continue

        # print(versions)
        # print("##################")
        # print(versions[:-1])

        # #versions should be ["19.13.0.066","19.14.0.037"]
        # versions =[]
        if len(versions) <= 1:
            print("\033[0;37;40m%s\033[0m" % (server))
            print("only latest build %r on server %r" %(versions[0], server))
            print("#" * len(versions) * 15)
        else:
            print("\033[0;37;40m%s\033[0m" % (server))
            for version in versions[:-1]:
                print("-- working  on %r with version  %r " % (server, version))
                arguments = "/c \"rd /s /q E:\\acm\\_versions\\" + version + "\""
                result = c.run_executable(executable, arguments=arguments)
                print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
                print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")
                print("## complete on %r with version  %r " % (server, version))




    finally:
        c.remove_service()
        c.disconnect()




    # print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
    # print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")
    # print("RC: %d" % result[2])

if __name__ == '__main__':

    # servers = ["ANACMP007.active.tan"]
    servers = ["ANACMP003.active.tan", "ANACMP003a.active.tan", "ANACMP003b.active.tan",\
               "ANACMP004.active.tan", "ANACMP004a.active.tan", "ANACMP004b.active.tan", \
               "ANACMP005.active.tan", "ANACMP005a.active.tan", "ANACMP005b.active.tan", \
               "ANACMP006.active.tan", "ANACMP006a.active.tan", "ANACMP006b.active.tan", \
               "ANACMP006c.active.tan", "ANACMP006d.active.tan", "ANACMP007.active.tan", \
               "ANACMP007a.active.tan", "ANACMP007b.active.tan", "ANACMP007c.active.tan",\
               "ANACMP007d.active.tan", "ANACMP008.active.tan", "ANACMP008a.active.tan", \
               "ANACMP008b.active.tan", "ANACMP008c.active.tan", "ANACMP008d.active.tan"]
    # servers = [ "ANACMP003.active.tan", "ANACMP003a.active.tan" ]
    username = "tan\\ajia"
    password = "Nwy7frxy@anet01"
    executable = "cmd.exe"
    # executable = "iisreset.exe"
    # arguments = "/c \"rd /s /q E:\\acm\\_versions\\" + version + "\""
    # arguments = "/c \"dir E:\\acm\\_versions /b /ad\""
    # arguments = "/all"

    remote_path = "E:\\acm\\_versions"

    #cmd /c "rd /s /q E:\acm\_versions\19.14.0.041"


    for server in servers:
        t = threading.Thread(target=clear_version_pkg_on_remote, args=(server, username, password, executable, remote_path))
        t.start()
        t.join()
        # clear_version_pkg_on_remote(server, username, password, executable, remote_path)


