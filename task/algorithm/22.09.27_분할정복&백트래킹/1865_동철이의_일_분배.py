import sys
sys.stdin = open("input.txt", "r")


def boonbae(k, curM):
    global result
    if curM <= result:
        return

    if k == N:
        result = max(result, curM)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                boonbae(k + 1, curM * jikwon[k][i] / 100)
                visited[i] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    jikwon = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    boonbae(0, 1)

    print(f'#{test_case} {result * 100:.6f}')


# 다른 답
def per(row, now_per):
    global max_per

    if row == n:
        max_per = max(max_per, now_per)
        return

    elif now_per <= max_per:
        return

    else:
        for col in range(n):
            if not visited[col]:
                visited[col] = 1
                per(row + 1, now_per * arr[row][col])
                visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(n)]
    visited = [0] * (n + 1)
    max_per = 0
    per(0, 1)
    print(f'#{tc}', format(max_per * 100, '.6f'))