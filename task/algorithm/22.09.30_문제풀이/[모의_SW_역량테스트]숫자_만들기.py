import sys
sys.stdin = open("input.txt", "r")


def mima(k):
    global minV, maxV

    if k == N - 1:
        result = nums[0]
        for i in range(1, N):
            if yeonsan[i - 1] == 0:
                result += nums[i]

            elif yeonsan[i - 1] == 1:
                result -= nums[i]

            elif yeonsan[i - 1] == 2:
                result *= nums[i]

            elif yeonsan[i - 1] == 3:
                result = int(result / nums[i])

        minV = min(minV, result)
        maxV = max(maxV, result)

    else:
        for i in range(4):
            if yeonsanja[i]:
                yeonsan.append(i)
                yeonsanja[i] -= 1
                mima(k + 1)
                yeonsanja[i] += 1
                yeonsan.pop()


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    yeonsanja = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    minV, maxV = 1e10, -1e10
    yeonsan = []
    mima(0)
    print(f'#{test_case}', maxV - minV)
