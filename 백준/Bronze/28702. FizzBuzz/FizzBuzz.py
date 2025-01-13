def isFizzBuzz(i):
    i = int(i)
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i

strings = [input() for _ in range(3)]
i = 0
for idx in range(3):
    if strings[idx].isdigit():
        i += int(strings[idx]) + 3 - idx
        break
print(isFizzBuzz(i))