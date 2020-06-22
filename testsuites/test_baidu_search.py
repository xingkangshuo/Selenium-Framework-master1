import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browse=BrowserEngine()
        cls.driver=cls.browse.open_browser()
    @classmethod
    def tearDownClass(cls):
        cls.browse.quit_browser()
    def test_baidu_search(self):
        """
                这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
                :return:
         """
        homepage=HomePage(self.driver)
        homepage.type_search("苍井空")
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.get_windows_imgs()
        try:
            assert "苍井空" in self.driver.title
            print("Test Pass")
        except Exception as e:
            print('Test Fail.',e)

    def test_search2(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_imgs()  # 调用基类截图方法
        print('Test Pass.')

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print(homepage.get_page_title())

if __name__ == '__main__':
    unittest.main()
