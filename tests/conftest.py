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
    
    def tear_down():
        driver.quit()
    
    request.cls.driver = driver
    yield driver
    request.addfinalizer(tear_down)

    
def flaky_test(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < max_retries:
                try:
                    result = func(*args, **kwargs)
                    print(f"Success on attempt {attempt + 1}")
                    return result 
                except Exception as e:
                    attempt += 1
                    print(f"Retrying... Attempt {attempt} of {max_retries}")
                    if attempt >= max_retries:
                        print("Max retries reached. Raising exception.")
                        raise e
                    time.sleep(delay)
        return wrapper
    return decorator


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
    
