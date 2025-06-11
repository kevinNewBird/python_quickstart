# coding:utf-8
import pytest
from selenium import webdriver

driver_type = 'chrome'


#
@pytest.fixture()
def browser():
    global driver
    if driver_type == 'chrome':
        driver = webdriver.Chrome()
    elif driver_type == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()
    # 创建的是谷歌浏览器的驱动


@pytest.fixture()
def base_url():
    return 'https://www.baidu.com'
