# 类属性方式：类属性 = property(获取值的函数, 设置值的函数)
class Person:
    def __init__(self):
        self.__name = 'test'
        self.__age = 11

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    name = property(get_name, set_name)

if __name__ == '__main__':
    person = Person()
    print(person.name)
    person.name = 'test2'
    print(person.name)