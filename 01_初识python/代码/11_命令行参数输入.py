import sys

# 1.可通过python  name.py hello world传入命令行参数（空格分隔）
# 2.也可以通过在IDE中配置script parameters进行指定（空格分隔）
# 注意： 第一个参数为模块名。即Command-Line Arguments:  ['11_命令行参数输入.py', 'hello', 'world']
print("Command-Line Arguments: ", sys.argv)