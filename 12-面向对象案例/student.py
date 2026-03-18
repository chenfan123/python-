"""
用于记录 学生类，学生的属性信息为：姓名、性别、年龄、手机号、描述信息
"""


class Student(object):
    """学生类，包含学生信息"""

    def __init__(self, name, gender, age, phone, desc):
        """
        用于初始化属性信息
        :param name: 姓名
        :param gender: 性别
        :param age: 年龄
        :param phone: 手机号
        :param desc: 描述信息
        """
        self.name = name  # 姓名
        self.gender = gender  # 性别
        self.age = age  # 年龄
        self.phone = phone  # 手机号
        self.desc = desc  # 描述信息

    # 定义魔法方法，用于打印学生信息
    def __str__(self):
        return f'学生信息：{self.name}，性别：{self.gender}，年龄：{self.age}，手机号：{self.phone}，描述信息：{self.desc}'


# 测试
if __name__ == '__main__':
    student = Student('张三', '男', 18, '13800138000', '学生')
    print(student)
