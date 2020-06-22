import time
from framework.logger import Logger
import os.path
from selenium.common.exceptions import NoSuchElementException
logger=Logger('BasePage').getlog()


class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def quit_browser(self):
        self.driver.quit()
        logger.info("browser is quit")
    def forword(self):
        self.driver.forword()
        logger.info("Click forward on current page.")
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)
    #截屏
    def get_windows_imgs(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        screen_name=file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.driver.get_windows_imgs()
    #寻找元素方法
    def find_element(self,*selector):#传入可变参数实现对元组的拆分
        try:
            element=self.driver.find_element(*selector)
            logger.info("The element looked up is %s "% (selector[1]))
            return element
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()
    #清除文本框
    def clear(self,*selector):
        el=self.find_element(*selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_imgs()
    #输入
    def type(self,*selector,text):
        self.clear(*selector)
        el = self.find_element(*selector)
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_imgs()

    def click(self, *selector):
        el = self.find_element(*selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    #获得网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

