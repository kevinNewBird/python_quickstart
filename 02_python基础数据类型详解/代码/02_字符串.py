# 1.字符串格式化
print("-----------------字符串格式化-------------")
## 1.1.使用占位符
s = "我是%s，%d岁，身高%f米" % ("a", 2, 3.0)
print(s)
s = "我是%s" % "b"
print(s)

## 1.2.使用format方法
s1 = "我是{}，{}岁，身高{}米".format("a", 2, 3.0)
print(s1)

## 1.3.使用f-string
name = "c"
age = 12
tall = 3.0
s2 = f"我是{name}，{age}岁，身高{tall}米"
print(s2)
print("\n")

# 2.切片
print("-----------------字符串切片-------------")
## 2.1.从头到尾，每隔2个元素正向或反向提取一个元素
s = "我是刘德华"
print(s[::2])  # 我刘华
print(s[2::2])  # 刘华
print(s[::-2])  # 华刘我
print(s[-2::-2])  # 德是
print(s[-2::-1])  # 德刘是我
print(s[-2:])  # 德华
print(s[-2::2])  # 德

print(s[:])  # 我是刘德华。正向以步长1从头提取到尾
print()

# 3.字符串常用操作
## 3.1.字符串大小写转换
print("-----------------字符串大小写转换-------------")
### 3.1.1. 字符串首字母大写
s = "python"
print(s.capitalize())  # Python
### 3.1.2. 所有单词的首字母大写
s1 = "i have a dream"
print(s1.title())  # I Have A Dream
s2 = "i ha,ve a dream"
print(s2.title())  # I Ha,Ve A Dream
### 3.1.3.字符串全小写
s3 = "I HAVE A DREAM"  # i have a dream
print(s3.lower())
### 3.1.4.字符串全大写
s4 = "i have a dream"
print(s4.upper())  # I HAVE A DREAM
print()

# 3.2.字符串的替换和切割
print("-----------------字符串的替换和切割-------------")
# 3.2.1.替换
sr = "  我是谁，我来自哪里！！   \n  \t"
print(sr.strip())
sr2 = "python_java_c_csharp_javascript"
print(sr2.replace("_", "#"))
# 3.2.2.切割
sp = "python_java_c_csharp_javascript"
print(sp.split("_"))
print()

# 3.3.字符串的查找和判断
print("-----------------字符串的查找和判断-------------")
## 3.3.2.查找
sf = "还有谁，告诉我还有谁"
print(sf.find("还有谁"))
# print(sf.find("还有谁11"))
# print(sf.rfind("还有谁"))
print(sf.index("还有谁"))
# print(sf.index("还有谁22"))
# print(sf.rindex("还有谁"))
print("还有谁" in sf)
print("还有谁" in sf)  # True
print("还有谁11" not in sf)  # True
## 3.3.2.判断
sif = "张三丰"
print(sif.startswith("张"))
print(sif.endswith("张"))
sint = "11"
print(f"{sint}是否为整数: %s" % sint.isdigit())
print(f"{sint}是否为整数: %s" % sint.isdecimal())
print(f"{sint}是否为整数: %s" % sint.isnumeric())
sbyte = b'1'  # 二进制
print(f"{sbyte}是否为整数: %s" % sbyte.isdigit())  # True
# print(f"{sbyte}是否为整数: %s" % sbyte.isdecimal()) # 报错
# print(f"{sbyte}是否为整数: %s" % sbyte.isnumeric()) # 报错
sint = "四"  # 汉字
print(f"{sint}是否为整数: %s" % sint.isdigit())  # False
print(f"{sint}是否为整数: %s" % sint.isdecimal())  # False
print(f"{sint}是否为整数: %s" % sint.isnumeric())  # True
sint = "Ⅳ"  # 罗马数字
print(f"{sint}是否为整数: %s" % sint.isdigit())  # False
print(f"{sint}是否为整数: %s" % sint.isdecimal())  # False
print(f"{sint}是否为整数: %s" % sint.isnumeric())  # True
# 字符长度
s = "12345"
print(len(s)) # 5
# 字符连接
lst = ["java", "python", "c"]
print("_".join(lst))
print()
