# for循环
 主要用来循环可迭代对象的（比如字符串）
## 1.语法
```properties
# 常用语法
for 变量 in 可迭代的东西:
   代码

# 同else一起使用
for 变量 in 可迭代的东西:
   代码
else:   # for循环没有break时生效
    代码
```
上述代码的作用：把可迭代的东西中的每一项内容拿出来，挨个赋值给变量，每一赋值都要执行一次循环体（代码）
 
for循环想要计数，必须要借助于range</br>
range(n): 从0数到n，不包含n</br>
range(m,n): 从m数到n，不包含n</br>
range(m,n,step): 从m数到n，步进为step，不包含n</br>

平时用的是for循环，while一般用的是死循环