import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utilities.readConfig import read_config
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

global driver

@pytest.fixture(scope='function')
def setup():
    global driver
    option=Options()
    option.add_argument('--disable-notifications')
    if read_config('basic','browser')=='chrome':
        driver=webdriver.Chrome(options=option,service=ChromeService(ChromeDriverManager().install()))
    elif read_config('basic','browser')=='edge':
        driver=webdriver.Edge(options=option,service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    driver.get(read_config('basic', 'url'))
    yield driver
    driver.quit()