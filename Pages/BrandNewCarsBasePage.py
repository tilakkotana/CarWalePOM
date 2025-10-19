from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.readConfig import read_config
from Utilities.generate_logs import get_logs
log=get_logs()
class BrandNewCars:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,30)
    def get_details(self):
        car_details_list=[]
        car_names=self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,read_config('locators','car_names_XPATH'))))
        car_names_list=[]
        for i in car_names:
            car_names_list.append(i.text)
        car_prices=self.wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,read_config('locators','car_prices_XPATH'))))
        car_prices_list = []
        for i in car_prices:
            car_prices_list.append(i.text)
        for i in range(len(car_prices_list)):
            car_details_list.append([car_names_list[i],car_prices_list[i]])
        return car_details_list
