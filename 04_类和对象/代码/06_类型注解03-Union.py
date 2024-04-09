from typing import Union

# 1.变量
## 1.1.方法1，变量：类型
my_list1: list[Union[int, str]] = [1, "a", 3]
my_tuple1: tuple[int, str, Union[list, int]] = (1, "tommy", [1, 2, 3])
my_set1: set[Union[int, str]] = {1, 2, 3}
my_dict1: dict[str, Union[int, str]] = {"age": 666}

## 1.2.方法2，# type：类型
my_list12 = [1, 2, 3]  # type:list[Union[int, str]]
my_tuple12 = (1, 2, 3)  # type:tuple[int,int,Union[list, int]]
my_set12 = {1, "a", 3}  # type:set[Union[int, str]]
my_dict12 = {"name": "tommy", "age": 17}  # type:dict[str,Union[int,str]]

# var_1: int = 10
var_1: Union[int, str] = True
print(var_1)


# 2.方法
def func1(data: list[Union[int, str]]) -> list[Union[int, str]]:
    return [True]


print(type(func1(["a", 1, [11, 222]])))


def func2(base_data: Union[int, str]) -> Union[int, str]:
    print(type(base_data))
    return "hello"


print(type(func2("1")))
