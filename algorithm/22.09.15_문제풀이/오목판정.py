import sys
sys.stdin = open("input.txt", "r")


def check():
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 'o':
                for dr, dc in dt:
                    for dis in range(1, 5):
                        nr, nc = r + dr * dis, c + dc * dis
                        if 0 <= nr < n and 0 <= nc < n:
                            if arr[nr][nc] == '.':
                                break
                        else:
                            break
                    else:
                        return 'YES'
    return 'NO'


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    dt = [(0, 1), (1, 0), (1, 1), (1, -1)]

    print(f'#{test_case} {check()}')
