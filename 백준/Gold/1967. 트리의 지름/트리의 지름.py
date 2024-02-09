import sys
input = sys.stdin.readline


def dfs(start):
    visited = [0] * (n + 1)
    stack = [[start, 0]]
    visited[start] = 1

    node, distance = start, 0
    while stack:
        cNode, cDistance = stack.pop()
        if cDistance > distance:
            distance = cDistance
            node = cNode

        if parents[cNode]:
            p, w = parents[cNode]
            if not visited[p]:
                visited[p] = 1
                stack.append([p, cDistance + w])
        for c, w in children[cNode]:
            if not visited[c]:
                visited[c] = 1
                stack.append([c, cDistance + w])

    return [node, distance]


n = int(input())
parents = [0] * (n + 1)
children = [[]for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    children[p].append([c, w])
    parents[c] = [p, w]

node1, tmp = dfs(1)
node2, answer = dfs(node1)

print(answer)
