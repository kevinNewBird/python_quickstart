# 1.整数
a = 10
print(a)

# 2.进制
a = 0b10  # 二进制
b = 0o10  # 八进制
c = 0x10  # 十六进制
print(a, b, c, sep='=====', end='\n')

# 3.科学计数法
d = 9.815e2  # 可省略+号
e = 98.345e-2
print(d, e, sep='=====', end='\n')

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