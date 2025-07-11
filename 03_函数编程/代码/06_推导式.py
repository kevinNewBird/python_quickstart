# 1.列表推导式
# 循环往列表里添加0-10的数据
lst = [i for i in range(10) if i > 4]
print(lst)
# 假设我们不想获取列表，而想要获取生成器，在后续去遍历。可使用如下方式：
gen = (i for i in range(10) if i >6)
print(type(gen))
lst = [i for i in gen]
print('使用generator-》list：', lst)
gen = (i for i in range(10) if i >7)
st1 = {i for i in gen}
print('使用generator-》set：', st1)

lst1 = ["allen", "tommy", "tony"]
lst2 = [item.upper() for item in lst1]
print(lst2)

# 2.集合推导式
set1 = {i for i in range(10)}
print(set1)

# 3.字典推导式
# 请将下列的列表修改成字典
lst3 = ["刘大嘴", "李大脑袋", "狗剩儿"]
dic = {index: data for index, data in enumerate(lst3) if index % 2 == 0}
# dic = {index: lst3[index] for index in range(len(lst3))}
print(dic)

# 4.多重循环
rows = range(1,3)
print(type(rows))
cols = range(1,3)
cells = []
for row in rows:
    for col in cols:
        cells.append((row, col))
# [(1, 1), (1, 2), (2, 1), (2, 2)]
print(cells)

# [(1, 1), (1, 2), (2, 1), (2, 2)]
# cells2 = [(r,c) for r in range(1,3) for c in range(1,3)]
# 每循环一次第一个循环，第二个循环都将完全循环
cells2 = [(r,c) for r in rows for c in rows]
print(cells2)

# 5.嵌套推导式
# [[0], [0, 1]]
cells3 = [[j for j in range(i)] for i in range(1,3)]
print(cells3)

# 嵌套循环展开二维列表
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]  # 输出：[1, 2, 3, 4]
print(flattened)
