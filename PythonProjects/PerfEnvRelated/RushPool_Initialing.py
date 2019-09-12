# -*- coding: utf-8 -*-

# !/usr/bin/python


import requests
import threading
import time
import logging
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
    thread = []
    # orgname = 'perf04'
    orgname = 'acm01vegasjetty'
    count = 0



    for i in range(1, 19):
        if (i < 10):
            urlstr = "http://perf-activenet-0"+str(i)+"w.an.active.tan:3000/"+orgname+"/servlet/adminlogin.sdi"
            # logging.debug('i is '+ str(i) + ' , url is ' + urlstr)
        else:
            urlstr = "http://perf-activenet-"+str(i)+"w.an.active.tan:3000/"+orgname+"/servlet/adminlogin.sdi"
            # logging.debug('i is ' + str(i) + ' , url is ' + urlstr)
        # print(urlstr)
        # print("server  %r is initialing"  %(i))
        a = threading.Thread(target=getResponse, args=(urlstr,))
        a.start()
        count += 1


    print("initial %d orgs"  %(count))

        # logging.debug('end of program')





