import copy


def dm01_普通赋值():
    # 普通赋值 - 不可变类型
    a = 10
    b = a
    print(id(a))  # 假设地址为0x01
    print(id(b))  # 则同为0x01
    print(b)  # 10
    # 普通赋值 - 可变类型
    c = [1, 2, 3]
    d = [11, 22, 33]
    e = [c, d]
    d = e
    print(id(e))  # 0x02
    print(id(d))  # 0x02


def dm02_浅拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [7, 8, a, b]
    d = copy.copy(c)
    print(f"id(c){id(c)}和id(d){id(d)}值不一样，说明浅拷贝第一层")
    print(id(c[2]))  # 0x01
    print(id(a))  # 0x01
    print("id(c[2])和id(a)值一样，说明浅拷贝第2层的数据")

    # 修改a[2] = 22
    a[2] = 22
    print(c)  # [7, 8,[1,2,22], [11, 22, 33]]
    print(d)  # [7,8,[1,2,22], [11, 22, 33]]


def dm03_浅拷贝不可变类型():
    a = (1, 2, 3)
    b = (11, 12, 13)
    c = (6, 7, a, b)
    d = copy.copy(c)
    print(id(c))  # 0x01
    print(id(d))  # 0x01


def dm04_深拷贝可变类型():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [6, 7, a, b]
    d = copy.deepcopy(c)
    print(id(c))  # 0x01
    print(id(d))  # 0x02
    a[1] = 110
    b[1] = 800
    print(c)  # [6, 7, [1, 100, 3], [11, 800, 33]]
    print(d)  # [6, 7, [1, 2, 3], [11, 22, 33]]
