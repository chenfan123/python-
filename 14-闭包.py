# 闭包
def test():
    a = 100

    def test_in(b):
        print(a + b)
    return test_in


f = test()
f(6)
