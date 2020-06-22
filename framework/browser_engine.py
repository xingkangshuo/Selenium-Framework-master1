import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger("BrowserEngine").getlog()


class BrowserEngine(object):
    def open_browser(self):
        #读取配置文件
        config=ConfigParser()
        dir=os.path.dirname(os.path.abspath('.'))
        file_path=dir+'/config/config.ini'#此时需要在项目目录中创建config文件夹以及config.ini文件
        config.read(file_path)
        #读取配置文件属性
        browser=config.get("browserType","browserName")
        logger.info("You had select %s browser." % browser)
        url=config.get("testServer","URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            self.driver=webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            self.driver=webdriver.Chrome(dir+'/tools/chromedriver.exe')#创建tools文件夹并放入驱动
            logger.info("Starting Chrome browser.")
        elif browser=="IE":
            self.driver=webdriver.Ie(dir+'/tools/IEDriverServer.exe')
            logger.info("Starting IE browser.")
        self.driver.get(url)
        logger.info("Open url: %s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return self.driver
    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()