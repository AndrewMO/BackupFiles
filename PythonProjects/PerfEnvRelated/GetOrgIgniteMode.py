# -*- coding: utf-8 -*-

# !/usr/bin/python


import requests
import re
import time
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def getMode(url):
    requests.adapters.DEFAULT_RETRIES = 3

    response = requests.get(url)
    response.raise_for_status()

    # print(response.text)


    mode = re.search( r"This Org CacheMode -> \[(.*?)\]",response.text).group(1)

    return mode



if __name__ == '__main__' :

    logging.debug('start...')

    thread = []

    # orgname = ['perf01', 'perf01jetty', 'perf02', 'perf03', 'acm01vegas', 'acm01vegasjetty']
    orgname = ['acm01vegasjetty']

    for org in orgname:
        urlstr = "https://anperf01.active.com/" + org + "/servlet/ignitemetrics.sdi"
        print("Current ignie mode of " + org +" is " + str(getMode(urlstr,)) )

    logging.debug('end.')





