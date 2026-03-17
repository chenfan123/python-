# object是所有类的父类
class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def teach(self):
        print(f'{self.name}在上课')

# 继承
class MyTeacher(Teacher):
    pass

my_teacher = MyTeacher('张三', 18)
my_teacher.teach()  # 张三在上课

# 多继承
class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f'{self.name}在玩')

    def say(self):
        print(f'{self.name}在说话1')

class Mother(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cook(self):
        print(f'{self.name}在做饭')

    def say(self):
        print(f'{self.name}在说话2')

class Son(Father, Mother):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.name = name
        self.age = age

son = Son('张三', 18)
son.play() # 张三在玩
son.cook()  # 张三在做饭
son.say()  # 张三在说话1
print(Son.__mro__) # 查看调用顺序:Son->Father->Mother->object