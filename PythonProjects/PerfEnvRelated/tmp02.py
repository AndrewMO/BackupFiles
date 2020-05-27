# -*- coding: utf-8 -*-

# !/usr/bin/python


import requests
import threading
import time
import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__Name__)
# logging.disable(logging.CRITICAL)


def getResponse(url, org):
    requests.adapters.DEFAULT_RETRIES = 5
    # response = requests.get(url)
    # response.raise_for_status()
    time_start = time.time()
    response = requests.get(url)
    # response.raise_for_status()
    time_end = time.time()
    initial_time = time_end - time_start
    server = url[23:25]
    rsc = response.status_code




    print("Org : %s ; Server : %s ; Status_Code : %r ; initial time : %r s ; hosturl : %s" % (org, server, rsc, initial_time, url))



if __name__ == '__main__' :

    # logging.debug('start of program')
    thread = []
    orgname = ['lstgchicagoparkdistrict','lstgymcala','lstgphoenix','lstgdvusdce','lstgqa01','lstgqa02','lstgqa01trainer']
    # orgname = ['lstgchicagoparkdistrict']

    # orgname = ['lstgapachejunction' ]




    for org in orgname:
        for i in range(3, 5):
            if (i < 10):
                urlstr = "http://stage-activenet-0"+str(i)+"w.an.dev.activenetwork.com:3000/"+org+"/servlet/adminlogin.sdi"
            else:
                urlstr = "http://stage-activenet-"+str(i)+"w.an.dev.activenetwork.com:3000/"+org+"/servlet/adminlogin.sdi"

            a = threading.Thread(target=getResponse, args=(urlstr, org))
            a.start()

            # getResponse(urlstr, org)







        # logging.debug('end of program')





