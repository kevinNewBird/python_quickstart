class P1:
    producer = "P1"

    def call_by_5g(self):
        print("使用5g网络进行通话")


class P2:
    producer = "P2"


class Child1(P1, P2):
    pass


class Child2(P1, P2):
    # 复写父类的成员属性
    producer = "Child2"


class Child3(P1, P2):
    producer = P1.producer

    def call_by_5g(self):
        print("开启CPU单核模式，省电。。。")
        print(super().producer)  # P1
        # 两种方式，调用父类成员方法
        # 方法1:使用super()
        super().call_by_5g()
        # 方法2:使用类名
        P1.call_by_5g(self)
        print("关闭CPU单核模式")


child1 = Child1()
print(child1.producer)  # P1
child2 = Child2()
print(child2.producer)  # Child2
child3 = Child3()
print(child3.producer)  # P1
"""
开启CPU单核模式，省电。。。
P1
使用5g网络进行通话
使用5g网络进行通话
关闭CPU单核模式
"""
child3.call_by_5g()
