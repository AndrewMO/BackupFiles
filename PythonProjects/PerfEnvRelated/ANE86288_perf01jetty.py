# -*- coding: utf-8 -*-

# !/usr/bin/python

import requests
import csv
import logging
import datetime
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


def getResponse(url, programID):
    t1 = datetime.datetime.now()
    response = requests.get(url)
    t2 = datetime.datetime.now()
    totalResponseTime = (t2 - t1).total_seconds()


    print("ProgramID: %4s  ,  totalResponseTime : %r s" % (programID, totalResponseTime ))



if __name__ == '__main__' :

    logging.debug('start of program')

    with open("D:/tmp/programID_Perf01Jetty.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        column = [row['DCPROGRAM_ID'] for row in reader]
        # print(column)


    # https://anperf01.active.com/perf01/rest/program/exceptionandextradates?program_id=11&api_key=xtccwxpswtcraum65jp2nbwv

    for i in column:
        urlstr = "https://anperf01.active.com/perf01jetty/rest/program/exceptionandextradates?program_id=" + str(
            i) + "&api_key=ecyt49sgafa2van2fbaw8udu"
        getResponse(urlstr, i)


    logging.debug('end of program')





