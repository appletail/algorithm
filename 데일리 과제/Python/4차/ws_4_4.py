word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

sum1 = 0
sum2 = 0

for i in range(len(word1)):
    sum1 += ord(word1[i])

for j in range(len(word2)):
    sum2 += ord(word2[j])


if sum1 > sum2:
    print(word1)
else:
    print(word2)