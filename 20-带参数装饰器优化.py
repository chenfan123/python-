def decorator(func):
    def inner(num1, num2):
        if func.__name__ == 'get_sun':
            print('++++++')
            result = func(num1, num2)
            print(result)
        elif func.__name__ == 'get_sun2':
            print('------')
            result = func(num1, num2) 
            print(result)

    return inner
    
@decorator
def get_sun(num1, num2):
    return num1 + num2

@decorator
def get_sun2(num1, num2):
    return num1 - num2

get_sun(10, 20)
get_sun2(10, 20)