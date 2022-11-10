"""
python内置队列
以及实现linux的tail命令，打印一个txt文件的后n行
"""
from collections import deque
q = deque([1,2,3,4,5],5)
q.append(6)   # 队尾进队
print(q.popleft()) # 队首出队
# q.appendleft(1) # 队首进队
# q.pop() # 队尾出队

def tail(n):
    with open('test.txt','r') as f:
        q = deque(f, n)
        return q

for line in tail(5):
    print(line, end='')