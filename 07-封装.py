class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000000

    def __say(self):
        print(f'{self.name}在说话')

    def get_money(self):
        return self.__money


class Son(Father):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

    def get_money(self):
        return super().get_money()


son = Son('张三', 18)
print(son.get_money())  # 1000000
