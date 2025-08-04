# %matploylib inline的作用将图放到表格里每个shell里查看， 而不是一个个单独点击打开查看
import matplotlib.pyplot as plt
import pandas as pd

# pd.set_option('display.mpl_style', 'default')
# plt.rcParams['figure.figsize'] = (15, 5)

# 读取csv文件
heros = pd.read_csv('./dc_heros.csv', encoding='utf8')
"""
    NAME    REAL NAME
0  Flash  Barry Allen
1   Atom  Ray, Palmer
"""
print(heros)
# 读取首行
"""
    NAME    REAL NAME
0  Flash  Barry Allen
"""
print(heros[:1])