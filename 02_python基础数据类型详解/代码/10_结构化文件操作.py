import csv

print("=" * 150)
CSV_TIP = 'CSV File Test: reader & writer'
print(CSV_TIP.center(150, '*'))
# 1. csv文件写入操作: reader和writer方法
dc_heros = [
    ['Flash', 'Barry Allen'],
    ['Atom', 'Ray, Palmer'],
    ['Kitty', 'Jay Pomelo']
]

"""
Flash,Barry Allen
Atom,"Ray, Palmer"
"""
with open('../../09_数据库/代码/dc_heros.csv', 'w+') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(dc_heros)

# 1.读取为列表
with open('../../09_数据库/代码/dc_heros.csv', 'r') as fin:
    csvin = csv.reader(fin)
    hero_docs_in = [row for row in csvin]

print('Read dc_heros.csv to list, the content is : ', hero_docs_in)


# 2.读取为dict
def read_csv_to_dict(filename):
    with open(filename, 'r') as fin:
        # 会把第一行数据作为其它行的key键（即转换出来的dictionary的key）
        # [{'Flash': 'Atom', 'Barry Allen': 'Ray, Palmer'}]
        csvdictin = csv.DictReader(fin)
        # 通过fieldnames执行转换的每一行的key键
        # [{'NAME': 'Flash', 'REAL NAME': 'Barry Allen'}, {'NAME': 'Atom', 'REAL NAME': 'Ray, Palmer'}]
        # csvdictin = csv.DictReader(fin, fieldnames=['NAME', 'REAL NAME'])
        hero_docs_dict = [row for row in csvdictin]
    return hero_docs_dict


print('Read dc_heros.csv to dictionary, the content is : ', read_csv_to_dict('../../09_数据库/代码/dc_heros.csv'), '\n', '\n')
print("=" * 150)

# 2.csv文件写入操作: DictReader和DictWriter方法
CSV_TIP = 'CSV File Test: DictReader & DictWriter'
print(CSV_TIP.center(150, '*'))
hero_dict_docs = [
    {'NAME': 'Flash', 'REAL NAME': 'Barry Allen'},
    {'NAME': 'Atom', 'REAL NAME': 'Ray, Palmer'}
]
with open('../../09_数据库/代码/dc_heros.csv', 'w+') as fout:
    cout = csv.DictWriter(fout, hero_dict_docs[0].keys())
    cout.writeheader()
    cout.writerows(hero_dict_docs)

print('Read dc_heros.csv to dictionary, the content is : ', read_csv_to_dict('../../09_数据库/代码/dc_heros.csv'), '\n', '\n')

import json

JSON_TIP = 'JSON File Test: parse'
print(JSON_TIP.center(150, '*'))
temperature = {
    'avg': 20.0,
    'daily': [
        {'highest': 21.0, 'lowest': 19.0},
        {'highest': 22.0, 'lowest': 18.0},
        {'highest': 23.0, 'lowest': 17.0}
    ]
}
# dumps: 输入源--Python对象。输出--转换json对象为一个json字符串
# dump: 输入源--Python对象+文件。输出--直接写入文件
temperature_json = json.dumps(temperature)  # type:str
print("JSON Temperature Type: ", type(temperature_json), "\nJSON String Content:", temperature_json)

# loads: 输入源--字符串。输出--处理API响应或内存中的JSON数据
# load: 输入源--文件对象。输出--读取本地JSON文件
temperature_obj = json.loads(temperature_json)  # type:dict
print("JSON Temperature Type: ", type(temperature_obj), "\nJSON Object Content:", temperature_obj)


# class对象转换为json串的两种方式：
# 1.使用class对象的内置__dict__属性
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'name = {}'.format(self.name)


print("Person Object convert to JSON String: ", json.dumps(Person('a').__dict__))
# 2.引入pickle处理
import pickle

person_bin = pickle.dumps(Person('b'))
print("Person Object convert to JSON Binary String: ", person_bin)
person_load = pickle.loads(person_bin)
print("JSON Binary String convert to Person Object: ", person_load)
