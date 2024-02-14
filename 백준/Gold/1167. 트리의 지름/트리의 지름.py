import sys
input = sys.stdin.readline


def dfs(start):
    visited = [0] * (V + 1)
    stack = [[start, 0]]
    visited[start] = 1

    node, distance = start, 0
    while stack:
        cNode, cDistance = stack.pop()
        if cDistance > distance:
            distance = cDistance
            node = cNode

        for c, w in children[cNode]:
            if not visited[c]:
                visited[c] = 1
                stack.append([c, cDistance + w])

    return [node, distance]


V = int(input())
children = [[]for _ in range(V + 1)]

for _ in range(1, V + 1):
    node = list(map(int, input().split()))
    p = node[0]
    for i in range(1, len(node) - 1, 2):
        c, w = node[i], node[i + 1]
        children[p].append([c, w])

node1, tmp = dfs(1)
node2, answer = dfs(node1)

print(answer)