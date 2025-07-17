from random import Random
from random import Random as Random2

# choice随机选举序列中一个元素
print("=" * 40)
lst = ['a', 'b', 'c', 'd', 'e']
print("选举任一元素：", Random().choice(lst))
print("使用别名随机对象打印随机数：", Random2().randint(1,10000))