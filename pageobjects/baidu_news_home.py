# coding=utf-8
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class NewsHomePage(BasePage):
    # 点击体育新闻入口
    sports_link = (By.XPATH,'//*[@href="http://news.baidu.com"]')

    def click_sports(self):
        self.click(*self.sports_link)
