# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_news_home import NewsHomePage
class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine()
        cls.driver = browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_baidu_news(self):
        newspage = NewsHomePage(self.driver)
        newspage.click_sports()
        time.sleep(2)
        newspage.get_windows_imgs()  # 调用基类截图方法
        print('Test Pass.')


if __name__ == '__main__':
    unittest.main()