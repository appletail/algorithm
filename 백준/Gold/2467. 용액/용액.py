import sys
input = sys.stdin.readline

def binarySearch(start, end, value):
    left, right = start+1, end-1
    answer = []
    while left <= right:
        mid = (right + left) // 2
        if abs(arr[start]+arr[mid]) < value:
            value = abs(arr[start]+arr[mid])
            answer = [arr[start], arr[mid]]
        if 1 > mid-1 or mid+1 >= end:
            break
        if abs(arr[start]+arr[mid-1]) < abs(arr[start]+arr[mid+1]):
            right = mid - 1
        else:
            left = mid + 1

    return [value, answer]
N = int(input())
arr = list(map(int, input().split()))

answer = []
value = 1e10
for i in range(N):
    tmpValue, tmpAnswer = binarySearch(i, N, value)
    if value > tmpValue:
        value = tmpValue
        answer = tmpAnswer

print(*sorted(answer))
