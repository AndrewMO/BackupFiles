# -*- coding: utf-8 -*-

# !/usr/bin/python

from pypsexec.client import Client


def RunCmdOnRemote(server, username, password, executable, arguments):
    # set encrypt=False for Windows 7, Server 2008
    c = Client(server, username=username, password=password, encrypt=False)

    c.connect()
    try:
        c.create_service()
        result = c.run_executable(executable, arguments=arguments)
    finally:
        c.remove_service()
        c.disconnect()

    print("Current Server : " + server)
    print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
    print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")






if __name__ == '__main__':

    # server = "ANACMP003.active.tan"
    servers = ["ANACMP003.active.tan", "ANACMP003a.active.tan", "ANACMP003b.active.tan",\
               "ANACMP004.active.tan", "ANACMP004a.active.tan", "ANACMP004b.active.tan", \
               "ANACMP005.active.tan", "ANACMP005a.active.tan", "ANACMP005b.active.tan", \
               "ANACMP006.active.tan", "ANACMP006a.active.tan", "ANACMP006b.active.tan", \
               "ANACMP006c.active.tan", "ANACMP006d.active.tan", "ANACMP007.active.tan", \
               "ANACMP007a.active.tan", "ANACMP007b.active.tan", "ANACMP007c.active.tan",\
               "ANACMP007d.active.tan", "ANACMP008.active.tan", "ANACMP008a.active.tan", \
               "ANACMP008b.active.tan", "ANACMP008c.active.tan", "ANACMP008d.active.tan"]
    username = "tan\\ajia"
    password = "Nwy7frxy@d"
    executable = "iisreset.exe"
    arguments = ""
    # arguments = "/all"



    for server in servers:
        RunCmdOnRemote(server, username, password, executable, arguments)


