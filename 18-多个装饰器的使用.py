# 多个装饰器的使用

# 多个装饰器装饰一个原函数，按照由内向外的顺序装饰。单如果用装饰器的语法糖来写，看到的效果是从上往下执行

# 需求发表评论前，先登录，再验证码，再发布

def login_required(func):
    def wrapper():
        print('登录')
        func()
    return wrapper

def captcha_required(func):
    def wrapper():
        print('验证码')
        func()

    return wrapper
    
# 从上往下装饰
@login_required
@captcha_required
def comment():
    print('发表评论')

comment()