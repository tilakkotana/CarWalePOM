import os
from datetime import datetime

import pytest
from pathlib import Path
from selenium.webdriver.support.wait import WebDriverWait
from Pages.HomePage import HomePageClass
from Utilities.write_excel import write_to_excel
from Utilities.generate_logs import get_logs
log=get_logs()
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = Path.cwd().parent / f'Excel/CarDetails_{current_time}.xlsx'
class Test_new_cars:
    @pytest.fixture(scope='class')
    def setup_class(self):
        log.info('test new cars details started')
        if os.path.exists(file_path):
            os.remove(file_path)
            log.info('deleted CarDetails excel file')
        return file_path

    @pytest.fixture(autouse=True)
    def setup_method(self,setup):
        self.driver=setup
        self.find_new_cars = HomePageClass(self.driver)
        self.wait=WebDriverWait(self.driver,30)

    def test_get_maruti_suzuki_cars_details(self,setup_class):
        log.info('extracting maruti suzuki car details')
        result=self.find_new_cars.go_to_find_new_cars().select_MarutiSuzuki().get_details()
        log.info('writing maruti suzuki car details in excel')
        write_to_excel('Maruti Suzuki',result,file_path)
        log.info('maruti suzuki car details saved in excel')

    def test_get_mahindra_cars_details(self,setup_class):
        log.info('extracting mahindra car details')
        result=self.find_new_cars.go_to_find_new_cars().select_Mahindra().get_details()
        log.info('writing mahindra car details in excel')
        write_to_excel('Mahindra', result, file_path)
        log.info('mahindra car details saved in excel')

    def test_get_tata_cars_details(self,setup_class):
        log.info('extracting tata car details')
        result=self.find_new_cars.go_to_find_new_cars().select_TATA().get_details()
        log.info('writing tata car details in excel')
        write_to_excel('Tata', result, file_path)
        log.info('tata car details saved in excel')

    def test_get_bentley_cars_details(self,setup_class):
        log.info('extracting bentley car details')
        result=self.find_new_cars.go_to_find_new_cars().select_Bentley().get_details()
        log.info('writing bentley car details in excel')
        write_to_excel('Bentley', result, file_path)
        log.info('bentley car details saved in excel')












