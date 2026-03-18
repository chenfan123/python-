class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'{self.name}在说话')


class Dog(Animal):
    def __init__(self, name, age, types):
        super().__init__(name, age)
        self.types = types

    def say(self):
        print(f'{self.name}在说话')


class Husky(Dog):
    def __init__(self, name, age, types, color):
        super().__init__(name, age, types)
        self.color = color

    def say(self):
        print(f'{self.name}在说话，我的颜色是{self.color},我的品种是{self.types},我的年龄是{self.age}')


husky = Husky('旺财', 10, '哈士奇', '白色')
husky.say()
