# -*- coding: utf-8 -*-

# !/usr/bin/python


import requests
import threading
from bs4 import BeautifulSoup
import time
import re



def get_live_session_count(url):
    time_start = time.time()
    # soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    # tmp_number = re.search(requests.get(url).content, 'Active Session Count:(.*?)', re.I)
    # print(tmp_number.group())
    # # print(soup.prettify())
    # # active_session_count = soup.find('td',attrs={"class":"altRowEven"})
    # # print(type(active_session_count))
    # # print(active_session_count)
    print(requests.get(url).content)





    time_end = time.time()
    time_spend = time_end - time_start


    # return active_session_count



    # print(" time spent : %r s ; hosturl : %s" % (time_spend, url))





if __name__ == '__main__' :

    # logging.debug('start of program')
    # https://anprod.active.com/chicagoparkdistrict/servlet/displaysessiondata.sdi
    # https://anprodca.active.com/vancouver
    orgs = ['acm01vegasjetty']


    # orgs = ['Chicagoparkdistrict', 'SeattleYMCA', 'MontgomeryCounty', 'YMCALA', 'vancouver', 'kansascityymca', 'northshoreymca', 'ymcasatx','YMCAGreaterBrandywine']


    for org in orgs:
        if 'vancouver' in org:
            url = "https://anprodca.active.com/" + org + "/servlet/displaysessiondata.sdi"
        elif 'acm01vegasjetty' in org: #debug
            url = "https://anperf01.active.com/" + org + "/servlet/displaysessiondata.sdi"
        else:
            url = "https://anprod.active.com/" + org + "/servlet/displaysessiondata.sdi"

        print(org)
        current_live_session_count = get_live_session_count(url,)





