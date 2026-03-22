# 把函数当作变量来使用
# property的装饰器用法
# # @property 修饰 获取值的函数
## @获取值的函数名.setter 修饰 设置值的函数
class Person:
    def __init__(self):
        self.__name = 'test'
        self.__age = 11

    @property
    def get_name(self):
        return self.__name

    # 修改属性
    @get_name.setter
    def name(self, value):
        self.__name = value
        

if __name__ == '__main__':
    person = Person()
    print(person.name)
    person.name = 'test2'
    print(person.name)