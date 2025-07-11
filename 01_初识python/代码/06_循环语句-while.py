# 循环计数
i = 1
sum = 0
while i <= 100:
    print(i)
    i += 1
    sum += i
print("总和：" + str(sum))

# while+else
print("==================")
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("no break")
print("==================")
i = 1
while i < 5:
    print(i)
    i += 1
    if i == 2:
        break
else:
    print("no break")
