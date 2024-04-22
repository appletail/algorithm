import sys
input = sys.stdin.readline

def chicken_distance(n, s, cd):
    if n == M:
        sum_cd = 0
        for r, c in houses:
            cur_cd = 1e10
            for sr, sc in selected:
                cur_cd = min(cur_cd, abs(r-sr) + abs(c-sc))
            sum_cd += cur_cd
            if sum_cd >= cd:
                return cd
        return  sum_cd
    else:
        for idx in range(s, len(chicken_restaurants)):
            selected.append(chicken_restaurants[idx])
            cd = chicken_distance(n+1, idx+1, cd)
            selected.pop()
        return cd

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses, chicken_restaurants = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chicken_restaurants.append([i, j])

selected = []
print(chicken_distance(0, 0, 1e10))
