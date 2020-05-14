# -*- coding: utf-8 -*-

# !/usr/bin/python

from pypsexec.client import Client


def run_cmd_on_remote(server, username, password, executable, arguments):
    # set encrypt=False for Windows 7, Server 2008
    c = Client(server, username=username, password=password, encrypt=False)
    print("\033[0;37;40m%s\033[0m" %(server))

    c.connect()
    try:
        c.create_service()
        result = c.run_executable(executable, arguments=arguments)
    finally:
        c.remove_service()
        c.disconnect()


    print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
    print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")
    # print("RC: %d" % result[2])






if __name__ == '__main__':

    servers = ["dev-perfqa-01w.dev.activenetwork.com", "dev-perfqa-02w.dev.activenetwork.com", "dev-perfqa-03w.dev.activenetwork.com",\
               "dev-perfqa-04w.dev.activenetwork.com", "dev-perfqa-05w.dev.activenetwork.com", "dev-perfqa-06w.dev.activenetwork.com", \
               "dev-perfqa-07w.dev.activenetwork.com"]
    username = "dev\\ajia"
    password = "Nwy7frxy@anet01"
    executable = "ipconfig.exe"
    # executable = "iisreset.exe"
    arguments = ""
    # arguments = "/all"

    #cmd /c "rd /s /q "E:\acm\_versions\19.13.*" "



    for server in servers:
        run_cmd_on_remote(server, username, password, executable, arguments)


