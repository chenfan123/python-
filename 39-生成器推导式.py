# 创建生成器
# 注意一：括号()代表这是一个生成器，不是元祖
# 注意二：括号()里面写的是数据的生成规则，返回一个对象，对象内不是存的数据，而是产生数据的规则

my_generator = (i * 2 for i in range(5))

print(my_generator)

# next 获取生成器下一个值
value = next(my_generator)
print(value) # <generator object <genexpr> at 0x1024dde50>

# for 循环遍历生成器   
for value in my_generator:
    print(value) # 0 2 4 6 8
 