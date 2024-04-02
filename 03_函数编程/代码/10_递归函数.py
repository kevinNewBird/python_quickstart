# 阶乘 1*2*3...n!
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(5))


# 1+2+3...+n
def add(n):
    if n == 0:
        return 0
    return n + add(n - 1)


print(add(5))
