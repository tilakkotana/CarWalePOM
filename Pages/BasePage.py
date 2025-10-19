from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.readConfig import read_config


class BasePageClass:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,30)
    def hover_on(self,locator):
        element=self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,read_config('locators',locator))))
        action=ActionChains(self.driver)
        action.move_to_element(element).perform()
    def click(self,locator):
        element=self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,read_config('locators',locator))))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    def input_text(self,locator,value):
        element=self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, read_config('locators', locator))))
        element.clear()
        element.send_keys(value)
    def get_text(self,locator):
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,read_config('locators',locator)))).text
    def select_using_text(self,locator,txt):
        lst=self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,read_config('locators',locator))))
        for i in lst:
            if i.text==str(txt):
                i.click()
                break

