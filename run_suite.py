# 导包
import unittest

# 定义套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")

# 获取报告
with open("./report/report.html", "wb")as f:
    HTMLTestRunner(stream=f).run(suite)
