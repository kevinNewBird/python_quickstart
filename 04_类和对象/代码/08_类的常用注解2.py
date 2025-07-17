class Cat:
    name = None

    @property
    def name_(self):
        return self.name

    @name_.setter
    def name_(self, name):
        self.name = name


cat = Cat()
cat.name_ = 'kitty'  # call setter
print(cat.name_)  # call getter
