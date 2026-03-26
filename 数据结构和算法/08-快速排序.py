# 快速排序
"""
1. 首先设定一个分界值，通过该分界值将数组分为左右两部分
2. 将大雨或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边。
3. 然后，左边和右边的数据可以独立排序。对于左侧的数组数据，又可以取一个分界值，将该部分数据分为左右两部分，同样左边放较小值，右边放较大值。右侧的数组数据也可以做类似处理。
4. 重复上述过程，可以看出这是一个递归定义。通过递归将左侧部分排好序后，再递归排好右侧部分的顺序。当左侧和右侧两个部分的数据排完序后，整个数组的排序也就完成了。
"""


def quick_sort(alist, start, end):
    """
    alist: 待排序的列表
    start: 起始位置
    end: 结束位置
    """
    # 如果起始位置大于等于结束位置，则返回
    if start >= end:
        return
    # 设置分界值,默认取第一个元素
    mid = alist[start]
    # 设置左右指针
    left = start
    # 设置右指针
    right = end
    # 循环条件 左指针小于右指针
    while left < right:
        # 只要分界值右边的数据比分界值大，right就减1
        while left < right and alist[right] >= mid:
            right -= 1
        # 将右指针的数据赋值给左指针
        alist[left] = alist[right]
        # 只要分界值左边的数据比分界值小，left就加1
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
    # 走到这里既left=right，将分界值赋值给left指针
    alist[left] = mid
    # 递归排序左边的数据
    quick_sort(alist, start, left - 1)
    # 递归排序右边的数据
    quick_sort(alist, left + 1, end)
    return alist

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(alist, 0, len(alist) - 1))