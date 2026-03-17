# __init__ 方法

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'{self.name}说：你好')

person = Person('张三', 18)
print(person.name) # 张三
print(person.age) # 18  
person.say() # 张三说：你好

# __str__ 方法
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'打印的是这个{self.name}'

car = Car('宝马', 1000000)
print(car)  # <__main__.Car object at 0x100abb590>

# __del__ 方法
class Dog:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'{self.name} 对象被删除了')
    
    def __str__(self):
        return f'打印的是这个{self.name}'

dog = Dog('旺财')
del dog