import sys
input = sys.stdin.readline

# 제출한 답 - 292ms
def solution1():
    N = int(input())
    A = list(map(int, input().split()))

    forward = [0] * N
    backward = [0] * N
    forward[0] = 1
    backward[-1] = 1
    
    for i in range(1, N):
        for j in range(i):
            forward[i] = max(forward[i], (forward[j] if A[i] > A[j] else 0) + 1)

    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            backward[i] = max(backward[i], (backward[j] if A[i] > A[j] else 0) + 1)

    answer = 1
    for i in range(N):
        answer = max(answer, forward[i]+backward[i])

    print(answer-1)

# 다른 답 - 40ms
from bisect import bisect_left
n = int(input().strip())
nums = list(map(int, input().strip().split()))

def calculate_lis(nums):
    sub = []  # LIS를 유지하기 위한 배열
    lis = [0] * len(nums)  # 각 위치에서의 LIS 길이

    for i, x in enumerate(nums):
        pos = bisect_left(sub, x)  # x가 들어갈 위치 찾기
        if pos == len(sub):
            sub.append(x)  # x를 LIS 끝에 추가
        else:
            sub[pos] = x  # 기존 값을 x로 대체
        lis[i] = pos + 1  # LIS 길이 저장
    return lis

lis = calculate_lis(nums)
lds = calculate_lis(nums[::-1])[::-1]
max_length = 0
for i in range(len(nums)):
    max_length = max(max_length, lis[i] + lds[i] - 1)

print(max_length)
