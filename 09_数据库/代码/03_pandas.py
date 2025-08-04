import pandas as pd
# matplotlib是pandas自带的做可视化的包。 当然还有第三方的seaborn
import matplotlib.pyplot as plt
# DataFrame类型(数据表格) 最常用的类型
"""
   C1  C2  C3
A   1   2   3
B   4   5   6
"""
# index表示行名， columns表示列名
df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], index=['A', 'B'], columns=['C1', 'C2', 'C3'])
print("表格展示：\n", df1)
"""
 [[1 2 3]
 [4 5 6]]
"""
print("表格数据：\n", df1.values)
#  Index(['C1', 'C2', 'C3'], dtype='object')
print("表格列名：\n", df1.columns)
"""
     A  B
C1  1  4
C2  2  5
C3  3  6
"""
print("表格行和列进行转换：\n", df1.T)
# 表格的纬度： (2, 3)即2行3列, 元素总个数：6
print("表格的纬度：", df1.shape, "\b即{}行{}列, 元素总个数：{}".format(df1.shape[0], df1.shape[1], df1.size))

# 从头开始选举多少行
"""
    C1  C2  C3
A   1   2   3
"""
print("从头开始选举1行: ", df1.head(1))
# 从尾部开始选举多少行
"""
    C1  C2  C3
B   4   5   6
"""
print("从末尾开始选举1行: ", df1.tail(1))
# 自动计算所有数值信息（比如数量/平均值/方差/最大/最小等）
"""
             C1       C2       C3
count  2.00000  2.00000  2.00000
mean   2.50000  3.50000  4.50000
std    2.12132  2.12132  2.12132
min    1.00000  2.00000  3.00000
25%    1.75000  2.75000  3.75000
50%    2.50000  3.50000  4.50000
75%    3.25000  4.25000  5.25000
max    4.00000  5.00000  6.00000
"""
print("自动计算所有数值信息:\n", df1.describe())

# 获取某一行标注的值
"""
获取某一行标注的值: 
 C1    4
C2    5
C3    6
Name: B, dtype: int64
"""
print("获取B标注的行的值: \n", df1.loc['B'])
#  5
print("获取B标注的行的C2标注的列的值: \n", df1.loc['B', 'C2'])
