def add(a, b):
    """计算两数之和。

    Args:
        a (int): 第一个加数
        b (int): 第二个加数

    Returns:
        int: 两数之和

    Example:
        >>> add(2, 3)
        5
    """
    return a + b


# 通过 func.__doc__ 可访问该字符串
print(add.__doc__)