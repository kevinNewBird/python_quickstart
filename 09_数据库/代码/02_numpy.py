import numpy as np

"""
numpy是Python科学计算的基础库，专注于高效的多维数组运算和数值计算
"""


def print_deli(info: str, fillchar="=", length: int = None):
    length = length if length and length > 0 else 120
    fillchar = fillchar if fillchar else "="
    if len(info) >= length:
        print(info)
    else:
        left = int((length - len(info)) / 2)
        right = length - left - len(info)
        print("{} {} {}".format(fillchar * left, info, fillchar * right))


print_deli("转换容器为numpy array")
lst1 = [1, 2, 3]
array = np.array(lst1)
# 转换后类型： int64 结果： [1 2 3]
print("转换后类型：", array.dtype, "结果：", array)

lst2 = [1.1, 2.3, 4]
array = np.array(lst2)
# 转换后类型： float64 ，结果： [1.1 2.3 4. ]
print("转换后类型：", array.dtype, "，结果：", array)

# 虚数
lst3 = [[1, 2], [3, 4]]
array = np.array(lst3, dtype=complex)
# 转换后类型： complex128 ，结果：  [[1.+0.j 2.+0.j]
#  [3.+0.j 4.+0.j]]
print("转换后类型：", array.dtype, "，结果：", array)
# (2, 2)表示两行两列
print("纬度shape：", array.shape)

print_deli("numpy快速初始化一个纬度的array")
array = np.zeros([2, 3])
print("初始化一个两行三列的array(所有值为0): ", array, "类型为：", type(array))
array = np.ones([2, 3])
print("初始化一个两行三列的array(所有值为1): ", array, "类型为：", type(array))
array = np.empty([2, 2])
print("初始化一个两行两列的array(所有值为0, == zeros): ", array, "类型为：", type(array))
array = np.eye(4)
"""
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]] 
"""
print("初始化一个四行四列的array的矩阵(斜角为1): ", array, "类型为：", type(array))

# [2 4 6 8]
array = np.arange(2, 10, 2)
print("初始化一个[2,10)且步进为2的array: ", array, "类型为：", type(array))
# 等分范围[2,10]为2份，并获取两个数。注意[2,10]有9个数
array = np.linspace(2, 10, 2)
# [ 2. 10.]
print("初始化一个[2,10]并等分获取2个数的array: ", array, "类型为：", type(array))
array = np.linspace(2, 10, 9)
# [ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
print("初始化一个[2,10)并等分获取9个数的array: ", array, "类型为：", type(array))

print_deli("numpy的计算：加减乘除")
"""
numpy的加减乘除, 对于其本身的操作是对于其每一个元素而言的
如果是需要做矩阵的运算是需要使用特定的方法去处理， 如dot和add
"""
# 对numpy array本身的加减乘除
array = np.array([[1, 2, 3], [4, 5, 6]])
"""
[[0 1 2]
 [3 4 5]]
 """
print("加法：", array - 1)
"""
[[ 1  4  9]
 [16 25 36]]
 """
print("乘法 a*a (其实是a的每个元素的平方)：", array * array)
"""
[[ 1  4  9]
 [16 25 36]]
 """
print("乘法 a*a (其实是a的每个元素的平方)：", array ** 2)
print("除法：", 1 / array)

A = np.array([[1, 3], [0, 1]])
B = np.array([[2, 2], [3, 4]])
"""
结果如下：
 [[2 6]
 [0 4]]
 
 注意：其仍是相同位置元素的普通运算，而非矩阵运算
 """
print("两个不同array运算：", A * B)

# 矩阵运算
"""
[[11 14]
 [ 3  4]]
 """
print("矩阵运算(点乘)：", A.dot(B))
"""
[[11 14]
 [ 3  4]]
 """
print("矩阵运算(点乘)：", np.dot(A, B))
"""
[[3 5]
 [3 5]]
 """
print("矩阵运算(点加)：", np.add(A, B))
# 矩阵行和列进行转变
"""
[[1 0]
 [3 1]]
 """
print("矩阵行和列进行转变:", A.T)

# 生成一个纬度的随机数
rlst = np.random.random([2, 4])  # 默认生成[0.0, 1.0)区间范围的随机数
"""
[[0.26712957 0.43797263 0.4235156  0.88817986]
 [0.09181687 0.90797681 0.29231889 0.77545342]]
 """
print("生成[0,1)之间的2行4列的随机数array:", rlst)
# 0.9079768068182205
print("找出array中的最大值: ", rlst.max())
# 4.084363647990193
print("求array的和: ", rlst.sum())
# 将[0,24)范围内的数据处理成6行4列
b = np.arange(24).reshape(6, 4)
"""
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]
 """
print("将[0,24)范围内的数据处理成6行4列:\n", b)
# 计算每一列的值的和
"""
[60 66 72 78]
"""
print("计算每一列的值的和:\n", b.sum(axis=0))
# 计算每一行的值的和
"""
 [ 6 22 38 54 70 86]
"""
print("计算每一行的值的和:\n", b.sum(axis=1))
# 计算每一行的累加值
"""
以第一行[0 1 2 3]为例， 0， 0+1， 0+1+2， 0+1+2+3 
[[ 0  1  3  6]
 [ 4  9 15 22]
 [ 8 17 27 38]
 [12 25 39 54]
 [16 33 51 70]
 [20 41 63 86]]
"""
print("计算每一行的累加值:\n", b.cumsum(axis=1))


def f(x, y):
    return 4 * x + y


# x表示行， y表示列。行和列均是从0开始
"""
[[0 1]
 [4 5]
 [8 9]]
 """
l = np.fromfunction(f, (3, 2), dtype=int)
print("使用函数f生成一个3行2列的array：", l)

# 获取元素，使用slice（即切片）
print_deli("切片/修改array元素")
# [ 0  1  4  9 16 25 36 49 64 81]
b = np.arange(10, dtype=int) ** 2
# 切片一维数组
# [ 4  9 16 25 36 49 64 81]
print("操作一维数组:", b[2:])
# 修改一维数组的范围内的值
b[0:3] = 100
# [100 100 100   9  16  25  36  49  64  81]
print("修改一维数组的范围内的值:", b)
# 浅拷贝
b_new = b[0:5]
b_new[0] = 200
# [200 100 100   9  16  25  36  49  64  81]
print("修改一维数组的某个值(浅拷贝):", b)
# 深拷贝
b_deep = b[0:5].copy()
b_deep[0] = 300
# [200 100 100   9  16  25  36  49  64  81]
print("修改一维数组的某个值(深拷贝):", b)

# 操作多维数组
array = np.array([[1, 2, 3], [4, 5, 6]])
# 获取某一行元素， [1 2 3]
print("获取多维数组的第一行数据:", array[0])
# 获取某一列元素， [1 4]
print("获取多维数组的第一列数据:", array[:, 0])
# 1
print("获取多维数组的第一行第一列数据:", array[0][0])
# 切片
# [[1 2 3]]
array_slice = array[0:1]
print("切片多维数组的第一行数据:", array_slice)
array_slice = array[:, 0:2]
"""
 [[1 2]
 [4 5]]
"""
print("切片多维数组的第0-2列数据:", array_slice)
print()
# 修改某一行数组
array[0] = 100
"""
[[100 100 100]
 [  4   5   6]]
 """
print("修改多维数组的第一行数据:", array)
