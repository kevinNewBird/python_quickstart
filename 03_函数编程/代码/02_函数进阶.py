a = 10        # 全局变量

def func():   # 全局函数
    b = 20    # 局部变量
    func3()

def func3():
    print("func3")

func()        # 调用