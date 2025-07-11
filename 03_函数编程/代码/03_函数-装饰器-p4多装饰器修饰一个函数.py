import time


def wrapper1(game):
    def inner(*args, **kwargs):
        print("进入wrapper1")
        ret = game(*args, **kwargs)
        print("结束wrapper1")
        return ret

    return inner


def wrapper2(game):
    def inner(*args, **kwargs):
        print("进入wrapper2")
        ret = game(*args, **kwargs)
        print("结束wrapper2")
        return ret

    return inner


@wrapper1  # wrapper1装饰wrapper2装饰器，即wrapper1(wrapper2.inner), 实际返回的封装函数wrapper1.inner
@wrapper2  # wrapper2装饰play_dnf方法，即wrapper2(play_dnf), 实际返回的封装函数wrapper2.inner
def play_dnf(username, password):
    print("你好啊，我叫赛利亚，今天又是美好的一天", username, password)
    return "神器-寒霜剑"


"""
进入wrapper1
进入wrapper2
你好啊，我叫赛利亚，今天又是美好的一天 铸币 admin123
结束wrapper2
结束wrapper1
神器-寒霜剑
"""
print(play_dnf("铸币", "admin123"))


class Dog:
    def __init__(self, name):
        self.__name = name

    @property  # 类似于getName
    def name(self):
        return self.__name

    @name.setter  # 类似于setName
    def name(self, name):
        self.__name = name


## 测试数组的性能
## 计时器
def timer(func):
    def inner(*args, **kwargs):
        start = time.time_ns()
        ret = func(*args, **kwargs)
        print("函数{}执行耗时：{}ns".format(func.__name__, time.time_ns() - start))
        return ret

    return inner


@timer
def removePos(lst: list, index: int):
    if not lst:
        pass
    del lst[index]


lst1 = [i for i in range(1, 1000000)]
lst2 = [i for i in range(1, 1000000)]
removePos(lst1, 0)
removePos(lst2, -1)
