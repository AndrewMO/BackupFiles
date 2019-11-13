# -*- coding: utf-8 -*-

# !/usr/bin/python
import sys

import requests
import threading
import logging
import time
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


def getResponse(url):
    requests.adapters.DEFAULT_RETRIES = 5
    time_start = time.time()
    response = requests.get(url)
    # response.raise_for_status()
    time_end = time.time()
    initial_time = time_end - time_start
    rsc = response.status_code
    serverNo = url[18:20]


    print("Server : %s ; Status_Code : %r ; initial time : %r s ; hosturl : %s" % (serverNo, rsc, initial_time, url))



if __name__ == '__main__' :

    # logging.debug('start of program')

    print("processing...")
    thread = []
    # orgname = ['perf01', 'perf01jetty', 'perf02', 'perf03', 'acm01vegas']
    base_orgname = "acm01vegas"
    # base_orgname = "perf02"
    orgname = []


    for orgindex in range(1, 26):
        if (orgindex < 10):
            orgindex = base_orgname + "0" + str(orgindex);
        else:
            orgindex = base_orgname + str(orgindex)

        orgname.append(orgindex)



    for org in orgname:
        for i in range(1, 3):

            urlstr = "http://10.119.43.10"+str(i)+":3000/"+org+"/servlet/adminlogin.sdi"
            a = threading.Thread(target=getResponse, args=(urlstr,))
            a.start()


    orgname.clear()

    # logging.debug('end of program')





