# 元组
t1 = (1, 2)
print(type(t1))  # tuple
print(t1)  # (1,2)
print(t1[1:])
t2 = ("hh")
print(type(t2))  # str
t3 = ("hh",)
print(type(t3))  # tuple
print(t3)  # ('hh',)

t4 = ("b", "c", ["张三"])
t4[2].append("李四")
print(t4)  # ('b', 'c', ['张三', '李四'])
