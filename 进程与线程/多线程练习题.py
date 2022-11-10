"""
多线程练习题
data.txt中文件中共有10020条数据，请为每100行数据创建一个线程，并在线程中把当前100条数据的num列相加并打印
subscript_id,erotic,num
ASDFSFFFFFFHJ,5,1
ADUHEUIHIUHIH,5,99
....
"""
import threading
def task(row_list):
    num_list = [int(row.split(',')[-1]) for row in row_list]
    result = sum(num_list)
    print(result)

def run():
    file_object = open('data.txt',mode='r',encoding='utf-8')
    file_object.readline() # 只读第一行
    row_list = []
    for line in file_object:
        row_list.append(line.strip())
        if len(row_list) == 100:
            t = threading.Thread(target=task,args=(row_list,))
            t.start()
            row_list = []
    if row_list:
        t = threading.Thread(target=task, args=(row_list,))
        t.start()
    file_object.close()

if __name__ == '__main__':
    run()