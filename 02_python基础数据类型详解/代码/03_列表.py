# 列表的特性
print("--------------列表的特性-------------")
## 同字符串一样有索引和切片
lst = ["a", 1, "b"]
print(lst[0])
print(lst[1:])
print(lst[::-1])
## 越界
# print(lst[4]) # 越界
## 循环遍历
for item in lst:
    print(item)
## 列表长度
print(len(lst))
print()

# 列表的增删改查
print("--------------列表的增删改查-------------")
## 添加元素
lst2 = []
lst2.append("武大郎")
print(lst2)
lst2.insert(0, "潘金莲")
print(lst2)
lst2.extend(["叮当猫", "hello kitty"])
print(lst2)
## 删除元素
lst3 = ["a", "b", "c", "d"]
ret = lst3.pop(2)
print(lst3)
print(f"pop删除的元素：{ret}")
lst3.remove("d")
print(lst3)
## 修改
lst3[0] = "a_modify"
print(lst3)
## 查询
print(lst3[0])
print()

# 列表的其它操作
print("--------------列表的其它操作-------------")
## 排序
lst4 = [7, 4, 2, 3, 9, 1, 5]
lst4.sort()
print(lst4)
lst4.sort(reverse=True)
print(lst4)
## 嵌套使用
lst5 = ["a", "b",[1,2,3,["呼吸"]],"c"]
print(lst5[2][3][0]) # 呼吸

print()

#  创建空列表
l1 = []
l2 = list()
print(type(l1))
print(type(l2))
