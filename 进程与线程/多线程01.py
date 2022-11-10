# ####################多线程基本用法#####################
# import threading
#
#
# def task(arg):
#     pass
#
#
# # 创建一个Thread对象(线程)，并封装线程被cpu调度时应该执行的任务和相关参数
# t = threading.Thread(target=task, args=('xxx',))
# # 线程准备就绪(等待CPU调度)，代码继续向下执行
# t.start()
#
# print('继续执行...')  # 主线程执行完所有代码，不结束(等待子线程)
# ####################多线程基本用法#####################


# ####################t.start()方法#####################
# t.start(),当前线程准备就绪
# import threading
#
#
# loop = 1000000
# number = 0
#
#
# def _add(count):
#     global number
#     for i in range(count):
#         number += 1
#
#
# t = threading.Thread(target=_add, args=(loop,))
# t. start()
#
# print(number)
# ####################t.start()方法#####################


# ####################t.join()方法#####################
# t.join() 等待当前线程的任务执行完毕后再向下执行
import threading


number = 0


def _add():
    global number
    for i in range(1000000):
        number += 1


t = threading.Thread(target=_add)
t.start()
t.join()  # 主线程等待中

print(number)

# ####################t.join()方法#####################

