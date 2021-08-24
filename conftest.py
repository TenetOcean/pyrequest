import os
import pytest
from py.xml import html
from datetime import datetime

# 项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + "/test_report/"

# 修改html报告的Environment
def pytest_configure(config):
    # 添加项目名称
    config._metadata["项目名称"] = "任我行订货平台登录接口"

# 设置用例描述表头
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

# 设置用例描述表格
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(datetime.now(), class_='col-time'))
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    用于向测试用例中添加用例的描述.（description）
    :param item:
    """

    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

# 测试用例为pass时替换所有附加的HTML和日志输出，并通知日志为空
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('No log output captured.', class_='empty log'))