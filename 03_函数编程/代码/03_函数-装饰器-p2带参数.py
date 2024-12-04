def guanjia(game):
    def inner(*args, **kwargs):
        print("开挂")
        game(*args, **kwargs)
        print("关闭外挂")

    return inner


@guanjia
def play_dnf(username, password):
    print("你好啊，我叫赛利亚，今天又是美好的一天", username, password)


@guanjia
def play_lol(username, password, hero):
    print("德玛西亚！！！！", username, password, hero)


play_dnf("大脚", "root@123")
print()
play_lol("刘能", "root@1234", "盖伦")
f = guanjia(play_lol)
f("刘能2", "admin@1234", "马儿扎哈")
