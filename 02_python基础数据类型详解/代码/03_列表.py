# 列表的特性
print("--------------列表的特性-------------")
## 同字符串一样有索引和切片
lst = ["a", 1, "b"]
print(lst[0])
print(lst[1:])
print(lst[::-1])
## 越界
# print(lst[4]) # 越界
print("数组长度：%d" % (len(lst)))
## 循环遍历1
for item in lst:
    print(item)

## 循环遍历2，使用enumerate函数遍历
print("--------------使用函数enumerate遍历：")
for index, item in enumerate(lst):
    print(index, item)
## 列表长度
print("数组长度：%d" % (len(lst)))

# 在循环中删除元素，需要使用一个临时列表进行操作
print("---------创建新列表用于处理循环遍历删除----------")
new_lst = []
for item in lst:
    if isinstance(item, int):
        new_lst.append(item)

## 列表长度
print(new_lst)
print("数组长度：%d" % (len(new_lst)))
print()

# 列表的增删改查
print("--------------列表的增删改查-------------")
## 添加元素
lst2 = []
lst2.append("武大郎")  # 追加
print(lst2)
lst2.insert(0, "潘金莲")  # 指定位置插入
print(lst2)
lst2.extend(["叮当猫", "hello kitty"])  # 合并列表
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
lst5 = ["a", "b", [1, 2, 3, ["呼吸"]], "c"]
print(lst5[2][3][0])  # 呼吸

print()

#  创建空列表
l1 = []
l2 = list()
print(type(l1))
print(type(l2))
