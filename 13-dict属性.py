# __dict__ 属性
# 是python的内置属性，可以把对象转成字典形式
class Dog:
    def __init__(self, name):
        self.name = name


dog1 = Dog('旺财')
dog2 = Dog('小黑')
dog3 = Dog('大黄')
dog_list = [dog1, dog2, dog3]

# 列表推导式
dog_dict_list = [dog.__dict__ for dog in dog_list]
print(dog_dict_list)

dog4 = {
    "name": "xixi"
}

newDog = Dog(**dog4)
print(newDog.name)
