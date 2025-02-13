def solution(routes):
    answer = 0
    return answer


test = [
    [[[-20, -15], [-14, -5], [-18, -13], [-5, -3]], 2]
]
for routes, result in test:
    answer = solution(routes)
    print('====================================')
    print('pass' if answer == result else 'fail')
    print('====================================')
    print()
