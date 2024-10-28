import os
import sys
sys.path.append(os.getcwd())

from utils.common_imports import *
from utils.logger import *

@allure.step("Setup the browser")
@pytest.fixture(scope='class',autouse=True)
def setup_fixture(request):

    if request.config.getoption('--firefox'):
        driver = webdriver.Firefox()
    elif request.config.getoption('--headless'):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome()
    

    request.cls.driver = driver
    yield driver
    driver.quit()

    
def pytest_addoption(parser):
    parser.addoption(
        '--chrome',
        help = 'Runs in chrome as default browser',
        action = 'store_true',
        default = True
    )
    parser.addoption(
        '--firefox',
        help = 'Runs in Firefox browser',
        action = 'store_true',
        default = False
    )
    parser.addoption(
        '--headless',
        help = 'Runs in Headless browser',
        action = 'store_true',
        default = False
    )
    
