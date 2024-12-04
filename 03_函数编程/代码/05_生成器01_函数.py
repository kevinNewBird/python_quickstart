## 1.基本使用
def f1():
    print(1234)
    yield 666


# （!!!）生成器函数执行的时候，并不会执行函数，而是得到生成器
f1 = f1()
print(f1.__next__())  # 1234


# print(f1.__next__()) # 没有数据后，抛出异常StopIteration

## 2.分段执行函数
def f2():
    print("段1")
    yield 1
    print("段2")
    yield 2


# （!!!）生成器函数执行的时候，并不会执行函数，而是得到生成器
f2 = f2()
print(f2.__next__())
print(f2.__next__())
# print(next(f2)) # 等价于 f2.__next__()

## 使用场景
num = 1000
batch = 50
print(f"------总共{num}衣服，分{batch}一批次-------")
def order():
    lst = []
    for i in range(num):
        lst.append(f"衣服{i}")
        if len(lst) == batch:
            yield lst # yield也有返回数据的作用

            # 下一次拿数据，清空列表
            lst = []


gen = order()
print(gen.__next__())
for lst in gen:
    print(lst)
