import random


class RandomHelper:

    def random_number(cls, length=5):
        return '_' + str(random.randint(10 ** (length-1), 10 ** length))


objTree=['(ss)','(bbb{{random}})']

def xx(obj: list):
    result = list()
    for item in obj:
        if not item:
            continue
        result.append(item.replace("{{random}}","101"))
    return result

oo=xx(objTree)
print(1)

bb = [ item.replace("{{random}}","201") for item in objTree if item]
print(2)