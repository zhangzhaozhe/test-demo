import unittest
from page_object.login_page import LoginPage
from page_object.phone_details_page import PhonePage
from selenium import webdriver

class CaseDemo(unittest.TestCase):
    # 用例运行前置
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    # 用例运行后置
    def tearDown(self) -> None:
        self.driver.quit()
    # 用例实现登录并添加购物车流程
    def test_1(self):

        lp = LoginPage(self.driver)
        pg = PhonePage(self.driver)
        lp.login('666666', '666666')
        pg.add()

    # 用例实现登录操作
    def test_2(self):

        lp = LoginPage(self.driver)
        lp.login('666666', '666666')

if __name__ == '__main__':
    unittest.main()