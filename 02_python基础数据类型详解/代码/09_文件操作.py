# 1.文件操作
## 1.1.基础使用
print("基础使用:")
f = open("../资源/孙悟空.txt", mode="r", encoding='utf-8', errors='ignore')
# print("读取所有行：\n" + f.read())
# print("读取一行：" + f.readline().strip()) # 读取一行
# print("读取所有行的列表：{}".format(f.readlines()))  # 读取一行
# 循环遍历
for line in f:
    print(line.strip())
# 关闭文件通道
f.close()
print()

## 1.2.进阶使用with，将资源的释放交由py处理
print("进阶使用（with）:")
with open("../资源/孙悟空.txt", mode="r", encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        print(line.strip())

print()
## 1.3.进阶使用finally，将资源的释放交由py处理
f2 = None
try:
    f2 = open("../资源/孙悟空.txt", mode="r", encoding='utf-8', errors='ignore')
    print("打开文件成功...")
    content = f2.read()  # 可能引发OSError异常
    print(content)
except FileNotFoundError | OSError as e:
    print("文件不存在！")
finally:
    if f2 is not None:
        f2.close()
        print("关闭文件成功")

