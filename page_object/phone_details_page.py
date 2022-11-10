'''
实现手机商品详情页的页面对象
'''
from time import sleep

from selenium import webdriver

from base.base_page import BasePage
from selenium.webdriver.common.by import By

class PhonePage(BasePage):
    # URL
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html'

    # 元素位置
    type1 = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[1]/ul/li[1]')
    golden = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[2]/ul/li[1]')
    sg = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/dl/dd/div[2]/div[3]/form/div[1]/div[3]/ul/li[2]')
    shop_car = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[3]/div[3]/div/button')

    # 添加购物车
    def add(self):
        self.visit(self.url)
        self.max_window()
        sleep(3)
        self.click(self.type1)
        sleep(3)
        self.click(self.golden)
        sleep(3)
        self.click(self.sg)
        sleep(3)
        self.click(self.shop_car)
        # self.quit()
#
if __name__ == '__main__':
    driver = webdriver.Chrome()
    pg = PhonePage(driver)
    pg.add()