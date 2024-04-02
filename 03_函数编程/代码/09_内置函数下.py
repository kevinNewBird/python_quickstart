# 1.zip内置函数
lst1 = ["狗熊", "盖伦", "议长"]
lst2 = [2011, 2034, 2026]
result = zip(lst1, lst2)
print(list(result))  # [('狗熊', 2011), ('盖伦', 2034), ('议长', 2026)]

set1 = {2, 3, 4, 5}
result2 = zip(lst1, set1)
print(list(result2))  # [('狗熊', 2), ('盖伦', 3), ('议长', 4)]

# 2.sorted内置函数
s_lst = [3, 2, 6, 4, 1, 5]
print(sorted(s_lst))  # [1, 2, 3, 4, 5, 6]
print(sorted(s_lst, reverse=True))  # [6, 5, 4, 3, 2, 1]

str_lst = ["a", "ab", "zcdee", "bcd", "bkdsxz"]
print(sorted(str_lst))  # ['a', 'ab', 'bcd', 'bkdsxz', 'zcdee']
print(sorted(str_lst, key=lambda x: len(x)))  # ['a', 'ab', 'bcd', 'zcdee', 'bkdsxz']


# 3.filter内置函数
## 定义一个函数，判断是否为偶数
def is_even(num):
    return num % 2 == 0


num_list = [1, 3, 4, 2, 8, 6, 4, 5, 7]
nums_iter = filter(is_even, num_list)  # [4, 2, 8, 6, 4]
print(list(nums_iter))
nums_iter2 = filter(lambda num: num % 2 == 0, num_list)  # [4, 2, 8, 6, 4]
print(list(nums_iter2))

# 4.map内置函数
numbers = [1, 2, 3, 4, 5]
numbers2 = [2, 4, 6, 8, 10]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]
squared2 = map(lambda x, y: x * y, numbers, numbers2)
print(list(squared2))  # [2, 8, 18, 32, 50]
