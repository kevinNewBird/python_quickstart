def guanjia(game):
    # inner参数：args表示将接收到的参数处理为tuple， kwargs表示将处理的参数处理为字典
    def inner(*args, **kwargs):
        print("开挂")
        # 由于inner接收的参数被处理为了元组或者字典，所以传给具体的方法的时候，需要再次被打散。如下：
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


print("=" * 40)
print(play_dnf("大脚", "root@123"))
print("*" * 40)
params = ['大脚2', 'root@123']
# play_dnf实际接收到的是单个位置参数，所以需要把列表参数params打散传递。如下：
play_dnf(*params)
print("*" * 40)
play_lol("刘能", "root@1234", "盖伦")
print("*" * 40)
guanjia(lambda name: print("德玛西亚, ",name))('大头')
