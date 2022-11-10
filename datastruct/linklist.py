"""
创建链表 头插、尾插
链表的遍历
"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next
def create_linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head
def creat_linklist_tai(li):
    head = tail = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head
lk = create_linklist([1,2,3])
print_linklist(lk)
lk2 = creat_linklist_tai([1,2,3])
print_linklist(lk2)


