import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utilities.readConfig import read_config

@pytest.fixture(scope='function')
def setup():
    option=Options()
    option.add_argument('--disable-notifications')
    driver=webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get(read_config('basic', 'url'))
    yield driver
    driver.quit()