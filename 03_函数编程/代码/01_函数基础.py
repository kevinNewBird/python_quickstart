# 1.函数的形参
## 1.1.位置参数（也叫必需参数）
def printme0(msg):
    print(msg)


### 调用printme0
# printme0() # 必须传参，否则报错
printme0("位置参数")

## 1.2.关键字参数
printme0(msg="关键字参数1")


def printme1(who, msg):
    print(f"{who}：{msg}")


printme1(msg="关键字参数2", who="刘能")


## 1.3.默认参数
def printme2(name="赵四", age=18):
    print(f"{name},年龄为：{age}")


printme2()
printme2("大嘴")


## 1.4.动态参数（也叫不定长参数）
### 1.4.1.*args
def printinfo1(arg1, *vartuple):
    print("*args使用：")
    print(arg1)
    for var in vartuple:
        print(f"可变参：{var}")


printinfo1(10)
printinfo1(10, 20, 30)


### 1.4.2.**kwargs
def printinfo2(arg1, **vardict):
    print("**kwargs使用：")
    print(arg1)
    for key, val in vardict.items():
        print(f"{key} {val}")


printinfo2(2232, name="武大", age="20")


### 1.4.3.混合使用
def printinfo3(arg1, *args, **kwargs):
    pass


printinfo3(1)


def printinfo3(*args, arg1, **kwargs):
    print(f"必需参数:{arg1}")
    for val in args:
        print(f"可变位置参数：{val}")
    for key, val in kwargs.items():
        print(f"可变关键字参数：{key}--{val}")


printinfo3(kwargs={"a": 1, "b": 2}, args=(1, 3), arg1=2)
printinfo3(1, 2, name="大脚", args=1, arg1=2)

## 扩展--列表和字典的实参传递
def f1(*var_tuple):
    print(var_tuple)
def f2(**var_dict):
    print(var_dict)

lst = {"a",1,"b"}
dic = {"name":"二狗","age":"猪鼻"}
f1(*lst)  # ('a', 'b', 1)
f2(**dic) # {'name': '二狗', 'age': '猪鼻'}
# 4.函数的返回值
def func():
    return 1, 2, 3, ["a", "b"]


print("函数返回值：", func())
