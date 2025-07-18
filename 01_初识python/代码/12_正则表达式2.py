import re

print("=" * 20, "1.branch condition -- ｜", "=" * 20)
source = "expression express express powerful abcd expeceted\nline2 experence"
exp_pattern = re.compile(r"\bexpress\b|\babcd\b")
findall_ret = exp_pattern.findall(source)
print("findall | result:", findall_ret)

print("=" * 20, "2.后向引用", "=" * 20)
source = "kitty kitty go go, so cute"
# 第一个\b, 表示匹配任意\w开头的字符串
# 第二个\b, 表示匹配任意\s（空格）开始的字符串
# \1的含义： 重复前面的\b(\w+)\b匹配再写一次
# 第三个\b, 表示结束匹配
# 展开来看就是：\b(\w+)\b\s+\b(\w+)\b\b，但是两者是有差别的。前者表示是重复，也就说是匹配后的结果写到\1位置进行匹配
b_pattern = re.compile(r"\b(\w+)(?#匹配一个或多个字母等)\b\s+\1\b")  # \1第一匹配
b_pattern2 = re.compile(r"\b(?P<exp>\w+)(?#匹配一个或多个字母等)\b\s+(?P=exp)\b")  # 和上面是等价的
# 注意使用后向引用，建议不要使用findall， 可能会和期待结果有差异（会自行排除重复的匹配，比如两个go，只会保留一个）
# ['kitty', 'go']
print("find \\b result: ", b_pattern.findall(source))
for m in b_pattern.finditer(source):
    # 00-11: kitty kitty
    # 12-17: go go
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group()))

# ['kitty kitty', 'go go']
lst = [m.group() for m in b_pattern.finditer(source)]
lst2 = [m.group() for m in b_pattern2.finditer(source)]
print("find \\b result: ", lst)
print("find \\b result: ", lst2)


print("=" * 20, "3.后向引用进阶使用--捕获", "=" * 20)
source = "expression express express powerful abcd expeceted"
exp_pattern = re.compile(r"\b(?P<pw>\w+)\b\s+(?P=pw)\b")
lst_all = exp_pattern.findall(source)
lst_iter = [m.group() for m in exp_pattern.finditer(source)]
# ['express']
print("find \\b result: ", lst_all)
# ['express express']
print("find \\b result: ", lst_iter)

print("=" * 20, "4.后向引用进阶使用--零宽断言", "=" * 20)
source = "expression express express powerful abcdion expeceted"
exp_pattern = re.compile(r"\b\w+(?=ion\b)") # 匹配以ion结尾的单词的前面部分（即除了ion部分）
lst_all = exp_pattern.findall(source)
lst_iter = [m.group() for m in exp_pattern.finditer(source)]
# ['express', 'abcd']
print("find \\b before result: ", lst_all)
# ['express', 'abcd']
print("find \\b before result: ", lst_iter)

# exp_pattern = re.compile(r"(?<=exp)\w+")
# lst_all = exp_pattern.findall(source)
# lst_iter = [m.group() for m in exp_pattern.finditer(source)]
# print("find \\b after result: ", lst_all)
# print("find \\b after result: ", lst_iter)

exp_pattern = re.compile(r"(?<=\bexp)\w+\b") # 匹配以exp开头的单词的后面部分（除了exp以外的部分）
lst_all = exp_pattern.findall(source)
lst_iter = [m.group() for m in exp_pattern.finditer(source)]
# ['ression', 'ress', 'ress', 'eceted']
print("find \\b after result: ", lst_all)
# # ['ression', 'ress', 'ress', 'eceted']
print("find \\b after result: ", lst_iter)

print("=" * 20, "5.正则拆分", "=" * 20)
source = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Burger: 925.541.7635 436 Finley Avenue"""
entries = re.split("\n+", source)
result = [re.split(":? ", entry, maxsplit=3) for entry in entries]
print(result)

# 替换是 sub
print("=" * 20, "6.正则替换", "=" * 20)
source = "AAREPLACEBB"
result = re.sub("replace", " 1111 ", source, flags=re.IGNORECASE)
print(result)