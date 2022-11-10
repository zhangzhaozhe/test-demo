"""
异常处理的基本格式 2种
"""
# 1.------------------------
try:
    pass  # 逻辑代码
except Exception as e:
    pass  #  try中的代码如果有异常，则此代码块中的代码会执行。

# 2.----------------------------------
try:
    pass  # 逻辑代码
except Exception as e:
    pass  #  try中的代码如果有异常，则此代码块中的代码会执行。
finally:
    pass  # try中的代码无论是否报错，finally中的代码都会执行，一般用于释放资源.

# --------------例子---------------
try:
    file_object = open('xxxx.log')
    # ...
except Exception as e:
    # 异常处理
    pass
finally:
    file_object.close()

