"""
单例模式
"""

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance = object.__new__(cls)
        return cls._instance


class Myclass(Singleton):
    def __init__(self,a):
        self.a = a

a = Myclass(10)
b = Myclass(20)
print(a.a)
print(b.a)