import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Library.config import Config
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=["Chrome","Edge"])
@pytest.fixture(params=["Chrome"])
def _driver(request):
    if request.param=="Chrome":
        opt = webdriver.ChromeOptions()
        time.sleep(2)
        opt.add_argument("--disable-notifications")
        driver=webdriver.Chrome(Config.Chrome_Driver_path,options=opt)
    # if request.param=="Firefox":
    #     opt = webdriver.ChromeOptions()
    #     opt.add_argument("--disable-notifications")
    #     driver = webdriver.Firefox(Config.Firefox_Driver_path)

    # elif request.param=="Edge":
    #     opt = webdriver.ChromeOptions()
    #     opt.add_argument("--disable-notifications")
    #     driver = webdriver.Edge(Config.Edge_Driver_path)
    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.save_screenshot(Config.Screenshot_path+'test_bag.png')
    time.sleep(2)

# import pytest
