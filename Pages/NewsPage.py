import time
from selenium.webdriver.support.wait import WebDriverWait
from Pages.BasePage import BasePageClass
from Utilities.generate_logs import get_logs
log=get_logs()
class NewsPageClass(BasePageClass):

    def __init__(self,driver):
        super().__init__(driver)
        self.wait=WebDriverWait(self.driver,30)

    def get_latest_news_details_of_specific_car(self,car_name):
        log.info('searching for car news')
        self.input_text('search_car_XPATH',car_name)
        self.click('select_car_XPATH')
        time.sleep(1)
        log.info('clicking on latest news icon')
        self.click('latest_news_icon_XPATH')
        # lst=[]
        # lst.append(self.get_text('news_heading_XPATH'))
        # lst.append(self.get_text('author_name_XPATH'))
        # lst.append(self.get_text('time_XPATH'))
        # print()
        # for i in lst:
        #     print(i)

