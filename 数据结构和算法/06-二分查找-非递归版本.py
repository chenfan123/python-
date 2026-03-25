# 非递归版
def binary_search(alist, item):
    # 1. 设置初始化搜索空间 起始位置和结束位置   
    first = 0
    last = len(alist) - 1
    # 2. 循环条件 起始位置小于等于结束位置
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False