# nonlocal 关键字
# 声明能够让内部函数去修改外部函数的变量
def func_out():
    num = 100
    def func_in():
        nonlocal num
        num = 200
        print(num)
    return func_in

func_out()() 