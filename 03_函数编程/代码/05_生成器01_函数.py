## 1.基本使用
def f1():
    print(1234)
    yield 666


f1 = f1()
print(f1.__next__())


# print(f1.__next__())

## 2.分段执行函数
def f2():
    print("段1")
    yield 1
    print("段2")
    yield 2


f2 = f2()
print(f2.__next__())
print(f2.__next__())


## 使用场景
def order():
    lst = []
    for i in range(10000):
        lst.append(f"衣服{i}")
        if len(lst) == 50:
            yield lst

            # 下一次拿数据，清空列表
            lst = []


gen = order()
print(gen)
print(gen.__next__())
for lst in gen:
    print(lst)

