# 装饰器装饰无参无返回值的函数
def print_log(func):
    def wrapper():
        func()

    return wrapper
    
@print_log
def get_sun():
    a = 10
    b = 10
    c = a + b
    print(c)


get_sun()  # 开始计算 20 计算结束

# 装饰器装饰有参无返回值的函数
def print_log2(func):
    def wrapper(a, b):
        func(a, b)

    return wrapper
    
@print_log2
def get_sun2(a, b):
    c = a + b
    print(c)


get_sun2(20, 10)  # 开始计算 30 计算结束

# 装饰器装饰无参有返回函数
def print_log3(func):
    def wrapper():
       return func()

    return wrapper
    
@print_log3
def get_sun3():
    return 10


print(get_sun3())  # 10

# 装饰器装饰有参有返回值函数
def print_log4(func):
    def wrapper(a, b):
        return func(a, b)
    return wrapper
@print_log4
def get_sun4(a, b):
    return a + b


print(get_sun4(10, 10))  # 20

# 装饰器装饰函数参数不定长，有返回值的
def print_log5(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
    
@print_log5
def get_sun5(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(get_sun5(10, 10, 10,a=1,b=2,c=4))  # 30