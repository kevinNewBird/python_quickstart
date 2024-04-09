def func1(data: list) -> list:
    return data


def func2(data: list[int]) -> list[str]:
    return ["tommy", "kitty"]


def func3(name: str, age: int) -> bool:
    print(f"{name}:{age}")
    return True


f1 = func1([1, "a"])
f2 = func2([1, 5, 3])
f3 = func3("刘能", 19)
print(f3)
