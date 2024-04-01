gen = (i ** 2 for i in range(5))
print(gen)  # <generator object <genexpr> at 0x100735a40>
# print(tuple(gen))  # (0, 1, 4, 9, 16)

for item in gen:
    print(item)