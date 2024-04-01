# 1.装饰器的雏形
def guanjia(game):
    def inner():
        print("开挂")
        game()
        print("关闭外挂")

    return inner

@guanjia
def play_dnf():
    print("你好啊，我叫赛利亚，今天又是美好的一天")

@guanjia
def play_lol():
    print("德玛西亚！！！！")


# 管家把游戏重新封装一遍，将原来的游戏替换了。
# 方法变量赋值的方式
# play_dnf = guanjia(play_dnf)
# play_lol = guanjia(play_lol)

# 通过注解实现和上述一样的方式，在play_dnf和play_lol上添加方法的注解，即@guanjia
# 见方法定义上

# 带有外挂的游戏实体方法
play_dnf()
play_lol()
