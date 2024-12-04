# 1.函数的作用域
a = 10  # 全局变量


def func():  # 全局函数
    b = 20  # 局部变量
    func3()


def func3():
    print("func3")


func()  # 调用


# 2.函数的嵌套
def f1():
    def f2():  # 局部变量。仅支持在当前作用域中调用
        pass

    f2()


# 调用报错。嵌套函数仅支持在作用域内调用。
# f2() # NameError: name 'f2' is not defined. Did you mean: 'f1'?

# 3.闭包函数
def ff1():
    def inner():
        print("inner")

    return inner


inner = ff1()  # 将一个函数当成变量进行赋值
print(inner)  # 打印函数的类型：<function ff1.<locals>.inner at 0x000001BA7931ECB0>
inner()  # 闭包函数的调用

num = 10


def fff1():
    num = 20  # 创建一个局部变量，并没有去改变全局变量中的num（在java中是可行的）


fff1()
print("方法内部修改变量：", num)  # 方法内部修改变量： 10


# 4.内部函数改变全局变量或内部函数改变外部函数的变量
# 4.1.在局部引入全局变量num, 并修改
def fff2():
    global num
    num = 30


fff2()
print(f"方法内部global关键字引入全局遍历后，修改变量：{num}")  # 方法内部global关键字引入全局遍历后，修改变量： 30


def fff3():
    a = 10

    def f1():
        a = 20

    f1()
    print(a)  # 10


fff3()


# 4.2.内部函数改变外部函数变量（不含全局变量）
def fff4():
    aa = 10

    def f1():
        nonlocal aa  # 向外找一层，看有没有该变量，如果有就引入；如果没有，继续向外找一层，直到全局（不包括）
        aa = 20

    f1()
    print(f"内部函数改变外部函数fff4的函数变量aa：{aa}")  # 20


fff4()


# num2 = 30
# def fff5():
#     def f1():
#         # 报错no binding for nonlocal 'num2' found。
#         # nonlocal关键字查找范围 < 全局，即不能超出最外层方法
#         nonlocal num2 # 向外找一层，看有没有该变量，如果有就引入；如果没有，继续向外找一层，直到全局（不包括）
#         num2 = 40
#     f1()
#     print(num2)
#
# fff5()

# 3.闭包函数
def foo():
    num = 1

    def add(n):
        nonlocal num
        num += n
        return num

    return add


f = foo()  # add函数名的变量
print(f(1), f(2))  # 2 4
