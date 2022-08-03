count = 2
words = []

while True:
    a = input()

    if a == 'done':
        break
    else:
        words.append(a)

for i in range(0, len(words) - 1):
    if words[i][-1] == words[i + 1][0]:
        count += 1
    else:
        print(f'{count}번째 사람이 탈락했습니다.')
        break