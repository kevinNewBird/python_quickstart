import my  # 导入同级目录的py文件
# import my2.my2 as my2 # 导入下级目录中的单个文件，语法：import 文件夹.py文件 as 别名
# from my2 import my2  # 导入下级目录中的单个文件，语法：from 文件夹 import py文件
# from my2.my2 import *  # 导入文件夹中py文件的所有的函数，语法：from 文件夹.py文件 import *
from my2.my2 import my2Func  # 导入文件夹中py文件的单个函数，语法：from 文件夹.py文件 import 函数


def __init__():
    print("Hi, python project!!!")
    # 调用其它py文件的方法
    my.myFunc()
    # my2.my2Func()
    my2Func()


if __name__ == '__main__':
    __init__()
