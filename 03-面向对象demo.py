class Student:

    def __init__(self, weight,name):
        self.weight = weight
        self.name = name

    def run(self):
        print(f'{self.name}在跑步')
        self.weight -= 0.5

    def eat(self):
        print(f'{self.name}在吃饭')
        self.weight += 2

    def __str__(self):
        return f'{self.name}的体重是{self.weight}'

student = Student(75.5, '张三')
student.run()
student.eat()
print(student)