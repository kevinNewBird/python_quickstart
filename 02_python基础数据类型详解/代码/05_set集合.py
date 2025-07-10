# 创建空集合
## 错误的方式
s = {}
print(type(s))  # <class 'dict'/>
## 正确的方式
s = set()
print(type(s))  # <class 'set'>

# set集合
# s = {1,2.0,"hehe",[]} # 报错，数组是可变数据，即不可hash
a = 2.0
s = {1, a, "hehe", (1, 23)}  # 可存放可hash的类型，比如字符串、数字、布尔、元组
a = 3.0
print(type(s))  # <class 'set'>
print(s)

# 常用操作
s2 = set()
s2.add("赵本山")
s2.add("狗蛋")
s2.add("狗剩儿")
print(s2)
s2.pop()  # 未知的删除元素，取决于当前最后一个元素是谁
print(s2)
# s2.remove("赵本山")
# print(s2)

# 交集、并集、差集
ss1 = {"张三", "赵四", "刘能"}
ss2 = {"tommy", "刘能"}
ret = ss1.difference(ss2)  # 取差集，原集合不发生变化。{'赵四', '张三'}
print('差集：',ret)
print('差集：',ss1 - ss2)
ret = ss1.intersection(ss2)  # 取交集，原集合不发生变化。{'刘能'}
print('交集：',ret)
print('交集：',ss1 & ss2)
ret = ss1.union(ss2)  # 取并集，原集合不发生变化。{'刘能', '张三', 'tommy', '赵四'}
print('并集：',ret)
print('并集：',ss1 | ss2)
# 合并两个集合中不同的元素
# {'tommy', '赵四', '张三'}
print('异或：', ss1 ^ ss2)

# 列表的去重
lst = ["张", "张"]
print(lst)
set1 = set(lst)
print(set1)
print(list(set1))

# 循环遍历
print("------循环遍历集合------")
for item in lst:
    print(item)

