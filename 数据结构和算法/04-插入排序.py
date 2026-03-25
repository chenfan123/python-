# 插入排序
"""
将无序序列的第一个元素插入到有序序列的合适位置，直到所有元素都插入到有序序列中。
"""


def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        for i in range(j, 0, -1):
            # alist[i]为待插入的数据
            # 若待插入数据小于有序数据，则插入；若待插入数据大于有序数据，则break
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insert_sort(alist))