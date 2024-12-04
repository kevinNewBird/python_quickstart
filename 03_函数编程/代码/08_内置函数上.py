# 1.数字相关的内置函数
## 1.1.进制转换
a = 18
print(bin(a))  # 十进制转为二进制
print(oct(a))  # 十进制转为八进制
print(hex(a))  # 十进制转为十六进制

b = 0b10010  # 二进制
print(int(b))  # 二进制转为十进制

## 1.2.数学运算
print(abs(-2.3))  # 返回一个数的绝对值: 2.3
print((divmod(10, 3)))  # 商和余数: (3,1)
print(round(3.5))  # 四舍五入: 4
print(pow(2, 3))  # 返回一个数的指定次幂: 8
print(sum([1, 2, 3, 4]))  # 求和: 10
print(min(1, 2, 3, 4))  # 最小值：1
print(max(1, 2, 3, 4))  # 最大值：4

# 2.数据结构相关的内置函数
## 2.1.序列
### 2.1.1.列表和元组
print(list({1, 2, 3}))  # [1, 2, 3]。将集合转换为列表 （本质是循环）
print(list("呵呵哒"))  # ['呵', '呵', '哒']。将字符串转换为列表（本质是循环）

print(tuple([1, 2, 3]))  # (1, 2, 3)
print(tuple("么么哒"))  # ('么', '么', '哒')
### 2.1.2.翻转和切片
r = reversed("14222349")  # 翻转后得到的并不是字符串，而是reversed类型
print(type(r))  # <class 'reversed'>
print("".join(r))  # 94322241
print("14222349"[::-1])  # 94322241
print(list(reversed([3, 4, 2, 1])))  # [1, 2, 4, 3]
s = slice(1, 4, 2)
print("12345678"[s])  # 24
print("12345678"[1:4:2])  # 24

### 2.1.3.字符串相关
print(str(1))  # "1"
print(str([1, 2, 3]))  # "[1,2,3]"
print(type(str([1, 2, 3])))  # <class 'str'>
print(format(18, "b"))  # o: 转为8进制，x：转为16进制，b：转为2进制
print(format(18, "08b"))  # 08b表示得到一个由0补充的8位二进制（只能补齐不能切割）
a = "中"  # 在python的内存中使用的是unicode
print(ord(a))  # 打印“中”在unicode中的码位是20013
print(chr(20013))  # 接收码位，输出文字

# for i in range(65536):
#     print(chr(i)+" ",end="")

### 相关内置函数
print(all([12, "呵呵"]))  # True。相当于and逻辑运算符
print(all([0, 12, "呵呵"]))  # False。
print(any([0, 12, "呵呵"]))  # True
print(any([0, ""]))  # False
lst = ["张无忌", "张翠三", "张三丰"]
# (0, '张无忌')
# (1, '张翠三')
# (2, '张三丰')
for item in enumerate(lst):
    print(item)

# 0 张无忌
# 1 张翠三
# 2 张三丰
for index, item in enumerate(lst):
    print(index, item)
