class Student:
    def __init__(self, name, age):
        self.__name = name  # 私有成员变量
        self.__age = age  # 私有成员变量

    # 私有成员方法
    def __show(self):
        print(f"{self.__name}, {self.__age}")
