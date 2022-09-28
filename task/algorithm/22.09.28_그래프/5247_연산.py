import sys
sys.stdin = open("input.txt", "r")

from collections import deque


def yeonsan(v, g):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return visited[v]
        if 0 < v + 1 < 1000001 and not visited[v + 1]:
            q.append(v + 1)
            visited[v + 1] = visited[v] + 1
        if 0 < v - 1 < 1000001 and not visited[v - 1]:
            q.append(v - 1)
            visited[v - 1] = visited[v] + 1
        if 0 < v * 2 < 1000001 and not visited[v * 2]:
            q.append(v * 2)
            visited[v * 2] = visited[v] + 1
        if 0 < v - 10 < 1000001 and not visited[v - 10]:
            q.append(v - 10)
            visited[v - 10] = visited[v] + 1


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    visited = [0] * 1000001
    print(f'#{test_case}', yeonsan(n, k) - 1)


# 반복문으로 구현
from collections import deque


def yeonsan(v, g):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        if v == g:
            return visited[v]
        for i in [(v + 1), (v - 1), (v * 2), (v - 10)]:
            if 0 < i < 1000001 and not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    visited = [0] * 1000001
    print(f'#{test_case}', yeonsan(n, k) - 1)
