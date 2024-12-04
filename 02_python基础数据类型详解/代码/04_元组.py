# 元组（创建后元素不可变，主要是地址不可变，所以元组中存放的可变元素是可以修改里面的元素）
t1 = (1, 2)
print(type(t1))  # tuple
print(t1)  # (1,2)
print(t1[1:])
t2 = ("hh")  # 特殊情况，这个不是单个元组的表示方式
print(type(t2))  # str
t3 = ("hh",)  # 特殊情况，这个才是单个元组的表示方式
print(type(t3))  # tuple
print(t3)  # ('hh',)

t4 = ("b", "c", ["张三"])
t4[2].append("李四")
print(t4)  # ('b', 'c', ['张三', '李四'])
print(f"元组t4的0位置数据: {t4[0]}")

t5 = ()
print(type(t5))  # 空元组
t6 = tuple()
print(type(t6))
