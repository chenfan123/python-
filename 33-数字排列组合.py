"""
1 2 3 4能组合成的四位数有哪些情况，按照5个一行输出
要求：
1. 同时包含 1 2 3 4
2. 要求数字1和3不能挨着
3. 数字4不能开头
4. 5行以内搞定
"""
count = 0
for s in [str(i) for i in range(1234, 3422)]:
    if '1' in s and '3' in s and '4' in s and '2' in s and s[0] != '4' and '13' not in s and '31' not in s:
        count += 1
        print(s, end="\n" if count % 5 == 0 else "\t")

# 已知列表my_list = ['aa','bb','cc','bb','bb','dd']，删除所有bb元素尽可能多的用不同的解决方案
my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'dd']
for item in my_list[:]:  # my_list[:]是my_list的副本，不会影响原列表
    print(item, 'item')
    if item == 'bb':
        my_list.remove(item)
print(my_list)

my_list2 = ['aa', 'bb', 'cc', 'bb', 'bb', 'dd']
my_list3 = [item for item in my_list2 if item != 'bb']
print(my_list3)
