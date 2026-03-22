# 只要在def函数里面看到有yield关键字，那么就是生成器
def mygenerator(n):
    for i in range(n):
        print(f'开始生成数据：{i}')
        # yield 做了3件事：1， 创建生成器对象2.把值存储到生成器中 3. 返回生成器
        yield i
        print(f'结束生成数据：{i}')


if __name__ == '__main__':
    g = mygenerator(5)
    # 获取生成器中下一个值
    result = next(g)
    result2 = next(g)
    result3 = next(g)
    print(result)