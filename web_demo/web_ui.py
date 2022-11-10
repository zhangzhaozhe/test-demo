from time import sleep

from selenium import webdriver

# 创建一个浏览器对象
driver = webdriver.Chrome()
# 访问指定的URL
driver.get('http://www.baidu.com')
# 定位元素：输入框，进行输入内容的操作
driver.find_element('id', 'kw').send_keys('虚竹')
# 点击元素
driver.find_element('id', 'su').click()
# 等待
sleep(3)
driver.quit()