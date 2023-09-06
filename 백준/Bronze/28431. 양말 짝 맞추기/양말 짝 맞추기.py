count = [0] * 10
for _ in range(5):
    num = int(input())
    count[num] += 1

answer = 0
for i in range(10):
    if count[i] % 2:
        answer = i

print(answer)
