# 1.列表推导式
# 循环往列表里添加0-10的数据
lst = [i for i in range(10) if i > 4]
print(lst)

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
