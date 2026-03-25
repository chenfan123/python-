# 冒泡排序
# 相邻位置两个元素比较，前面的元素比后面的元素大则交换。每一轮比较后，最大的元素会交换到末尾位置。

def bubble_sort(alist):

    for j in range(len(alist) - 1, 0, -1):
        count = 0
        for i in range(j):
            if alist[i] > alist[i + 1]:
                count += 1
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        if count == 0:
            break
    return alist


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(bubble_sort(alist))
