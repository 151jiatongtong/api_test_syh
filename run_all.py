#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from config import config
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import send_email

config.logging.info("="*25+"测试开始"+"="*25)
suite = unittest.defaultTestLoader.discover(config.testcase_path)#找test开头的.py的测试用例路径
with open(config.report_file,"wb") as f:
    HTMLTestRunner(stream=f,title="测试报告",description="描述").run(suite)
send_email(config.report_file)
config.logging.info("邮件已发送")
config.logging.info("="*25+"测试结束"+"="*25)