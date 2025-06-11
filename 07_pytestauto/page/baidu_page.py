# coding:utf-8
from poium import Page, Element, Elements


class BaiduPage(Page):
    search_input = Element(id_='kw', describe='搜索框')
    search_button = Element(id_='su', describe='搜索按钮')

    settings = Element(link_text='设置', describe='设置下拉框')

    search_setting = Element(css='.pfpanel-bd', describe='搜索设置选项')
    # 定位一组元素
    search_result = Elements(xpath='//div/h3', describe='搜索结果')
