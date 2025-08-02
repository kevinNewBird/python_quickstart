lst = [0]
ret = [lst]
print(";".join([";".join([str(item) for item in lst]) for lst in ret]))