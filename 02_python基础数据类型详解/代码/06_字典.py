# 1.字典的基本操作
print("---------------------字典的基本操作------------------------")
## 1.1.新增和修改
dic = dict()  # 创建空字典，或者{}
print(dic)  # {}
dic = {"java": "编程语言"}
print(dic)  # {'java': '编程语言'}
dic["c"] = "C语言"  # 新增
print(dic)  # {'java': '编程语言', 'c': 'C语言'}
dic["java"] = "我第一门学习的编程语言"  # 修改
print(dic)  # {'java': '我第一门学习的编程语言', 'c': 'C语言'}
dic.setdefault("java", "设置默认值")  # 设置默认值，如果字典中已经存在则不生效
print(dic)  # {'java': '我第一门学习的编程语言', 'c': 'C语言'}
dic["java"] = "再次修改"  # 修改
print(dic)  # {'java': '再次修改', 'c': 'C语言'}
print()

## 1.2.删除
dic2 = {"java": "编程语言2", "c": "C语言2"}
kv = dic2.popitem()  # ('c', 'C语言2')
print(kv)
print(dic2)
# dic2.pop("java")
# print(dic2)
# del dic2["c"]
# print(dic2)
# dic2.pop("c") # 键不存在，删除将报错
# del dic2["c"]   # 键不存在，删除将报错
# print(dic2)
dic2.clear()  # 清空
print(dic2)
print()

## 1.3.查找
dic3 = {"java": "java语言3", "c": "C语言3"}
print(dic3["c"])
print(dic3.get("java"))
print(dic3.get("java1010"))

# name = dic3.get(input("请输入你喜欢的编程语言："))
# if name is None:
#     print("俺们村没有这个编程语言...")
# else:
#     print(name)

# 2.进阶操作
## 2.1.遍历
### 2.1.1.基础使用
dic5 = {1: "java", 2: "c", 3: "python"}
print(dic5)
print(dic5.keys())  # dict_keys([1, 2, 3])
print(list(dic5.keys()))  # [1, 2, 3]
print(type(dic5.keys()))  # <class 'dict_keys'>
print(dic5.values())  # dict_values(['java', 'c', 'python'])
print(list(dic5.values()))  # ['java', 'c', 'python']
print(type(dic5.values()))  # <class 'dict_values'>
print(dic5.items())  # dict_items([(1, 'java'), (2, 'c'), (3, 'python')])
print(list(dic5.items()))  # [(1, 'java'), (2, 'c'), (3, 'python')]
print(type(dic5.items()))  # <class 'dict_items'>
# 直接遍历
for key in dic5:
    print(key, dic5[key])
## 2.1.2.键遍历
for s_key in dic5.keys():
    val = dic5.get(s_key)
    print(f"键[{type(s_key)}]：{s_key},值[{type(val)}]：{val}")
## 2.1.3.值遍历
for s_val in dic5.values():
    print(f"值[{type(s_val)}]：{s_val}")

## 2.1.4.键:值遍历
for s_key, s_val in dic5.items():
    print(f"键[{type(s_key)}]：{s_key},值[{type(s_val)}]：{s_val}")

for item in dic5.items():
    print(f"{item[0]}--{item[1]}")

print()
## （***）知识点：解构
a, b = 1, 2  # 定义了a,b两个变量，分别赋值1和2
### 对于列表和元组都可以使用解构操作，如下
c, d = (3, 4)
e, f = [5, 6]
lst = [7, 8]
h, g = lst
print(f"""a:{a},b:{b}
c:{c},d:{d}
e:{e},f:{f}
h:{h},f:{g}
""")

# 4.3.字典的嵌套
dic = {
    "name": "张三",
    "age": 19,
    "wife": {
        "name": "赵四",
        "assistant": {
            "name": "王五"
        }
    },
    "children": [
        {"name": "张小三", "age": 15},
        {"name": "张小四", "age": 18},
    ]
}
print(dic["wife"]["assistant"]["name"])
dic["children"][1]["age"] = dic["children"][1]["age"] + 1
print(dic)

## 4.4.字典的循环删除
tmp_key_lst = []
dic5 = {1: "java", 2: "c", 3: "python"}
for s_key, s_val in dic5.items():
    if s_val.startswith("py"):
        tmp_key_lst.append(s_key)

for key in tmp_key_lst:
    dic5.pop(key)

print(dic5)
