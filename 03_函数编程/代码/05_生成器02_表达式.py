# 1.映射数据，[0,5)范围数据的遍历平方数
gen = (i ** 2 for i in range(5))  # 本质是一个迭代器
print(gen)  # <generator object <genexpr> at 0x100735a40>
# 生成器函数的数据不能重复使用(因为是迭代器，是往下执行的)
print(tuple(gen))  # (0, 1, 4, 9, 16)
# print(list(gen))  # [0, 1, 4, 9, 16] 生成器函数的数据不能重复使用(因为是迭代器，是往下执行的)

# （！！！）生成器函数的数据不能重复使用(因为是迭代器，是往下执行的)
# 一旦上面使用了list(gen)或者tuple(gen)，后面的代码将不会有数据打印
# for item in gen:
#     print(item)

# 2.过滤数据(获取0-10之间的偶数)
even_numbers = (x for x in range(10) if x % 2 == 0)
print(list(even_numbers))  # [0, 2, 4, 6, 8]

# 3.组合数据（每个元素是元组）
pairs = ((x, y) for x in [1, 2] for y in [3, 4])
print(list(pairs))  # [(1, 3), (1, 4), (2, 3), (2, 4)]

# 4.传递数据给函数(函数需要接受可迭代类型)
sum_data = sum((x for x in range(100) if x % 3 == 0))
print(f"0-100区间范围内3的倍数的和：{sum_data}")
