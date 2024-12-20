# 迭代器的两种方案
# 1.使用内置函数
it = iter("你叫什么名字啊")  # 使用内置函数获取迭代器
print(it)  # <str_iterator object at 0x000002C910EC5390>
print(next(it))  # 你

# 2.使用特殊方法
it2 = "呵呵哒".__iter__()  # 使用特殊方法获取迭代器
print(it2)  # <str_iterator object at 0x000002C910F07B80>
print(it2.__next__())

# 3.模拟for循环
it3 = "数据9527".__iter__()
while 1:
    try:
        data = it3.__next__()
        print(data)
    except StopIteration:
        break

it4 = "数据9527".__iter__()
for data in it4:
    print(data)
