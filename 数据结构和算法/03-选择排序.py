# 选择排序
"""
第一次从待排序的数据元素中选出最小或者最大的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，放到已排序的序列的末尾，以此腿累，知道全部待排序的数据元素的个数为0.
"""


def selection_sort(alist):
    for j in range(len(alist) - 1):
        # 假定的最小值的下标
        min_index = j
        # 从假定的最小值的下一个位置开始比较
        for i in range(j + 1, len(alist)):
            # 如果找到比假定的最小值还小的值，则更新最小值的下标
            if alist[i] < alist[min_index]:
                min_index = i
        # 如果找到比假定的最小值还小的值，则交换位置
        alist[j], alist[min_index] = alist[min_index], alist[j]
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(selection_sort(alist))
