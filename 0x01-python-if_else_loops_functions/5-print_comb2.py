#!/usr/bin/python3
num = 0
while num < 100:
    if num != 99:
        print('{0:02d}'.format(num), end=', ')
    else:
        print(num)
    num += 1
