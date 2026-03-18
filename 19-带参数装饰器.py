# 带有参数的装饰器

def logging(flag):
    def decorator(func):
        def inner(num1, num2):
            if flag == '+':
                print('++++++')
                result = func(num1, num2)
                print(result)
            elif flag == '-':
                print('------')
                result = func(num1, num2)
                print(result)
        return inner
    return decorator

@logging('+')
def add(num1, num2):
    return num1 + num2

@logging('-')
def sub(num1, num2):
    return num1 - num2

add(10, 20)
