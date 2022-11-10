'''
 LoginPage页面对象，主要用于实现web系统的登录操作
'''
from selenium import webdriver

from base.base_page import BasePage
from selenium.webdriver.common.by import By

# 登录页面对象
class LoginPage(BasePage):
    # 页面URL
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    # 页面的关键元素
    user = (By.NAME, 'accounts')
    pwd = (By.NAME, 'pwd')
    button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')

    # 页面的业务流程
    def login(self, u, p):
        self.visit(self.url)
        self.input(self.user, u)
        self.input(self.pwd, p)
        self.click(self.button)
        # self.quit()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('666666', '666666')
