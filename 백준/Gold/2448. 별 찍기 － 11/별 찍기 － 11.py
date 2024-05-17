def stargazing(x, y):
    stars[x][y] = '*'
    stars[x+1][y-1], stars[x+1][y+1] = '*', '*'
    for i in range(5):
        stars[x+2][y-2+i] = '*'


N = int(input())
col = N * 2 - 1
stars = [[' '] * col for _ in range(N)]
stargazing(0, N-1)
start, end = (N-1) - 3, (N-1) + 3
for r in range(3, N, 3):
    for c in range(start, end+1):
        star_count = 0
        for i in range(-1, 2):
            if stars[r-1][c+i] == '*':
                star_count += 1
        if star_count == 1:
            stargazing(r, c)
    start -= 3
    end += 3
for i in range(N):
    print(''.join(stars[i]))
