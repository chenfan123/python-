# 类方法
class Dog:
    @classmethod
    def eat(cls):
        print(f'狗在吃东西{cls}')


Dog.eat()
dog = Dog()
dog.eat()
