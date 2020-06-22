from framework.base_page import BasePage
from selenium.webdriver.common.by import By
class HomePage(BasePage):
    input_box=(By.ID,'kw')
    search_submit_btn=(By.XPATH,'//*[@id="su"]')
    news_link=(By.XPATH,'//*[@id="url"]/a[@name="tj_trnews"]')

    def type_search(self,text):
        self.type(*self.input_box,text=text)#text为命名关键字参数必须传入参数名

    def send_submit_btn(self):
        self.click(*self.search_submit_btn)

    def click_news(self):
        self.click(*self.news_link)