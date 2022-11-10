"""
创建一个关键字驱动类对象，封装所有的常用关键字，作为工具类的存在
常规操作：1.启动浏览器 2.URL的访问 3.元素定位 4.输入 5.点击 6.推出 ....
"""
from selenium import webdriver
from time import time
from selenium.webdriver.common.by import By

# 创建driver对象：基于python的反射机制来实现driver对象的创建
def open_browser(browser_type):
    driver = getattr(webdriver, browser_type)()
    return driver

class KeywordDemo:


    # 构造函数
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 元素定位2.0:基于By对象解析元组内容生成元素定位操作
    def locator2(self, loc):
        return self.driver.find_element(*loc)

    # 元素定位3.0：基于str来生成定位元素
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 元素的输入
    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 元素的点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 访问指定的额URL
    def visit(self, url):
        self.driver.get(url)

    # 关闭浏览器，释放资源
    def quit(self):
        self.driver.quit()


