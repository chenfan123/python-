import re

# 正则校验,参1正则规则，参2:要被校验的字符串
result = re.match('hello..', 'hello world')
if result:
    print(result.group()) # hello w
else:
    print('匹配失败')