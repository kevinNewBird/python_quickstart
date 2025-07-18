import re

print("=" * 20, "1.search", "=" * 20)
source = "expressE10E"
# 正则编译（规则） 或者直接使用search
# 注意： 使用pattern的好处是可以反复使用，提升执行效率
# pattern = re.compile(r"(express)([A-Za-z0-9]*)")
# result = pattern.search(source)

# r的含义： 保持原始风格。如果没有的r， 比如 r"C:\\windows" 就需要转换为 "C:\\\windows" 才能保证正确的识别
result = re.search(r"(express)([A-Za-z0-9]*)", source)
# expressE10E
print("group(0) result:", result.group(0))
# express
print("group(1) result:", result.group(1))
# E10E
print("group(2) result:", result.group(2))

print()
print()
print("=" * 20, "2.search vs match", "=" * 20)
source = "Python powerful"
print("match powerful result:", re.match(r"powerful", source))  # No Match
print("search powerful result:", re.search(r"powerful", source).group())  # Match

print("match Python result:", re.match(r"Python", source).group())  # Match
print("search Python result:", re.search(r"Python", source).group())  # Match

print()
print()
print("=" * 20, "3.findall vs finditer", "=" * 20)
source = "expression express powerful abcd expeceted\nline2 experence"
exp_pattern = re.compile(r"exp\w*")
findall_ret = exp_pattern.findall(source)
print("findall exp* result:", findall_ret)
print("finditer exp* result:")
# 左开右闭的区间范围
for m in exp_pattern.finditer(source):
    print("  ->", "start:", m.start(), ",", "end:", m.end(), ",", "resutl:", m.group())
