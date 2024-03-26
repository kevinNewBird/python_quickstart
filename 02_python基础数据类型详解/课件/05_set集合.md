# 1.定义
存储数据的无序容器，元素可以通过逗号分隔。</br>
特点：存储的元素类型必须是能进行hash计算的，可哈希的数据类型可以认为是不可变的数据（数字、字符串、元组、布尔值）。</br>
注意：python中set集合存储数据时，需要对数据进行hash计算（而列表不能哈希）

# 2.语法
使用大括号来表示，即{}。</br>
注意：单独的{}在python中的类型为dict，即字典。</br>
创建空集合的方式：set()
# 3.使用场景
```python
s = {}
print(type(s))  # <class 'dict'/>

# 创建空集合
s0 = set()
s = {1,2.0,"hehe",[]} # 报错，数组是可变数据，即不可hash
a = 2.0
s2 = {1,a,"hehe"} # 报错，数组是可变数据，即不可hash
print(type(s)) # <class 'set'>
```

# 4.常用操作
add： 添加元素</br>
pop： 弹出最后一个元素</br>
remove： 删除指定的元素，无返回值</br>

# 5.注意
集合中修改操作，需要先删除，再添加</br>
查询操作，需要通过循环来实现

# 6.交集、并集、差集
intersection: 取交集, 也可以通过 & 。</br>
difference: 取差集，也可以通过 - 。</br>
union: 取并集，也可以通过 | 。</br>
## 代码
```python
ss1 = {"张三","赵四","刘能"}
ss2 = {"tommy","刘能"}
ret = ss1.difference(ss2) # 取差集，原集合不发生变化。{'赵四', '张三'}
print(ret)
print(ss1 - ss2)
ret = ss1.intersection(ss2) # 取交集，原集合不发生变化。{'刘能'}
print(ret)
print(ss1 & ss2)
ret = ss1.union(ss2)   # 取并集，原集合不发生变化。{'刘能', '张三', 'tommy', '赵四'}
print(ret)
print(ss1 | ss2)
```