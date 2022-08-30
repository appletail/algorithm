s_triangle = list(map(int, input().split()))
s_triangle.sort()

if sum(s_triangle[:2]) < s_triangle[2]:
    print('삼각형 아님')
elif len(set(s_triangle)) == 1:
    print('정삼각형')
elif s_triangle[0] ** 2 + s_triangle[1] ** 2 == s_triangle[2] ** 2:
    print('직각삼각형')
elif len(set(s_triangle)) == 2:
    print('이등변삼각형')
else:
    print('삼각형')


# 세 변 동일 = 정삼각형
# 두 변 동일 = 이등변 삼각형
# 피타고라스 일치 = 직각삼각형 출력
# 일반 삼각형 = 삼각형
# 삼각형 아닌 경우 = 삼각형 아님
# 짧은 두 변의 길이의 합이 가장 긴변의 길이보다 크다면 삼각형 될 수 있음

# 삼각형 판별  => 삼각형 아님

# 정삼각형 판별

# 직각삼각형 판별

# 이등변 삼각형 판별

# 일반 삼각형 => 삼각형