#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 17/11/17 下午6:55
# @Author  : zpy
# @Software: PyCharm


def d_inject(arr, i, j, n, m):
    """dfs 标记"""
    if i<0 or i>=n or j<0 or j>=m or arr[i][j]!=1:
        return
    arr[i][j] = 2
    d_inject(arr, i - 1, j, n, m)
    d_inject(arr, i + 1, j, n, m)
    d_inject(arr, i, j - 1, n, m)
    d_inject(arr, i, j + 1, n, m)


def b_inject(arr, i, j, n, m):
    """bfs 标记"""
    tmp = [[i,j]]
    while len(tmp)>0:
        i, j = tmp.pop()
        arr[i][j] = 2
        if i >= n or j >= m:
            break
        if i<n-1 and arr[i+1][j] == 1:
            tmp.append([i+1, j])
        if i>0 and arr[i-1][j] == 1:
            tmp.append([i-1, j])
        if j<m-1 and arr[i][j+1] == 1:
            tmp.append([i, j+1])
        if j>0 and arr[i][j-1] == 1:
            tmp.append([i, j-1])


def count_lands(data):
    res = 0
    n, m = len(data), len(data[0])
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                res += 1
                b_inject(data, i, j, n, m)
                # d_inject(data, i, j, n, m)
    return res

if __name__ == '__main__':
    data = [
      [1, 1, 0, 0, 0],
      [0, 1, 0, 0, 1],
      [0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1]
    ]
    # d_inject(data, 0, 0, 5, 5)
    print(count_lands(data))
    print(data)













