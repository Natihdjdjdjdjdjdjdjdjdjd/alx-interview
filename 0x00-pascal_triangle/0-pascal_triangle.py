#!/usr/bin/python3

def pascal_triangle(n):
    m = []
    if n <= 0:
        return m
    m = [[1]]
    for x in range(1, n):
        temp = [1]
        for y in range(len(m[x - 1]) - 1):
            curr = m[x - 1]
            temp.append(m[x - 1][y] + m[x - 1][y + 1])
        temp.append(1)
        m.append(temp)
    return m
