# 多态
# 同一个函数接受不同的参数，有不同的效果
class Animal:  # 抽像类（也叫接口）

    def speak(self):  # 抽象方法
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪')


class Cat(Animal):
    def speak(self):
        print('喵喵喵')


# 定义函数，接受不同的动物对象，调用speak方法
def make_sound(animal: Animal):
    animal.speak()


make_sound(Dog())
