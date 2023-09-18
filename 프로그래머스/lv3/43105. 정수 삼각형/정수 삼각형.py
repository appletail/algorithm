def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            left, right = j - 1, j
            if left < 0:
                triangle[i][j] += triangle[i - 1][right]
            elif right >= len(triangle[i - 1]):
                triangle[i][j] += triangle[i - 1][left]
            else:
                triangle[i][j] += max(triangle[i - 1][left], triangle[i - 1][right])

    return max(triangle[-1])