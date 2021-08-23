# coding=utf-8
import os
import time
import pytest
from conftest import REPORT_DIR
from config import RunConfig

'''
说明：
用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
'''

def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    # os.mkdir(new_report + "/image")
    
def run():
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)
    init_env(RunConfig.NEW_REPORT)
    html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
    xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")
    pytest.main(["-s", "-v", RunConfig.cases_path,
                 "--capture=sys",
                 "--html=" + html_report,
                 "--junit-xml=" + xml_report,
                 "--self-contained-html"])


if __name__ == '__main__':
    run()