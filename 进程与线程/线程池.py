"""
线程池
"""

# ---------------------------1.使用线程池-------------
import time
from concurrent.futures import ThreadPoolExecutor

def task(video_url):
    print('开始执行任务', video_url)
    time.sleep(5)

# 创建线程池,最多维护10个线程。
pool = ThreadPoolExecutor(10)

url_list = ["www.xxxx-{}.com".format(i) for i in range(300)]
for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池﹔如果没有空闲线程，则等待。
    pool.submit(task, url)

print('END')


# ---------------------------2.等待线程池的任务执行完毕。-------------
import time
from concurrent.futures import ThreadPoolExecutor

def task(video_url):
    print('开始执行任务', video_url)
    time.sleep(5)

# 创建线程池,最多维护10个线程。
pool = ThreadPoolExecutor(10)

url_list = ["www.xxxx-{}.com".format(i) for i in range(300)]
for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池﹔如果没有空闲线程，则等待。
    pool.submit(task, url)

print('执行中...')
pool.shutdown(True)  # 等待线程池中的任务执行完毕后，在继续执行
print('继续走')


# ----------------------------------3.任务执行完任务,再干点其他事。-------------
# 可以做分工，例如:task专门下载,done专门将下载的数据写入本地文件。
import time
import random
from concurrent.futures import ThreadPoolExecutor,Future

def task(video_url):
    print('开始执行任务',video_url)
    time.sleep(2)
    return random.randint(0,10)

def done(response):
    print('任务执行后的反回值',response.result())

# 创建线程池，最多维护10个线程
pool = ThreadPoolExecutor(10)

url_list = ["www.xxxx-{}.com".format(i) for i in range(15)]

for url in url_list:
    future = pool.submit(task, url)
    future.add_done_callback(done)  # 是子线程执行

# ----------------------------------4.最终统一获取结果。-------------
import time
import random
from concurrent.futures import ThreadPoolExecutor,Future

def task(video_url):
    print('开始执行任务',video_url)
    time.sleep(2)
    return random.randint(0,10)

def done(response):
    print('任务执行后的反回值',response.result())

# 创建线程池，最多维护10个线程
pool = ThreadPoolExecutor(10)

future_list = []

url_list = ["www.xxxx-{}.com".format(i) for i in range(15)]
for url in url_list:
    future = pool.submit(task, url)
    future_list.append(future)

pool.shutdown(True)
for fu in future_list:
    print(fu.result())