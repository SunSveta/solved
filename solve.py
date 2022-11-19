#!/usr/bin/python3
def solve(n, repeats):
    lst = []
    sum = 0
    for i in range(1, repeats + 1):
        lst.append(str(n)*i)
    for i in lst:
        sum += int(i)
    print(sum)

