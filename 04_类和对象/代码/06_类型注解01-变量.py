# 1.基础数据类型注解
## 1.1.方法1，变量：类型
var_1: int = 10
var_2: float = 3.14
var_3: bool = True
var_4: str = "tommy"

## 1.2.方法2，# type：类型
var_11 = 20  # type:int
var_21 = 33.14  # type:float
var_31 = False  # type:bool
var_41 = "kitty"  # type:str


# 2.类对象类型注解
class Student:
    pass


## 2.1.方法1，变量：类型
stu: Student = Student()
## 2.2.方法2，# type：类型
stu2 = Student()  # type:Student

# 3.基础容器类型注解
## 3.1.方法1，变量：类型
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"itheima": 666}
## 3.2.方法2，# type：类型
my_list2 = [1, 2, 3]  # type:list
my_tuple2 = (1, 2, 3)  # type:tuple
my_set2 = {1, 2, 3}  # type:set
my_dict2 = {"itheima": 666}  # type:dict

# 4.容器类型详细注解
## 4.1.方法1，变量：类型
my_list1: list[int] = [1, 2, 3]
my_tuple1: tuple[int, str, int] = (1, "tommy", 3)
my_set1: set[int] = {1, 2, 3}
my_dict1: dict[str, int] = {"itheima": 666}

## 4.2.方法2，# type：类型
my_list12 = [1, 2, 3]  # type:list[int]
my_tuple12 = (1, 2, 3)  # type:tuple[int,int,int]
my_set12 = {1, 2, 3}  # type:set[int]
my_dict12 = {"itheima": 666}  # type:dict[str,int]


# 函数本质也是变量
def func():
    return "hello"


f1 = func()  # type:str
f2: str = func()
