'''
用类实现栈
以及括号匹配问题
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0

# 括号匹配
def brace_match(s):
    match = {'}':'{',']':'[',')':'('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '{', '['}:
            stack.push(ch)
        else: # ch in {')', '}', ']'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else: # stack.get_top() == match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False
print(brace_match('[{{}[]()}]'))

