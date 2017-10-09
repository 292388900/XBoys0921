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


def getMax(A):
    temp = 0;
    for i in range(len(A)):
        if temp < A[i]:
            temp = A[i]
    return temp


def sort(A, k=100):
    B = []
    C = []
    for i in range(len(A)):
        B.append(0)
    for i in range(k+1):
        C.append(0)

    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]
    print "C",C

    for i in range(len(A)):
        B[C[A[i]]-1]=A[i]
        C[A[i]]=C[A[i]]-1
    return B


if __name__ == "__main__":
    A = init2()
    print A
    print sort(A, k=getMax(A))
    print [1, 2, 6, 8, 10, 11, 12, 14, 14, 17, 19, 21, 22, 22, 24, 24, 26, 27, 28, 30]
