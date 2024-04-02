# 阶乘 1*2*3...n!
lst = list()


def fact(n):
    if n == 0:
        return 1
    lst.append(n)
    return n * fact(n - 1)


# reverse = lst.reverse()
ret_fact = fact(5)
lst.reverse()
lst = [f"{i}" for i in lst]
print("表达式:【{}】的计算结果为{}".format(" * ".join(lst), ret_fact))

# 1+2+3...+n
lst.clear()

def add(n):
    if n == 0:
        return 0
    lst.append(n)
    return n + add(n - 1)


ret_add = add(5)
lst.reverse()
lst = [f"{i}" for i in lst]
print("表达式:【{}】的计算结果为{}".format(" + ".join(lst), ret_add))
