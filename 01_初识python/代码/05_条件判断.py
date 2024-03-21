money = 500

# 注意： py中通过缩进来区分代码块
# 格式1
if money > 300:
    print("大于300元")
    print("条件成立逻辑执行完成")

print("条件不成立执行的逻辑")

print("------------------------------------")

# 格式2/3/4
money = input("请输入你兜里的钱：")
money = int(money)
if money > 500:
    print("找快乐")
elif money > 300:
    print("小幸运")
else:
    print("认真学习")
