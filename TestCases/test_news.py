import pytest
from Utilities.readConfig import read_config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePageClass
import allure
from Utilities.generate_logs import get_logs
log=get_logs()

@pytest.mark.usefixtures('setup')
class Test_News:

    @pytest.fixture(autouse=True)
    def start(self,setup):
        self.driver=setup
        self.wait=WebDriverWait(self.driver,30)
        self.news=HomePageClass(self.driver)

    def test_news(self,start):
        self.news.go_to_reviews_and_news().get_latest_news_details_of_specific_car('Mahindra Thar')
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,read_config('locators','news_heading_XPATH'))))
        allure.attach(self.driver.get_screenshot_as_png(),name='News Image',attachment_type=allure.attachment_type.PNG)
        log.info('news screenshot attached to allure')
