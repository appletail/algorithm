fruits = list(input().split(','))

for i in range(len(fruits)):
    fruits[i] = fruits[i].lower()

    if 'rotten' in fruits[i]:
        fruits[i] = fruits[i][6:]

print(fruits)