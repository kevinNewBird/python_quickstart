# 获取全局信息
a = 10

print("f1方法声明前", globals())  # {..., 'a':10}


def f1():
    b = 20
    print("f1方法内部：", globals())  # {..., 'a':10,'f1':<function f1 at 0x0000026A0A133E20>}


# 保证方法内部的locals被执行
f1()
print("f1方法声明后", globals())  # {..., 'a':10,'f1':<function f1 at 0x0000026A0A133E20>}

print("f2方法声明前", locals())  # {..., 'a': 10}, 获取的是当前作用域的局部变量


def f2():
    b = 20
    print("f2方法内部：", locals())  # {'b': 20}


# 保证方法内部的locals被执行
f2()
print("f2方法声明后：", locals())  # {..., 'a': 10, 'f2': <function f2 at 0x0000010890B03E20>
