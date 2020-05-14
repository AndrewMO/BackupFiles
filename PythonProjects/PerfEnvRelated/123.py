import paramiko
import re
from xml.dom.minidom import parse
import xml.dom.minidom
import datetime
import requests
import sys
import os
rootPath = os.path.abspath(os.path.join(os.path.join(os.path.dirname("__file__"), os.path.pardir),os.path.pardir))
sys.path.append(rootPath)
sys.path.append(r'C:\Python_Workspace\ApplicationPerformance')

from Performance_CI.DailyPerf.service_properties import hostNameBuilder,RegressionTemplateConfig
from Performance_CI.DailyPerf.DBHandler import DatabaseHandler, TransactionResponseHistory, Version
from Performance_CI.DailyPerf.JenkinsValidator import Jenkins_Api
from Performance_CI.DailyPerf.neoloadweb import neoloadweb



class ReportComposer():

    def __init__(self):
        # file location for debug
        # Jenkins will start this script from workspace as default which makes all the relative path needs to start from here.
        # e.g : C:\Program Files (x86)\Jenkins\workspace\Endurance_Performance_Regression>python C:\Python_Workspace\ApplicationPerformance\Performance_CI\DailyPerf\ComposeReport.py

        # Current Jenkins configuration
        # This script needs to locate
        # C:\Python_Workspace\ApplicationPerformance\Performance_CI\DailyPerf\ComposeReport.py
        # report_file_source
        # C:\Python_Workspace\ApplicationPerformance\Performance_CI\neoload-report\Endurance_Daily_Report_template.html
        # report_xml
        # C:\Program Files (x86)\Jenkins\workspace\Endurance_Daily_Perf_Test\report.xml
        # report_file_gen
        # C:\Program Files (x86)\Jenkins\workspace\Endurance_Daily_Perf_Test\Endurance_Daily_Report.html
        if os.popen('hostname').read().strip() == 'dev-perfqa-02w':
            #file location for jenkins server
            self.report_file_source = "../../../../../Python_Workspace/ApplicationPerformance/Performance_CI/neoload-report/Endurance_Daily_Report_template.html"
            self.report_file_gen = "./neoload-report/Endurance_Daily_Report.html"
            self.report_xml = "./neoload-report/report.xml"

        # TODO(squall.yang@activenetwork.com): set the local machine list in the configuration file
        elif os.popen('hostname').read().strip() == 'che34080w.active.local' or os.popen('hostname').read().strip() == 'Squall-Yang.local' or os.popen('hostname').read().strip() == 'wl000731051.active.local':
            # file location for local
            self.report_file_source = "/Users/squallyang/Documents/Python_WorkSpace/ApplicationPerformance/Performance_CI/neoload-report/Endurance_Daily_Report_template.html"
            self.report_file_gen = "/Users/squallyang/Documents/Python_WorkSpace/ApplicationPerformance/Performance_CI/neoload-report/Endurance_Daily_Report.html"
            self.report_xml = "/Users/squallyang/Documents/Python_WorkSpace/ApplicationPerformance/Performance_CI/neoload-report/report.xml"

        else:
            raise RuntimeError('Could not find the hostname defined, The current machine hostname is '+os.popen('hostname').read().strip())

        self.testStatus = True
        self.domtree = xml.dom.minidom.parse(self.report_xml)
        self.root = self.domtree.documentElement
        self.statistics = self.root.getElementsByTagName("statistics")[0]
        self.virtualUser = self.root.getElementsByTagName("virtual-users")[0]

    def test_status(self):
        file = open(self.report_file_gen, "r", encoding="utf-8")
        buff = file.read()
        file.close()

        if self.testStatus is True:
            buff = re.sub('<span>test_status</span>', '<span style="color: green;"><strong>Success</strong></span>', buff, 0)
        else:
            buff = re.sub('<span>test_status</span>', '<span style="color: red;"><strong>Failed</strong></span>', buff, 0)

        file = open(self.report_file_gen, "w", encoding="utf-8")
        file.write(buff)
        file.close()


    def ssh2(self,host, username, passwd, cmd):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, 22, username, passwd, timeout=5)

            for m in cmd:
                stdin, stdout, stderr = ssh.exec_command(m)
                out = stdout.readlines()
            ssh.close()
            return out
        except:
            raise RuntimeError('%s\tError\n' % (host))


    # Get App version from given server
    def app_version(self, testset, host, service_name, base, architecture, *args):
        # TODO(squall.yang@activenetwork.com): to save the version info to data base and integrate with API
        namespace = args[0]
        username = "syang4"
        password = "Stone_214!!!!!!!!a"
        if base == 'VM':
            if architecture == 'CoreServer':
                service_properties_file_location = '/opt/active/' + service_name + '/config/service.properties'
                command = [
                    'cat ' + service_properties_file_location + '| grep appVersion=' + "| awk -F '=' '{print $2}' "]  # Command list
            elif architecture == 'SpringBoot':
                command = [
                    "ls /opt/active/" + service_name + "/ | grep " + service_name + " | awk -F '-' '{print $3}' | awk -F '.jar' '{print $1}'"]  # Command list
            else:
                raise RuntimeError('The architecture setting is incorrect, Please confirm the setting for ' + service_name)
            response = self.ssh2(host, username, password, command)
            version = response[0].replace("\n", "")
            self.save_version_to_db(service_name,version,testset,datetime.datetime.now())
            return version

        elif base == 'K8s':
            if architecture == 'SpringBoot':
                host = 'neoloadweb.dev.activenetwork.com'
                command = ["kubectl get pods -n '" + namespace + "' | grep " + service_name + " | awk -F ' ' '{print $1}' | head -n 1" ]
                pod_name = self.ssh2(host, username, password, command)[0].replace("\n", "")
                command = ["kubectl describe pod " + pod_name + " -n '" + namespace + "' | grep artifacts.dev.activenetwork.com | grep " + service_name + " |grep -v 'Image ID' | awk -F ':' '{print $4}'"]
                version = self.ssh2(host, username, password, command)[0].replace("\n", "")
                self.save_version_to_db(service_name, version, testset, datetime.datetime.now())
                return version
        else:
            raise RuntimeError('The base or architecture setting is incorrect, Please confirm the setting for ' + service_name)

    def save_version_to_db(self,service_name,version,testset,create_dt):
        dbh = DatabaseHandler()
        dbh.save_version(service_name,version,testset,create_dt)

    # Update version information
    def update_app_version_info(self,testSet):
        hb = hostNameBuilder()
        aut = (hb.buildShortNamesByTestSet(testSet))

        if testSet.find("ANET_Daily_Perf_Test") == -1:
            #read the buffer from template and replace the value
            with open(self.report_file_source, "r", encoding="utf-8") as file:
                buff = file.read()
                VersionInfoList = ''

                for serviceShortName in aut:
                    host_name = hb.SingleHost(serviceShortName)[0]
                    service_name = hb.SingleHost(serviceShortName)[1]
                    base = hb.SingleHost(serviceShortName)[2]
                    architecture = hb.SingleHost(serviceShortName)[3]
                    namespace = hb.SingleHost(serviceShortName)[4]

                    VersionInfo = service_name + ': ' + self.app_version(testSet,host_name,service_name,base,architecture,namespace) + '<br>'
                    VersionInfoList = VersionInfoList + VersionInfo

                buff = re.sub('VersionInfoToBeUpdated',VersionInfoList,buff, 0)

                # write the buff back to the file
                with open(self.report_file_gen, "w", encoding="utf-8") as file:
                    file.write(buff)
            return VersionInfoList
        else:
            TargetURL = "https://apmstg.activecommunities.com/stgacm01vegas/activenet_version"

            TargetURL_response = requests.get(TargetURL)
            TargetURL_response.raise_for_status()

            #read the buffer from template and replace the value
            with open(self.report_file_source, "r", encoding="utf-8") as file:
                buff = file.read()
                VersionInfoList = ''

                # for serviceShortName in aut:
                ServletVersionInfo = re.search(r'Servlet version:&nbsp;\d{2}.\d{2}.\d{1}.\d{3}', TargetURL_response.text).group().split(';')[1]
                AcmCUIVersionInfo = re.search(r'CUI version:&nbsp;\d{2}.\d{2}.\d{1}.\d{3}', TargetURL_response.text).group().split(';')[1]
                NewCUIVersionInfo = re.search(r'<span id=\"newCuiVersionSpan\">\d{2}.\d{2}.\d{1}.\d{3}', TargetURL_response.text).group().split('>')[1]
                VersionInfoList = 'servlet_version: ' + ServletVersionInfo + '<br>' +'acm_cui_version: ' + AcmCUIVersionInfo + '<br>' + 'new_cui_version: ' + NewCUIVersionInfo + '<br>'

                self.save_version_to_db('Servlet version', ServletVersionInfo, testSet, datetime.datetime.now())
                self.save_version_to_db('CUI version', AcmCUIVersionInfo, testSet, datetime.datetime.now())
                self.save_version_to_db('newCuiVersionSpan', NewCUIVersionInfo, testSet, datetime.datetime.now())

                buff = re.sub('VersionInfoToBeUpdated',VersionInfoList,buff, 0)

            # write the buff back to the file
            with open(self.report_file_gen, "w", encoding="utf-8") as file:
                file.write(buff)
            return VersionInfoList

    # Update Summary table
    def update_summary_table(self,testSet):

        statistic_elements = self.statistics.getElementsByTagName("statistic")

        with open(self.report_file_gen, "r", encoding="utf-8") as file:
            buff = file.read()

        table_summary_template = RegressionTemplateConfig(testSet).SummaryTable

        for statistic_template in table_summary_template:
            for statistic_report in statistic_elements:
                if statistic_report.getAttribute("name") == statistic_template and statistic_report.getAttribute("name") != "total_errors":
                    buff = re.sub(statistic_template, statistic_report.getAttribute('value'), buff, 0)

                elif statistic_report.getAttribute("name") == "total_errors":
                    total_errors = statistic_report.getAttribute("value")
                    if float(total_errors) <= 10:
                        buff = re.sub('total_errors', total_errors, buff, 0)
                    else:
                        self.testStatus = False
                        buff = re.sub(
                            '<td width="156">\n' + '.*' + '<p>total_errors</p>\n' + '.*' + '</td>',
                            '<td style="width: 156px;background: LightSalmon;"><p>' + total_errors + '</p></td>', buff, 0)

        with open(self.report_file_gen, "w", encoding="utf-8") as file:
            file.write(buff)



    # Update response time in table by given parameters
    def update_response_time_in_cell(self,report_buff, baseline_label, baseline_value, result_label, result_value, passfail_label,test_set):
        report_buff = re.sub(result_label, str(result_value), report_buff, 0)
        report_buff = re.sub(baseline_label, str(baseline_value), report_buff, 0)

        # Mark as failed if page response time is 0
        if float(result_value) < 0.001:
            self.testStatus = False
            report_buff = re.sub('<td style="width: 90px;">\n' + '.*' + '<p>' + passfail_label + '</p>\n' + '.*' + '</td>',
                          '<td style="width: 90px;"><p>N/A</p></td>' +
                          '<td style="width: 90px;background: LightSalmon;"><p>FAIL</p></td>', report_buff, 0)
            return report_buff

        ratio = (float(result_value) - float(baseline_value)) / float(baseline_value)

        dbh = DatabaseHandler()
        transaction_name = result_label[0:len(result_label) - 4]
        # Assumption - response time should be increased no more than 30% than baseline.
        if ratio <= 0.3:
            report_buff = re.sub('<td style="width: 90px;">\n' + '.*' + '<p>' + passfail_label + '</p>\n' + '.*' + '</td>',
                         '<td style="width: 90px;"><p>' + str(round(ratio * 100, 2)) + '%</p></td>' +
                         '<td style="width: 90px;background: LightGreen;"><p>PASS</p></td>', report_buff, 0)

            dbh.save_transaction_response_history(test_set, transaction_name, result_value, datetime.datetime.now(),'PASS')
        else:
            self.testStatus = False
            report_buff = re.sub('<td style="width: 90px;">\n' + '.*' + '<p>' + passfail_label + '</p>\n' + '.*' + '</td>',
                         '<td style="width: 90px;"><p>' + str(round(ratio * 100, 2)) + '%</p></td>' +
                         '<td style="width: 90px;background: LightSalmon;"><p>FAIL</p></td>', report_buff, 0)
            dbh.save_transaction_response_history(test_set, transaction_name, result_value, datetime.datetime.now(), 'FAILED')
        return report_buff

    def get_duplicate_transaction_name_count(self,test_set):

        statisticItem_element = self.virtualUser.getElementsByTagName("statistic-item")

        transactions_name_template = RegressionTemplateConfig(test_set).Transactions.keys()
        transaction_count = {}

        for transaction_name_template in transactions_name_template:
            for transactions_name_report in statisticItem_element:
                if transactions_name_report.getAttribute('name') == transaction_name_template:
                    if transactions_name_report.getAttribute('name') in transaction_count:
                        transaction_count[transactions_name_report.getAttribute('name')] += 1
                    else:
                        transaction_count[transactions_name_report.getAttribute('name')] = 1

        return transaction_count

    def get_highest_executed_avg(self,transaction_name):

        statisticItem_element = self.virtualUser.getElementsByTagName("statistic-item")

        transaction_response_time_list = []
        transaction_execution_count_list = []

        for transactions_name_report in statisticItem_element:
            if transactions_name_report.getAttribute('name') == transaction_name:
                transaction_response_time_list.append(transactions_name_report.getAttribute('avg'))
                transaction_execution_count_list.append(transactions_name_report.getAttribute('hits'))
        return transaction_response_time_list[transaction_execution_count_list.index(max(transaction_execution_count_list))]


    # Update Transaction table template
    def update_transaction_table_template(self,test_set):
        with open(self.report_file_gen,'r',encoding='utf-8') as file:
            buff = file.read()

        transactions_name_template = RegressionTemplateConfig(test_set).Transactions
        transaction_entries = ''
        for transaction_name_template in transactions_name_template:

            transaction_entry = '<tr>\n<td style="width: 330px;">\n<p>' + transaction_name_template + '</p>\n</td>\n<td style="width: 90px;">\n<p>' + transaction_name_template + '_base</p>\n</td>\n<td style="width: 90px;">\n<p>' + transaction_name_template + '_avg</p>\n</td>\n<td style="width: 90px;">\n<p>' + transaction_name_template + '_result</p>\n</td>\n</tr>\n'
            transaction_entries = transaction_entries + transaction_entry

        buff = re.sub('TransactionsSummary',transaction_entries,buff, 0)

        # write the buff back to the file
        with open(self.report_file_gen, "w", encoding="utf-8") as file:
            file.write(buff)

    # Update response time matrix
    def update_response_time_in_table(self, test_set, base_line_mode='fix', interval=10):
        '''
        :param test_set: the test set name which could be set in the service-properties.yaml. the test set name
        needs to match the jenkins job name

        :param base_line_mode: can be select for fix mode and dynamic mode, fix mode to take the baseline from
        service-properties.yaml file. dynamic mode to calculate from database

        :param interval: only be used for dynamic mode. used use for define the baseline calculation period by days

        :return:None
        '''

        statisticItem_element = self.virtualUser.getElementsByTagName("statistic-item")

        with open(self.report_file_gen, "r", encoding="utf-8") as file:
            buff = file.read()

        if base_line_mode == 'fix':
            transactions_name_template = RegressionTemplateConfig(test_set).Transactions
        elif base_line_mode == 'dynamic':
            dbh = DatabaseHandler()
            transactions_name_template = dbh.get_baseline_from_all_history('"' + test_set + '"', str(interval))

        for transaction_name_template in transactions_name_template:
            for transactions_name_report in statisticItem_element:
                # TODO(squall.yang@activenetwork.com): To calculate baseline from Database instead of hard code.
                if transactions_name_report.getAttribute('name') == transaction_name_template:
                    # Handle duplicated transaction name
                    if self.get_duplicate_transaction_name_count(test_set).get(transaction_name_template) > 1:
                        buff = self.update_response_time_in_cell(buff, transaction_name_template + '_base',
                                                            transactions_name_template.get(transaction_name_template),
                                                            transaction_name_template + '_avg',
                                                            self.get_highest_executed_avg(transaction_name_template),
                                                            transaction_name_template + '_result',test_set)
                    # Handle transaction name not duplicated
                    elif self.get_duplicate_transaction_name_count(test_set).get(transaction_name_template) == 1:
                        buff = self.update_response_time_in_cell(buff, transaction_name_template + '_base',
                                                            transactions_name_template.get(transaction_name_template),
                                                            transaction_name_template + '_avg',
                                                            transactions_name_report.getAttribute("avg"),
                                                            transaction_name_template + '_result',test_set)

        with open(self.report_file_gen, "w", encoding="utf-8") as file:
            file.write(buff)

    def compose_report(self):
        if os.popen('hostname').read().strip() == 'dev-perfqa-02w':

            ja = Jenkins_Api()
            JobName = ja.get_last_build_job_name()
            self.update_app_version_info(JobName)
            self.update_summary_table(JobName)
            self.update_transaction_table_template(JobName)
            self.update_response_time_in_table(JobName, base_line_mode='dynamic')
            self.test_status()

        elif os.popen('hostname').read().strip() == 'che34080w.active.local' or os.popen(
                'hostname').read().strip() == 'Squall-Yang.local' or os.popen('hostname').read().strip() == 'wl000731051.active.local':
            # TODO(squall.yang@activenetwork.com): set the local machine list in the configuration file

            self.update_app_version_info('Endurance_Daily_Perf_Test')
            self.update_summary_table('Endurance_Daily_Perf_Test')
            self.update_transaction_table_template('Endurance_Daily_Perf_Test')
            self.update_response_time_in_table('Endurance_Daily_Perf_Test', base_line_mode='dynamic')
            self.test_status()

        else:
            raise RuntimeError('Could not find the hostname defined, The current machine hostname is ' + os.popen(
                'hostname').read().strip())

if __name__ == '__main__':
    rc = ReportComposer()
    rc.compose_report()
    nlw = neoloadweb()
    nlw.delete_tests(nlw.get_expired_test_id())
