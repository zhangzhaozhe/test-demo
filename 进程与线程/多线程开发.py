"""
start(),join(),t.setDaemon(Ture or False)守护线程必须放在start之前
"""
import threading
def task(arg):
    pass
# 创建一个Thread对象（线程)，并封装线程被cPu调度时应该执行的任务和相关参数。
t = threading.Thread(target=task, args=('xxx',))
# 线程准备就绪（等待cPu调度)，代码继续向下执行。
t.start()



# ---------------线程的常见方法--------------
# t.start()，当前线程准备就绪（等待CPU调度，具体时间是由CPU来决定)。
import threading

loop = 10000000
number = 0

def _add(count):
    global number
    for i in range(count):
        number += 1

t = threading.Thread(target=_add, args=(loop,))
t.start()
t.join()  # 主线程等待中
print(number)


# ---------------守护线程--------------
import threading
import time

def task(arg):
    time.sleep(5)
    print('任务')

t = threading.Thread(target=task,args=(11,))
t.setDaemon(True)
t.start()

print('END')