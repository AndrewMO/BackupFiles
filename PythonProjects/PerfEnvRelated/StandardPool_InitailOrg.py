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
    serverNo = url[22:24]


    print("Server : %s ; Status_Code : %r ; initial time : %r s ; hosturl : %s" % (serverNo, rsc, initial_time, url))



if __name__ == '__main__' :

    # logging.debug('start of program')

    print("processing...")
    thread = []
    orgname = ['perf01', 'perf01jetty', 'perf02', 'perf03', 'acm01vegas']
    # orgname = ['acm01vegas']


    # orgname = sys.argv[1]


    for org in orgname:
        for i in range(19, 21):
            if (i < 10):
                urlstr = "http://perf-activenet-0"+str(i)+"w.an.active.tan:3000/"+org+"/servlet/adminlogin.sdi"
                # logging.debug('i is '+ str(i) + ' , url is ' + urlstr)
            else:
                urlstr = "http://perf-activenet-"+str(i)+"w.an.active.tan:3000/"+org+"/servlet/adminlogin.sdi"
                # logging.debug('i is ' + str(i) + ' , url is ' + urlstr)
            a = threading.Thread(target=getResponse, args=(urlstr,))
            a.start()

    # logging.debug('end of program')





