import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Utilities.generate_logs import get_logs
from Pages.BasePage import BasePageClass
from Pages.BrandNewCarsBasePage import BrandNewCars
from Utilities.readConfig import read_config

log=get_logs()
class NewCarsClass(BasePageClass):

    def __init__(self,driver):
        super().__init__(driver)
        log.info('clicking on view more brands')
        self.wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, read_config('locators', 'view_more_brands_XPATH')))).click()
        log.info('clicked on view more brands')
        time.sleep(2)


    def select_MarutiSuzuki(self):
        log.info('clicking on maruti suzuki cars')
        self.click('maruti_suzuki_xpath')
        log.info('clicked on maruti suzuki cars')
        return BrandNewCars(self.driver)

    def select_Mahindra(self):
        log.info('clicking on mahindra cars')
        self.click('mahindra_XPATH')
        log.info('clicked on mahindra cars')
        return BrandNewCars(self.driver)

    def select_TATA(self):
        log.info('clicking on tata cars')
        self.click('tata_XPATH')
        log.info('clicked on tata cars')
        return BrandNewCars(self.driver)

    def select_Bentley(self):
        log.info('clicking on bentley cars')
        self.click('bentley_XPATH')
        log.info('clicked on bentley cars')
        return BrandNewCars(self.driver)