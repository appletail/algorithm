import sys
sys.stdin = open("input.txt", "r")


def bfs(s_arr):
    tmp = []
    result = []
    q = s_arr
    while q or tmp:

        for num in range(len(tmp)):
            if tmp and not graph_pre[tmp[num]]:
                v = tmp.pop(num)
                break
        else:
            v = q.pop(0)

        if graph_pre[v]:
            tmp.append(v)
        else:
            visited[v] = 1
            result.append(v)
            for w in graph_next[v]:
                if not visited[w] and w not in tmp and w not in q:
                    q.append(w)
                if v in graph_pre[w]:
                    graph_pre[w].remove(v)

    return result


for test_case in range(1, 11):
    v, e = map(int, input().split())

    graph_next = [[] for _ in range(v + 1)]
    graph_pre = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    tmp_lst = list(map(int, input().split()))

    for i in range(0, e * 2, 2):
        graph_next[tmp_lst[i]].append(tmp_lst[i + 1])
        graph_pre[tmp_lst[i + 1]].append(tmp_lst[i])
    start = []
    for i in range(1, v + 1):
        if not graph_pre[i]:
            start.append(i)

    print(f'#{test_case}', *bfs(start))


# 다른 답
for tc in range(1, 11):
    v, e = map(int, input().split())
    lst = list(map(int, input().split()))
    par = [[] for _ in range(v + 1)]
    for i in range(e):
        p, c = lst[i * 2], lst[i * 2 + 1]
        par[c].append(p)

    result = []
    q = []

    while len(result) != v:
        for j in range(1, v + 1):
            if not par[j] and j not in result:
                result.append(j)
                q.append(j)
        while q:
            a = q.pop()
            for j in range(1, v + 1):
                if a in par[j]:
                    par[j].remove(a)

    print(f'#{tc}', end=' ')
    print(*result)