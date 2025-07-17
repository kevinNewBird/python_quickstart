class Dog:

    def __init__(self, breed, age):
        self._breed = breed
        self._age = age

    @classmethod
    def format_json(cls, data):
        return cls(data['breed'], data['age'])

    @staticmethod
    def print__(dog):
        return 'breed = {}, age = {}'.format(dog.breed, dog.age)

    @property  # 等价于getBreed
    def breed(self):
        return self._breed

    @breed.setter  # 等价于 setBreed
    def breed(self, breed):
        self._breed = breed

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return 'breed = {}, age = {}'.format(self._breed, self._age)


dogObj = Dog.format_json({'breed': '柯基', 'age': 2})
print("classmethod: ", dogObj)
print("=" * 40)
dogObj = Dog('unknown', -1)
dogObj.age = 10  # 自动调用setter
dogObj.breed = '雪纳瑞' # 自动调用setter
print("property+setter: ", dogObj)
dogObj = Dog('test1',3)
print(Dog.print__(dogObj))

print(dogObj.breed)
