class Student:

    def __init__(self, name=None, age=None):
        self.name = name  # 定义全局成员变量
        self.__age = age  # 定义私有成员变量

    def __str__(self):
        print(f"Student:[name={self.name}, age={self.__age}]")


stu: Student = Student()
stu.__str__()  # Student:[name=None, age=None]

stu2: Student = Student("tommy", 17)
print(stu2.name)  # 打印公有成员变量
stu2.__str__()  # Student:[name=tommy, age=17]
