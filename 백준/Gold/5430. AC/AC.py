import sys
input = sys.stdin.readline
from collections import deque


def AC():
    flag = 1
    for i in p:
        if i == 'R':
            if flag:
                flag = 0
            else:
                flag = 1
        else:
            if not len(arr):
                return 'error'
            if flag:
                arr.popleft()
            else:
                arr.pop()
    if not flag:
        arr.reverse()
    return '[' + ','.join(arr) + ']'


t = int(input())

for j in range(t):
    p = input().rstrip()
    n = int(input())
    if n:
        arr = deque(input().strip().strip('[]').split(','))
    else:
        trash = input()
        arr = deque()
    print(AC())
