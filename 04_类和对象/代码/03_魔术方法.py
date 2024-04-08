class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"Student:[name={self.__name}, age={self.__age}]"

    def __lt__(self, other):
        return self.__age < other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age


s1 = Student("tommy", 16)
s2 = Student("kitty", 17)
print(s1, s2)  # Student:[name=tommy, age=16] Student:[name=kitty, age=17]
print(s1 < s2)  # True
print(s1 <= s2)  # True
print(s1 == s2)  # False
