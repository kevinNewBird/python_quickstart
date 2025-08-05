import pandas as pd
import matplotlib.pyplot as plt

# 读取csv文件
# heros = pd.read_csv('./dc_heros.csv', encoding='utf8')
# parse_dates表示对日期列DATE做解析（默认处理为年月日格式，即yyyy-mm-dd）， dayfirst表示csv文件中日期列DATE的日dd在前面， index_col表示将DATE作为标识列（不指定默认是以0..n数字标识）
heros = pd.read_csv("./dc_heros.csv", encoding='utf8', sep=','
                    , parse_dates=['DATE'], dayfirst=True, index_col='DATE')
"""
             NAME    REAL NAME  AGE
DATE                               
2022-02-01  Flash  Barry Allen   10
2023-03-30   Atom  Ray, Palmer   29
"""
print(heros)

"""
              NAME    REAL NAME  AGE
DATE                               
2022-02-01  Flash  Barry Allen   10
"""
# 读取前几行
print("读取前几行：\n", heros[:1])

"""
 DATE
2022-02-01    Flash
2023-03-30     Atom
Name: NAME, dtype: object
"""
# 选取指定列(不能使用这种方式选择标识列)
print("选取指定列NAME:\n", heros['NAME'])
"""
              NAME  AGE
DATE                  
2022-02-01  Flash   10
2023-03-30   Atom   29
"""
# 选取多个指定列(两层列表)
print("选取多个指定列:\n", heros[['NAME', 'AGE']])
#  (2, 3)
print("多少行多少列:\n", heros.shape)
"""
              NAME    REAL NAME  AGE
DATE                               
2022-02-01  Flash  Barry Allen   10
"""
print("选取前多少行:\n", heros.head(1))
"""
             NAME    REAL NAME  AGE
DATE                              
2023-03-30  Atom  Ray, Palmer   29
"""
print("选取后多少行:\n", heros.tail(1))
"""
             NAME    REAL NAME  AGE
DATE                              
2023-03-30  Atom  Ray, Palmer   29
"""
# 条件选择行(年龄大于等于18)
print("条件选择列:\n", heros[heros['AGE'] >= 18])
"""
             NAME  AGE
DATE                 
2023-03-30  Atom   29
"""
# 条件选择行并只选择其中某些列(年龄大于等于18)
print("条件选择行并只选择其中某些列:\n", heros[heros['AGE'] >= 18][['NAME', 'AGE']][:2])
"""
 NAME
Flash    1
Atom     1
Name: count, dtype: int64
"""
# 统计重名数量
counts = heros['NAME'].value_counts()
print("统计同名数量：\n", counts)
"""
 NAME         object
REAL NAME    object
AGE           int64
dtype: object 
"""
print("列数据类型：\n", heros.dtypes)
heros['AGE'] = heros['AGE'].astype(str)
# 列数据类型：object
print("列数据类型：", heros['AGE'].dtype)

# 转换日期
# pd.to_datetime(heros['atime'],unit='s')

heros['AGE'] = heros['AGE'].astype(int)

# 画图(年龄列)
# 绘制前两行的柱状图（bar标识柱状图）
counts[:2].plot(kind = 'bar')
# plt.plot(heros['AGE'])
# heros['AGE'].plot()
# figsize指定图表的大小， 15是高度，10是宽度
heros.plot(figsize=(15, 10))
# 多个绘图，plt.show()只需要调用一次（比如上面的heros['AGE'].plot()，无需对齐单独调用show）。有多少个plot()，就会有多少个绘图窗口
plt.show()
