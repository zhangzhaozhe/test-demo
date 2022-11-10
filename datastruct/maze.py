"""
用栈解决迷宫问题 深度优先搜索
"""

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for li in maze:
    for i in li:
        print(i, end='')
    print(end='\n')
dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1)
]

def maze_path(x1,y1,x2,y2):
    stack = []
    stack.append((x1, y1))
    while(len(stack) > 0):
        curNode = stack[-1]  # 当前节点
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 2表示走过了
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print('没有路')
        return False

maze_path(1,1,8,8)
for li in maze:
    for i in li:
        print(i, end='')
    print(end='\n')