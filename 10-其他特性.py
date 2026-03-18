# 类属性
class Person:
    """人员类，包含类属性和实例属性示例。"""

    country = '中国'
    nickName = '44'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        """说话方法"""
        print(f'{self.name}说：你好')


Person.nickName = '李四'
print(Person.nickName, Person.country)  # 李四 中国


person = Person('张三', 18)
print(person.name)  # 张三
print(person.nickName)  # 李四
