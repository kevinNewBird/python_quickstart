# 整数
a = 10
print(a)

# 浮点数
b = 3.0
print(b)  # 3.0
print(10 / 3)  # 3.3333333333333335

# 布尔
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(""))  # False
print(bool("/"))  # True
lst = []
print(bool(lst))  # False
lst = [0]
print(bool(lst))  #True
print()

# 复数类型
print(type(1+2j)) # <class 'complex'>