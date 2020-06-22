import unittest
from MyHTMLTestReportCN import HTMLTestRunner
import os
import time
import sys
sys.path.append("..")
# 定义输出的文件位置和名字
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

HtmlFile = report_path+now+"HTMLtemplate.html"

fp = open(HtmlFile, "wb")


if __name__=='__main__':
    suite = unittest.TestLoader().discover("testsuites")
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='执行情况',tester='XKS')
    runner.run(suite)
