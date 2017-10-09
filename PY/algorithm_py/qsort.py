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


def part(A, p, r):
    x = A[r]
    q = p - 1
    for j in range(p, r):
        if A[j] < x:
            q = q + 1
            if not q == j:
                temp = A[j]
                A[j] = A[q]
                A[q] = temp
    q = q + 1
    temp = A[q]
    A[q] = A[r]
    A[r] = temp
    return q


def sort(A, p, r):
    if p < r:
        q = part(A, p, r)
        sort(A, 0, q - 1)
        sort(A, q + 1, r)


if __name__ == "__main__":
    A = init2()
    print A
    sort(A, 0, len(A) - 1)
    print A
    print [1, 2, 6, 8, 10, 11, 12, 14, 14, 17, 19, 21, 22, 22, 24, 24, 26, 27, 28, 30]
