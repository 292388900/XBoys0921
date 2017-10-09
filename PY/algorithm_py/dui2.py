#!/usr/bin/env python
# coding: utf-8

# 随机初始化指定长度的数组
def init1(length):
    import random
    A = []
    for i in range(length):
        A.append(int(random.random() * 3 * length) + 1)
    return A


# 返回一个随机排列的数组
def init2():
    return [19, 27, 30, 2, 12, 14, 14, 17, 28, 8, 6, 21, 10, 26, 22, 24, 24, 11, 1, 22]


# 以堆的形式打印数组
def printdui(A):
    for i in range(0, parent(len(A) - 1) + 1):
        if (i + 1) * 2 < len(A):
            print i, ":", A[i], A[(i + 1) * 2 - 1], A[(i + 1) * 2],
        else:
            print i, ":", A[i], A[(i + 1) * 2 - 1],
        print


# 获得下标为i的父节点
def parent(i):
    return (i - 1) / 2


# 获得节点为i的左子节点
def left(i):
    return i * 2 + 1


# 获得节点为idea右子节点
def right(i):
    return i * 2 + 2


# 保持A 在i节点后到length的最大堆性质，
# 返回true表示该节点左右节点小于该节点。
# 返回false表示该节点需调整最大堆，并递归更新左右节点。
def keepmaxdui(A, i, length):
    aisMax = False
    t = parent(length - 1) + 1
    if i in range(0, t):
        if (i + 1) * 2 < length:
            a = A[i]
            b = A[left(i)]
            c = A[right(i)]

            if a >= b:
                if a >= c:
                    aisMax = True
                else:
                    A[i] = c
                    A[right(i)] = a
                    keepmaxdui(A, right(i), length)
            else:
                if b >= c:
                    A[i] = b
                    A[left(i)] = a
                    keepmaxdui(A, left(i), length)
                else:
                    A[i] = c
                    A[right(i)] = a
                    keepmaxdui(A, right(i), length)
        else:
            a = A[i]
            b = A[left(i)]
            if a < b:
                A[i] = b
                A[left(i)] = a
            else:
                aisMax = True
    return aisMax


# 从底向上，A，初始化出一个最大堆
def initdui(A):
    t = parent(len(A) - 1) + 1
    for i in range(t):
        i = t - 1 - i
        keepmaxdui(A, i, len(A))


# 排序，返回的结果从大到小，A调整为从小到大
def sort(A):
    result = []
    initdui(A)
    length = len(A)

    for i in range(len(A)):
        result.append(A[0])
        length -= 1
        temp = A[0]
        A[0] = A[length]
        A[length] = temp
        keepmaxdui(A, 0, length)
    return result


# 测试
if __name__ == "__main__":
    A = init2()
    print A
    result = sort(A)
    print A
    print [1, 2, 6, 8, 10, 11, 12, 14, 14, 17, 19, 21, 22, 22, 24, 24, 26, 27, 28, 30]
    print
    print result
