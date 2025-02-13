from collections import deque

def findRedRoutes(maze, redPos, redGoal):
    n, m = len(maze), len(maze[0])
    visited = [[-1] * m for _ in range(n)]
    visited[redPos[0]][redPos[1]] = 0
    stack = [redPos]

    while stack:
        r, c = stack.pop()
        if r == redGoal[0] and c == redGoal[1]:

        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r + dr, c + dc

def solution(maze):
    answer = 0
    redPos, bluePos, redGoal, blueGoal = [0, 0], [0, 0], [0, 0], [0, 0]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                redPos = [i, j]
            elif maze[i][j] == 2:
                bluePos = [i, j]
            elif maze[i][j] == 3:
                redGoal = [i, j]
            elif maze[i][j] == 4:
                blueGoal = [i, j]

    redRoutes = findRedRoutes(maze, redPos, redGoal)
    return answer


test = [
    [[[1, 4], [0, 0], [2, 3]], 3],
    [[[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]], 7],
    [[[1, 5], [2, 5], [4, 5], [3, 5]], 0],
    [[[4, 1, 2, 3]], 0],
]

for maze, result in test:
    answer = solution(maze)
    print('pass' if answer == result else 'fail')
