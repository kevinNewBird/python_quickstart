def guanjia(game):
    def inner(*args, **kwargs):
        print("开挂")
        ret = game(*args, **kwargs)
        print("关闭外挂")
        return ret

    return inner


@guanjia
def play_dnf(username, password):
    print("你好啊，我叫赛利亚，今天又是美好的一天", username, password)
    return "神器-寒霜剑"


@guanjia
def play_lol(username, password, hero):
    print("德玛西亚！！！！", username, password, hero)


print(play_dnf("大脚", "root@123"))
print()
print(play_lol("刘能", "root@1234", "盖伦"))
