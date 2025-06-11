# coding:utf-8
import time

from page.baidu_page import BaiduPage


class TestSearch():
    def test_baidu_search_case(self, browser, base_url):  # 用到了钩子函数 browser,与base_url在conftest.py中定义
        # 创建Page类的对象
        page = BaiduPage(browser)
        # 打开网址
        page.get(base_url)  # 这个get方法由Page提供

        page.search_input.send_keys('pytest')  # pytest是用于搜索的关键字

        # 点击按钮
        page.search_button.click()

        time.sleep(2)

        # 断言
        assert browser.title == 'pytest_百度搜索'
