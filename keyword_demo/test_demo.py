"""
基于工具类(关键字驱动对象)实现的自动化测试
"""
from keyword_demo.keyword_for_test import KeywordDemo

# 创建关键字驱动类的对象
kd = KeywordDemo('Chrome')
kd.visit('http://www.baidu.com')
kd.input('id', 'kw', '虚竹')
kd.click('id', 'su')
kd.quit()