class Student:
    # 1.定义成员变量
    name = None  # 可省略。等价于调用的方法使用了self.name= name，注意如果是构造方法里定义，无需使用前成员前，调用相应的定义变量的方法。
    age = None

    # 2.定义私有成员变量
    __sex = None # # 可省略。等价于调用的方法使用了self.__sex= sex

    # 1.定义成员方法
    def initialize(self, name, age, sex):
        self.__initialize(name, age)
        self.__sex = sex

    # 2.定义私有成员方法
    def __initialize(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Student:[name={self.name}, age={self.age}, sex={self.__sex}]")


stu: Student = Student()
stu.name = "tommy"
stu.age = 18
stu.show()  # Student:[name=tommy, age=18, sex=None]

stu.initialize("kitty", 16, "male")  # Student:[name=tommy, age=18, sex=None]
stu.show()
