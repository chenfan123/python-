# 装饰器：本质是一个闭包函数，目的是在不改变原有函数的基础上，对其功能做增强。

# 装饰器的用法：
# 格式一：传统写法
'''
装饰后的函数名 = 装饰器名（被装饰的原函数名）
装饰后的函数名()
'''

# 格式2:语法糖
'''
@装饰器名
def 函数名():
    pass
'''

# 需求：在发表评论前都是需要先登录的

# 1. 定义外部函数表示登陆，形参列表接受要被装饰的函数名
def login_required(func):
    def wrapper():
        print('登录')
        func()
    return wrapper


# 2. 定义函数，表示发布评论
def comment():   
    print('发表评论')


def payment():
    print('支付成功')

login_comment = login_required(comment)
login_comment()

login_payment = login_required(payment)
login_payment()

# 语法糖写法
@login_required
def buy():
    print('购买商品')

@login_required
def sell():
    print('卖出商品')

buy()
sell()