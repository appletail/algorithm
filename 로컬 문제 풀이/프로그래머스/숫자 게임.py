test = [
    [2, 9, [4, 5]],
    [2, 1, [-1]],
    [2, 8, [4, 4]],
    [10000, 99999999, [1, 1]]
]
for n, s, result in test:
    answer = solution(n, s)
    print('====================================')
    print('pass' if answer == result else 'fail')
    print('====================================')
    print()
