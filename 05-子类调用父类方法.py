# 子类调用父类方法
# 子类中仍想要保留父类的行为，则需要在子类中调用父类方法，可以直接使用父类名来调用，使用的方法：父类名.父类方法名(self)
class Mother(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cook(self):
        print(f'{self.name}在做饭')

class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kongfu = '武功'

    def play(self):
        print(f'{self.name}在玩')

    def say(self):
        print(f'{self.name}在说话，我会{self.kongfu}')

class Son(Father, Mother):
    def __init__(self, name, age):        
        self.name = name
        self.age = age
        self.kongfu = '剑法'
    def play(self):
        print(f'{self.name}在玩')
        
    # 调用父类的功能 - 通过父类名来调用
    def useFatherMethod(self):
        Father.__init__(self, self.name, self.age)
        Father.say(self) 

    
    # 调用父类的功能 - 通过super()来调用
    # def useFatherMethod2(self):
    #     super().say()

son = Son('张三', 18)
son.play()  # 张三在玩
son.useFatherMethod()  # 张三在说话，我会武功
son.useMotherMethod2()  # 张三在说话，我会剑法
# son.useFatherMethod2()  # 张三在说话,我会武功（用的是父类的kongfu）