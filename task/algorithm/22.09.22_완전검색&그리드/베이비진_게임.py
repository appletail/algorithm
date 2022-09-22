import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    baby = list(map(int, input().split()))

    p1, p2 = baby[0: 6], baby[6: 12]
