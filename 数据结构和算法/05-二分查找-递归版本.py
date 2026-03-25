# 又称折半查找
# 原理：将数组分为三部分，依次是中值前，中值，中值后；将要查找的值与中值进行比较，若小于中值则在中值前面找，若大于中值则在中值后面找，等于中值直接返回。
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)