fn = lambda a, b: a + b
print(fn)
print(fn(1, 2))

# filter函数: 过滤
# filter() 是 Python 内置的高阶函数，用于从可迭代对象（如列表、元组等）中筛选满足条件的元素，返回一个迭代器对象
print("*" * 40)
lst1 = [i for i in range(5)]
print(list(filter(lambda x: x > 2, lst1)))

# map函数: 计算
# 可以传列表和单个函数
print("*" * 40)
lst2 = [i for i in range(5)]
print(list(map(lambda x: x ** 2, lst2)))

fn1 = lambda x: x * 2
fn2 = lambda x: x ** 2
for i in range(5):
    print(list(map(lambda x: x(i), [fn1, fn2])))

# reduce函数
from functools import reduce

"""
     1         2         3         4
        \    /          / 
           3           / 
               \      /
                   6
                        \      /
                           10
"""
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
