class Student:

    def __init__(self, name=None, age=None):
        self.name = name
        self.__age = age

    def __str__(self):
        print(f"Student:[name={self.name}, age={self.__age}]")


stu: Student = Student()
stu.__str__()  # Student:[name=None, age=None]

stu2: Student = Student("tommy", 17)
stu2.__str__()  # Student:[name=tommy, age=17]
